#!/bin/bash
if [ $1 = 'start' ]; then
    flag=0
    retries=0
    max_retries=2
    sleep_time=3
    while [ $flag -eq 0 ]; do
        if [ $retries -eq $max_retries ]; then
            echo Executed $retries retries, aborting
            exit 1
        fi
        sleep $sleep_time
        exec python ./{{ cookiecutter.project_slug }}/run_uvicorn.py --env PYTHONUNBUFFERED=1

        if [ $? -eq 0 ]; then
            flag=1
        else
            echo "Cannot start application, retying in $sleep_time seconds..."
            let retries++
        fi
    done
fi
