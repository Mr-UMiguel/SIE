from prefect import Task, Flow, Parameter, task
from prefect.engine.flow_runner import FlowRunner
from prefect.executors import LocalExecutor
import json

class Extract(Task):

    def __init__(self,function,*args,**kargs):
        self.function = function
        self.download_path = kargs['download_path']
        super().__init__()

    def run(self):
        r = self.function(download_path=self.download_path)
        with open('./test-serie.json','r+') as f:
            data = json.load(f)
            data['file_name'] = r
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()
        
        

class Transform(Task):

    def __init__(self,function,*args,**kargs):
        self.function = function
        self.flar_name = kargs['flar_name']
        self.download_path = kargs['download_path']

        super().__init__()

    def run(self):
        self.fname = json.load(open('./test-serie.json','r'))['file_name']
        r = self.function(self.fname,self.flar_name,self.download_path)
        return r

class Load(Task):
    def __init__(self,function,*args,**kargs):
        self.function = function
        self.state = kargs['state']
        super().__init__()
    
    def run(self):
        r = self.function(self.state)
        return r









