query1 = """
SELECT 
run_date,
run_duration,
((run_duration/10000*3600 + (run_duration/100)%100*60 + run_duration%100 + 31 ) / 60) as 'run_duration_minutes',
run_status
From msdb.dbo.sysjobhistory as jh
LEFT JOIN msdb.dbo.sysjobs as j on j.job_id = jh.job_id
WHERE j.name = 'JobIndicadoresSIE'
"""

query2 = """
SELECT 
start_execution_date,
stop_execution_date
From msdb.dbo.sysjobactivity as ja
INNER JOIN msdb.dbo.sysjobs as j on j.job_id = ja.job_id
WHERE j.name = 'JobIndicadoresSIE'
AND start_execution_date IS NOT NULL
"""

query3 = """
SELECT * FROM [SIEDB].[dbo].[audit]
ORDER BY code DESC
"""