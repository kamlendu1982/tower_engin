#!/usr/bin/python
#####################################################################################################
## AnsibleTower.py 
## author: Kamlendu Shekhar(kashekha@redhat.com)
#####################################################################################################

import requests
from requests.auth import HTTPBasicAuth
import json
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class AnsibleTower():
    def __init__(self, url_tower):
        self.tower_username = "admin"
        self.tower_password = "root123"
        self.url_tower      = url_tower
        self.headers        = {'Content-Type':'application/json'}

    def create_execuion_environment(self, payload_ee_template, url_string='api/v2/execution_environments/'):
        url = self.url_tower + url_string
        response = requests.post(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=payload_ee_template, verify=False)
        return response.text

    def modify_job_template(self, params_modify_template, templateid, url_string='api/v2/job_templates/'):
        url = self.url_tower + url_string + str(templateid) + '/'
        response = requests.patch(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=params_modify_template, verify=False)
        return response.text

    def create_job_template(self, params_create_template, url_string='api/v2/job_templates/'):
        url = self.url_tower + url_string
        response = requests.post(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=params_create_template, verify=False)
        return response.text

    def delete_job_template(self, templateid):
        url = self.url_tower + 'api/v2/job_templates/{templateid}/'.format(templateid=templateid)
        response = requests.delete(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        return response.json

    def get_job_template(self, templateid):
        url = self.url_tower + 'api/v2/job_templates/{templateid}/'.format(templateid=templateid)
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    def list_job_template(self, url_string='api/v2/job_templates/'):
        url = self.url_tower + url_string
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    def run_job_template(self, templateid, params_run_template = {},url_string='api/v2/job_templates/'):
        url = self.url_tower + url_string + str(templateid) + '/launch/'
        response = requests.post(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=params_run_template, verify=False)
        return response.text

    def list_inventories(self, url_string='api/v2/inventories/'):
        url = self.url_tower + url_string 
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        return response.text
        
    def list_projects(self, url_string='api/v2/projects/'):
        url = self.url_tower + url_string 
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        return response.text
        
    def create_project(self, data, url_string='api/v2/projects/'):
        url = self.url_tower + url_string 
        response = requests.post(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=data, verify=False)
        return response.text
        
    def list_credentials(self, url_string='api/v2/credentials/'):
        url = self.url_tower + url_string
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        return response.text
        
    def set_credential_template(self, credentialid, templateid, url_string='api/v2/job_templates/'):
        url = self.url_tower + url_string + str(templateid) + "/credentials/"
        data = {
                'id':credentialid
                }
        response = requests.post(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, json=data, verify=False)
        return response.text
        
    def pull_job_summary(self, jobid, url_string='api/v2/jobs/'):
        url = self.url_tower + url_string + str(jobid) + '/'
        response = requests.get(url, auth=HTTPBasicAuth(self.tower_username, self.tower_password), headers=self.headers, verify=False)
        return response.text

    def get_job_status(self, jobid):
        job_sum = json.loads(self.pull_job_summary(jobid))
        return job_sum['status']
        


