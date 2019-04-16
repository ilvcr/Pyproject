#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_first_common_node_in_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:06:42 2019
# Description: 两个链表中的第一个公共节点
#************************************************************************#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def find_first_common_node_in_linklist(self, pHead1, pHead2):

        if not pHead1 or not pHead2:
            return None

        p1, p2 = pHead1, pHead2
        len1 = len2 = 0

        while p1:
            len1 += 1
            p1 = p1.next

        while p2:
            len2 += 1
            p2 = p2.next

        if len1 > len2:
            while len1-len2:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len2-len1:
                pHead2 = pHead2.next
                len2 -= 1

        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None



