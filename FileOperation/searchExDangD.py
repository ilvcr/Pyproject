#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
  Author       : Yoghourt.Lee->lvcr
  Last modified: 2018-04-11 22:39
  Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
  Filename     : searchExDangD.py
  Description  : ��һ���ļ�������ָ�����ݵ�����
'''


import codecs
'''
��codecs�ṩ��open������ָ���򿪵��ļ������Ա���,
�����ڶ�ȡ��ʱ���Զ�ת��Ϊ�ڲ���unicode
'''
'''
��һ��
import codecs
filepath=r"FILEPATH\FILENAME"

file=codecs.open(filepath,"rb",encoding="gbk",errors="ignore")
for  line  in  file:#Ӳ��ģʽ
    print(line)
'''
def  loaddata():		#��������
    filepath = r"FILEPATH\FILENAME"		#�ļ�·��
    file = codecs.open(filepath, "rb", encoding="gbk", errors="ignore")		#�ļ��򿪷�ʽ
    global datalist 		#����ȫ��
    datalist=file.readlines() 		#��ȡ�ļ���list
    file.close()		�ر��ļ�
def  search(namestr):
    savefilepath="FILEPATHSAVE"+namestr+".txt"		#�̷�:\\��һ���ļ���\\�ڶ����ļ���\\�������ļ���\\���Ĳ��ļ���\\...
    savefile=open(savefilepath,"wb")		#�ļ�·��
    numbers=0		#number Ϊ������
    for  line  in datalist:		#����
        if line.find(namestr)!= -1:		#�ж�����
            print(line,end="") 		#��ʾ����
            numbers +=1
            savefile.write(line.encode("utf-8"))		#д��
    savefile.write(("����"+str(numbers)).encode("utf-8"))
    savefile.close()


datalist=[]
print("load  file start")
loaddata()
print("load  file end")
while True:
    searchname=input("Ҫ��ѯ������")
    search(searchname)