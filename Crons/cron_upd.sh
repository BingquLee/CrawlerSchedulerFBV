#!/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/local/bin:/usr/sbin

cd /home/BingquLee/Project/CrawlerSchedulerFBV
/home/BingquLee/anaconda3/envs/env_p3/bin/python Crons/UpdatePublishDate.py >> Crons/logs/upd.log

