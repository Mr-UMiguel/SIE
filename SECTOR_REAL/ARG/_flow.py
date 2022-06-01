from SECTOR_REAL.flow import Extract, Transform, Load
from SECTOR_REAL.scheduler import monthCron_scheduler
from SECTOR_REAL.renameFiles import rename_and_save
from SECTOR_REAL.ARG.extract import _1_01_1, _1_17_1
from prefect import Flow, Parameter

extract_path = Parameter('extract_path', default = "D:/Desktop/prueba-clases")
load_path = Parameter('load_path', default = "D:/Desktop/prueba-clases")

### Flow 1_01_1
with Flow("1_01_1") as flow:
    e = Extract(function=_1_01_1,download_path = extract_path)
    t = Transform(
        function=rename_and_save,
        file_name = e,
        flar_name="1_01_1.xlsx",
        download_path="D:/Desktop/prueba-clases",
        file_macro= load_path+'/1.01.1.xlsm',
        refAreaID = 'AR',
        flarID = '1.01.1',
        )
    l = Load(
        update_state=t,
        refAreaID = 'AR',
        flarID = '1.01.1',
        )

flow.schedule = monthCron_scheduler()
flow.register(project_name='AR')

