from datetime import timedelta 
from prefect import task, Flow, Parameter 

from ARG.flow import argFlow


with Flow("Update real sector") as flow:
    argFlow()