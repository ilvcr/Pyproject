# coding:utf-8

# @Time    : 2019-01-14 15:22
# @Author  : 小贰
# @FileName: ansible_sync_hosts.py
# @function: ansible for python 3.x

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase


class ResultsCollector(CallbackBase):
    """重构执行结果"""
    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
        self.host_skipped = {}

    def v2_runner_on_unreachable(self, result, *args, **kwargs):
        """不可达"""
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        """执行成功"""
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        """执行失败"""
        self.host_failed[result._host.get_name()] = result

    def v2_runner_on_skipped(self, result, *args, **kwargs):
        """跳过不执行"""
        self.host_skipped[result._host.get_name()] = result


def run_ansible(module_name,module_args,host_list,ansible_user="root"):
    """ansible api"""
    # 负责查找和读取yaml、json和ini文件
    loader = DataLoader()

    # 初始化需要的对象
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become',
                          'become_method', 'private_key_file','become_user',
                          'remote_user', 'check', 'diff']
                         )
    options = Options(connection='ssh', module_path=None, forks=5, become=True,
                      become_method='sudo',private_key_file="/root/.ssh/id_rsa",
                      become_user='root', remote_user=ansible_user, check=False, diff=False
                      )

    passwords = dict(vault_pass='secret')

    # 实例化ResultCallback来处理结果
    callback = ResultsCollector()

    # 创建库存(inventory)并传递给VariableManager
    inventory = InventoryManager(loader=loader, sources='')

    for ip in host_list:
        inventory.add_host(host=ip, port=22)

    # 管理变量的类，包括主机，组，扩展等变量
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    for ip in host_list:
        host = inventory.get_host(hostname=ip)
        variable_manager.set_host_variable(host=host, varname='ansible_ssh_pass', value='lzx@2019')

    # 创建任务
    host = ",".join(host_list)

    play_source = dict(
        name="Ansible Play",
        hosts=host,
        gather_facts='no',
        tasks=[
            dict(action=dict(module=module_name, args=module_args), register='shell_out'),
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # 开始执行
    tqm = None

    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback=callback,
    )
    result = tqm.run(play)

    result_raw = {'success': {}, 'failed': {}, 'unreachable': {}}

    for host, result in callback.host_ok.items():
        result_raw['success'][host] = result._result

    for host, result in callback.host_failed.items():
        result_raw['failed'][host] = result._result

    for host, result in callback.host_unreachable.items():
        result_raw['unreachable'][host] = result._result

    for host, result in callback.host_skipped.items():
        result_raw['skipped'][host] = result._result

    return json.dumps(result_raw, indent=4,ensure_ascii=False)

if __name__ == "__main__":
    ansible_user="root"
    module_name = 'script'
    module_args = "/tmp/pycharm_project_279/tools/add_ssh_key.sh"
    host_list = ['192.168.145.129','192.168.145.128']
    ret = run_ansible(module_name,module_args,host_list,ansible_user)
    print(ret)