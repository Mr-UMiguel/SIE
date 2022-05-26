from prefect import Task, Flow, Parameter
from prefect.engine.flow_runner import FlowRunner
from prefect.executors import LocalExecutor

from ARG.transform import *
class Extract(Task):

    def __init__(self,function,*args,**kargs):
        self.function = function
        super().__init__()

    def run(self):
        r = self.function()
        return r


class Transform(Task):

    def __init__(self,extract,*args,**kargs):
        self.__extract = extract
        super().__init__()

    def run(self):
        flow = Flow("Extract ARG")
        e = Extract(saludo)
        flow.add_task(e)
        state = flow.run()

        r = state.result[e].result
        return r + " OK"




flow = Flow("testing-example")

e = Extract(saludo)
t = Transform(e)
flow.add_edge(upstream_task=e, downstream_task=t)

state = flow.run()
print(state.result[t].result)
print(state.result[t].is_successful())



