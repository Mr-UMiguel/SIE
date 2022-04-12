from datetime import timedelta 
from prefect import task, Flow, Parameter 

from ARG.flow import argFlow
from BOL.flow import bolFlow
from BRA.flow import braFlow 
from CHL.flow import chlFlow
from COL.flow import colFlow
from CRI.flow import criFlow
from DOM.flow import domFlow
from ECU.flow import ecuFlow
from GTM.flow import gtmFlow
from HND.flow import hndFlow
from MEX.flow import mexFlow
from NIC.flow import nicFlow
from PAN.flow import panFlow
from PER.flow import perFlow
from PRY.flow import pryFlow
from SLV.flow import slvFlow
from URY.flow import uryFlow



with Flow("Real Sector Update") as flow:
    pass
    argFlow()
    bolFlow()
    braFlow()
    chlFlow()
    # colFlow()
    # criFlow()
    # domFlow()
    # ecuFlow()
    # gtmFlow()
    # hndFlow()
    # mexFlow()
    # nicFlow()
    # panFlow()
    # perFlow()
    # pryFlow()
    slvFlow()
    # uryFlow()

flow.register(project_name="FLAR prueba")