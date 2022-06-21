from prefect import Flow, Parameter
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run
from prefect.executors import LocalDaskExecutor



with Flow('AR-ORQUESTADOR',
            executor = LocalDaskExecutor()
            ) as flow:

    flow_1011 = create_flow_run(flow_name='1_01_1', project_name='AR')
    wait_for_flow_1011 = wait_for_flow_run(flow_1011, raise_final_state=False)

    flow_1171 = create_flow_run(flow_name='1_17_1', project_name='AR')
    wait_for_flow_1171 = wait_for_flow_run(flow_1171, raise_final_state=False)

    flow_1171.set_upstream(wait_for_flow_1011)

flow.register(project_name='AR')