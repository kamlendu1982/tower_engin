#!/usr/bin/python
import json

from AnsibleTower import *
#from UtilsAnsibleTower import *
from OrchAnsibleTower import *

#from rest_framework.parsers import JSONParser,ParseError

payload_create_template = {
         "name":"TestSample ADP",
         "description":"setup apache on Dev webservers",
         "job_type":"run",
         "inventory":1,
	 "credentials":2,
         "project":8,
         "playbook":"apache-setup.yml",
         "forks":0,
         "limit":"",
         "verbosity":0,
         "extra_vars": "{\"extra_var2\": \"test4\", \"extra_var3\": \"test5\"}",
         "job_tags":"",
         "force_handlers":"false",
         "skip_tags":"",
         "start_at_task":"",
         "timeout":0,
         "use_fact_cache":"false",
         "status":"successful",
         "host_config_key":"",
         "ask_scm_branch_on_launch":"false",
         "ask_diff_mode_on_launch":"false",
         "ask_variables_on_launch":"false",
         "ask_limit_on_launch":"false",
         "ask_tags_on_launch":False,
         "ask_skip_tags_on_launch":False,
         "ask_job_type_on_launch":False,
         "ask_verbosity_on_launch":False,
         "ask_inventory_on_launch":False,
         "ask_credential_on_launch":False,
         "survey_enabled":False,
         "become_enabled":False,
         "diff_mode":False,
         "allow_simultaneous":False,
         "job_slice_count":1,
         "webhook_service":""
}

payload_extravars_template = {
        "extra_vars": {
            "extra_var2": "test2",
            "extra_var1": "test1"
            }
        }

payload_create_project = {
        "allow_override": True,
        "name": "fooo",
        "organization": 1,
        "scm_type": "git",
        "scm_url": "https://github.com/ansible/test-playbooks.git"
        }

print(json.dumps(payload_create_template, indent = 4, sort_keys=True))
mytower = AnsibleTower('https://controller.lab.example.com/')
mytowerUtils = OrchAnsibleTower()
#print(mytowerUtils.get_id_template('TestSample ADP'))
#print(mytowerUtils.run_template_by_name('TestSample ADP'))
#print(mytowerUtils.get_id_inventory('Dev'))
#print(mytowerUtils.get_id_project('SampleADP-1'))
#print(mytowerUtils.get_id_credential('testOps'))
#print(mytowerUtils.set_credential_template_by_name('testOps', 'TestSample ADP'))
#print(mytowerUtils.get_template_by_name('TestSample ADP'))
#print(mytowerUtils.run_template_by_name('TestSample ADP', params_run_template=payload_extravars_template))
#print(mytowerUtils.modify_job_template_by_name(payload_create_template, 'TestSample ADP'))

#print(mytower.create_project(payload_create_project))
print(mytower.create_job_template(payload_create_template))
print(mytower.modify_job_template(payload_create_template, 11))
#print(mytower.set_credential_template(5, 14))
#print(mytower.list_inventories())
#print(mytower.list_job_template())
#print(mytower.run_job_template(10))
#print(mytower.delete_job_template('TestSample ADP'))
#print(mytower.get_job_status(21))