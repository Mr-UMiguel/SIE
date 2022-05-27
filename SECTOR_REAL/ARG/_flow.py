from SECTOR_REAL.flow import Extract, Transform, Load
from SECTOR_REAL.renameFiles import *
from SECTOR_REAL.ARG.extract import _1_01_1, _1_17_1
from SECTOR_REAL.ARG.load import upload

from prefect import Flow, Parameter
import json



flow = Flow("testing-example")

#### 1_01_1
e_1011 = Extract(_1_01_1,download_path="D:/Desktop")
t_1011 = Transform(rename_and_save,flar_name="1_01_1.xlsx",download_path="D:/Desktop")

flow.add_edge(upstream_task=e_1011,downstream_task=t_1011, key="PIB")

### 1_17_1
e_1171 = Extract(_1_17_1,download_path="D:/Desktop")

flow.add_task(e_1171)

flow.register(project_name="prueba-clases")
