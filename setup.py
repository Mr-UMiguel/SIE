from setuptools import setup

setup(
    name="ETLFLAR",
    version="1.1",
    description="""
    ETL-FLAR
    Es un paquete diseñado para el proceso de extracción, transformación y cargar
    del Sistema de Información Económica del Fondo Lationamericano de Reservas
    """,
    author="Miguel",
    author_email="",
    url="",
    packages= ["SECTOR_REAL",
               "SECTOR_REAL.ARG",
               "SECTOR_REAL.BOL",
               "SECTOR_REAL.BRA",
               "SECTOR_REAL.CHL",
               "SECTOR_REAL.COL"]
)