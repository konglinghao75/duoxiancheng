# -*- coding: utf-8 -*-
"""
使用文档：

经典开启多线程的基本方式

@author: zpj

"""
import threading



class ManyThread:
    
    def __init__(self, factory, worker_num = 5):
        
        self.worker_num = worker_num#工人数量
            
        self.worker_func = factory().worker_func#工做内容及工作函数
    
    def run(self):
        
        
        for i in range(self.worker_num):
            
            t = threading.Thread(target = self.worker_func)
            
            t.start()
            
if __name__ == '__main__':
    
    from factory import Factory
    
    ManyThread(Factory).run()
            
            
        
        
            
    
















