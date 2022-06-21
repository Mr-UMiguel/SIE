import datetime
from prefect.schedules import clocks, Schedule
from prefect.schedules.clocks import CronClock


def monthCron_scheduler():
    # on schedule format online
    # en este caso la primera posición son minutos: 0
    # la segunda posición es la hora: 12
    # La tercera pisición el día del mes: 20,30 = 20 y 30
    # La cuarta los meses: * = todos
    # La quita el día de la semana: * = todos
    # Así los flujos se ejecutan todos los 20 y 30 de cada mes
    clock1 = CronClock("0 12 20,30 * *")

    # the full schedule
    schedule = Schedule(clocks=[clock1])

    return schedule


def weeklyCron_scheduler():
    # on schedule format online
    # en este caso la primera posición son minutos: 0
    # la segunda posición es la hora: 12
    # La tercera pisición el día del mes: * = todos
    # La cuarta los meses: * = todos
    # La quita el día de la semana: 4 = jueves
    # Así los flujos se ejecutan todos los jueves de cada mes
    clock1 = CronClock("0 12 * * 4")

    # the full schedule
    schedule = Schedule(clocks=[clock1])

    return schedule