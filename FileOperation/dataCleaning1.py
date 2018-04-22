#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
  Author       : Yoghourt.Lee->lvcr
  Last modified: 2018-04-11 22:50
  Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
  Filename     : dataCleaning1.py
  Description  : ʵ��һ���򵥵�������ϴ
'''

import codecs

filepath=r"FILEPATH\FILENAME"
file=codecs.open(filepath,"rb","gbk","ignore")#����ָ������
mylist=file.readlines()#����һ��list,��ȡ���ڴ�


savegoodfilepath=r"FILEPATH\FILENAMESAVEGOOD"
savebadfilepath=r"FILEPATH\FILENAMESAVEBAD"

filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")

for  line  in  mylist:
    if  len(line)>35  or  len(line)<15:
        filebad.write(line.encode("utf-8"))
    else:
        modelist = line.split('----')	#�и����
        if  len(QQlist)==2:
            filegood.write(line.encode("utf-8"))
        else:
            filebad.write(line.encode("utf-8"))

filebad.close()
filegood.close()