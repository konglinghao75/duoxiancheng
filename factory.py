# -*- coding: utf-8 -*-
"""
使用文档：

本文件构造一个Factory类，

Factory类理解为一个工厂

        其中包含，任务管道，和工作流程


task_pipeline方法

    任务管道,#由于本例task_pipeline是一个迭代器，所以work_task才是真正的管道

worker_func方法

    白话：工人要做的具体工作，即工作流程

    一般是一个循环

    重点要包含：
    
        1  所有工作完成后如何退出

        2  工作中出错了如何处理

        3  一个工作完成后如何处理




@author: zpj

"""

import requests
import re
import sys
import logging
logging.captureWarnings(True)#不打印警告日志


class Factory:
    
    def __init__(self):
        
        self.work_task = self.task_pipeline()#由于本实例是一个迭代器，所以work_task才是真正的管道
        
        self.headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            
        
    def task_pipeline(self):

        '''\
        任务所保存的管道
        由于本实例是一个迭代器，所以self.work_task才是真正的管道


        '''
    
    
        for i in range(200):
    
    
            yield 'https://www.x23us.com/class/1_{}.html'.format(i)
       
    def worker_func(self):
        
        while True:
            
        
            task = next(self.work_task)#重管道中取出一个任务
            
            if task == None:  #线程退出机制
                
                print('队列任务取空')
                
                break
            
            print(task)
            
            try:
                print('_________________')
                r = requests.get(task, verify = False, timeout = 2)#这里的工作是请求一个网页
                r.raise_for_status()
                
            except:#在请求中出错后在下面处理
                
                print('处理出错')
                print(sys.exc_info())
                
            else:#正常请求后处理
            
                regex = '\[简介\]</a><a href="(.*?)" target="_blank">(.*?)</a></td>'
                
                r.encoding = 'gbk'
                
                info = re.findall(regex, r.text)
                
                print(info[:2])
        
        


if __name__ == '__main__':
    

    
    Factory().worker_func()
    
    
    
    
















