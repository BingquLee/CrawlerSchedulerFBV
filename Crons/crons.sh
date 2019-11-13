#!/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/local/bin:/usr/sbin

 

step=10

for (( i = 0; i < 60; i=(i+step) )); do
cd /home/BingquLee/Project/CrawlerSchedulerFBV; /home/BingquLee/anaconda3/envs/env_p3/bin/python /home/BingquLee/Project/CrawlerSchedulerFBV/Crons/AddFileToDb.py >>  /home/BingquLee/Project/CrawlerSchedulerFBV/Crons/logs/add_file_to_db.log
cd /home/BingquLee/Project/CrawlerSchedulerFBV; /home/BingquLee/anaconda3/envs/env_p3/bin/python /home/BingquLee/Project/CrawlerSchedulerFBV/Crons/GetJobs.py >> /home/BingquLee/Project/CrawlerSchedulerFBV/Crons/logs/get_jobs.log

sleep $step

done

exit 0
