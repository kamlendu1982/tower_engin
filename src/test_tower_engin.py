#!/usr/bin/env python3
import json

import src.AnsibleTower as AnsibleTower
import src.OrchAnsibleTower as OrchAnsibleTower
import sys
import src.configuration_tower as configuration

def test():
        """
        Runs an End-to-End test against an Ansible Automation Controller instance
        """
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

        configuration.logging.info(json.dumps(payload_create_template, indent = 4, sort_keys=True))
        mytower = AnsibleTower.AnsibleTower('https://controller.example.com/')
        mytowerUtils = OrchAnsibleTower.OrchAnsibleTower()

        configuration.logging.info(mytower.create_job_template(payload_create_template))
        configuration.logging.info(mytower.modify_job_template(payload_create_template, 11))
