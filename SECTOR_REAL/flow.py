from datetime import timedelta 
from prefect import task, Flow, Parameter 

from SECTOR_REAL.load import upload

@task(log_stdout=True)
def load():
    upload()


with Flow("Load Database 1.01.1") as flow:
    load()

flow.register(project_name="FLAR prueba")
# flow.run()
