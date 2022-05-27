# from SECTOR_REAL.flow import Extract, Transform, Load
# from SECTOR_REAL.ARG.extract import _1_01_1
# from SECTOR_REAL.ARG.transform import saludo
# from SECTOR_REAL.ARG.load import upload

# from prefect import Flow

# e = Extract(_1_01_1,download_path="OK")
# t = Transform(saludo,rename_files = e)
# l = Load(upload, state=t)

# flow = Flow("testing-example")
# flow.add_edge(upstream_task=e,downstream_task=t)
# flow.add_edge(upstream_task=t,downstream_task=l)


# state = flow.register(project_name="prueba-clases")

# state = flow.run()

# print(state.result[t].result)
# print(state.result[t].is_successful())