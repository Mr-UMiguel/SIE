from SECTOR_REAL.flow import Extract, Transform, Load
from SECTOR_REAL.scheduler import *
from SECTOR_REAL.renameFiles import *
from SECTOR_REAL.ARG.extract import _1_01_1, _1_17_1


from prefect import Flow, Parameter
import json

### Flow 1_01_1
with Flow("1_01_1") as flow:
    e = Extract(function=_1_01_1,download_path = "D:/Desktop/prueba-clases")
    t = Transform(
        function=rename_and_save,
        file_name = e,
        flar_name="1_01_1.xlsx",
        download_path="D:/Desktop/prueba-clases",
        file_macro="D:/Desktop/prueba-clases/1.01.1.xlsm",
        refAreaID = "AR",
        flarID = "1.01.1")

    # l = Load(rango=t)


flow.run()
# flow.schedule =  monthCron_scheduler()
# flow.register(project_name="prueba-clases")


# ### Floq 1_11_1
# with Flow("1_11_1") as flow:
#     e = Extract()

