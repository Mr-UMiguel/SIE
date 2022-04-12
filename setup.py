from setuptools import setup

setup(
    name="ETLFLAR",
    version="1.3",
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
    "SECTOR_REAL.COL",
    "SECTOR_REAL.CRI",
    "SECTOR_REAL.DOM",
    "SECTOR_REAL.ECU",
    "SECTOR_REAL.GTM",
    "SECTOR_REAL.HND",
    "SECTOR_REAL.MEX",
    "SECTOR_REAL.NIC",
    "SECTOR_REAL.PAN",
    "SECTOR_REAL.PER",
    "SECTOR_REAL.PRY",
    "SECTOR_REAL.SLV",
    "SECTOR_REAL.URY"]
)