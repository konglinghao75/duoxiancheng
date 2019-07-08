# -*- coding: utf-8 -*-
"""
使用文档：

线程池开启多线程的基本方式


@author: zpj

"""


from concurrent.futures import ThreadPoolExecutor


class ManyExecutor:
    
    def __init__(self, factory, worker_num = 5):
        
        self.worker_func = factory().worker_func#工作函数
        
        self.worker_num = worker_num#工人数量
        
        self.executor = ThreadPoolExecutor(max_workers = worker_num)#线程池
        

    
    def run(self):
        
                
      [self.executor.submit(self.worker_func) for i in range(5)]
            
        
if __name__ == '__main__':
    
    from factory import Factory
    #from executor_run import ManyExecutor
    
    ManyExecutor(Factory).run()
    
            
        
        
        
            
            
        
        
            
    
















