#!/usr/bin/python
#####################################################################################################
## ExecuteIntegration.py 
## author: Kamlendu Shekhar(kashekha@redhat.com)
#####################################################################################################

import json
import sys
from OrchAnsibleTower import *
from AnsibleTower import *
import time

import configuration_tower as configuration
mytowerOrch = OrchAnsibleTower()
mytower = AnsibleTower(configuration.ANSIBLE_TOWER_INSTANCE)

payload_file_path = configuration.INTEGRATION_TEST_PAYLOAD

def check_status_job_priodically(jobid):
    timeout_val = configuration.JOB_RUN_TIMEOUT
    sleeptime = configuration.JOB_CHECK_INTERVAL
    max_count = int(timeout_val/sleeptime)
    count = 0
    result_monitor = {}
    result_monitor['status'] = 'timeout'
    while count < max_count:
        status = str(mytower.get_job_status(jobid))
        time.sleep(sleeptime)
        if status == 'successful' or status == 'failed':
            result_monitor['status'] = status
            break
        count += 1
    return result_monitor['status']

def execute_all(payload_data):
    result_run = {}
    for payload in payload_data['payload_survey_templates']:
        survey_data = {}
        job_template_name = payload['name']
        survey_data["extra_vars"] = payload['extra_vars']
        configuration.logging.info("Executing Template " + job_template_name + "=============")
        resp = json.loads(mytowerOrch.run_template_by_name(job_template_name, params_run_template=survey_data))
        jobid = resp['job']
        result_job = check_status_job_priodically(jobid)
        result_run[jobid] = result_job
    return(result_run)


def main():
    with open(payload_file_path) as payload_file:
        payload_data = json.loads(payload_file.read())
    configuration.logging.info(execute_all(payload_data))
    payload_file.close()

if __name__ == "__main__":
    main()


