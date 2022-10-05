#!/usr/bin/python
#####################################################################################################
## OrchAnsibleTower.py 
## author: Kamlendu Shekhar(kashekha@redhat.com)
#####################################################################################################

import json
import src.AnsibleTower
import src.configuration_tower as configuration

ANSIBLE_TOWER_INSTANCE = configuration.ANSIBLE_TOWER_INSTANCE

#class UtilsAnsibleTower():
class OrchAnsibleTower():
    def __init__(self):
        self.tower  = AnsibleTower(ANSIBLE_TOWER_INSTANCE)

    def get_id_template(self, templatename):
        list_job_templates = json.loads(self.tower.list_job_template())
        templateid = 'NULL'
        count_templates = list_job_templates['count']
        for count in range(0, count_templates):
            template_metadata = list_job_templates['results'][count]
            if templatename.strip() == template_metadata['name'].strip():
                templateid = template_metadata['id']
        return templateid

    def get_id_inventory(self, inventoryname):
        list_inventories = json.loads(self.tower.list_inventories())
        inventoryid = 'NULL'
        count_inventories = list_inventories['count']
        for count in range(0, count_inventories):
            inv_metadata = list_inventories['results'][count]
            if inventoryname.strip() == inv_metadata['name'].strip():
                inventoryid = inv_metadata['id']
        return(inventoryid) 

    def get_id_project(self, projectname):
        projectid = 'NULL'
        list_projects = json.loads(self.tower.list_projects())
        count_projects = list_projects['count']
        for count in range(0, count_projects):
            project_metadata = list_projects['results'][count]
            if projectname.strip() == project_metadata['name'].strip():
                projectid = project_metadata['id']
        return(projectid) 

    def get_id_credential(self, credentialname):
        credentialid = 'NULL'
        list_credentials = json.loads(self.tower.list_credentials())
        count_credentials = list_credentials['count']
        for count in range(0, count_credentials):
            credential_metadata = list_credentials['results'][count]
            if credentialname.strip() == credential_metadata['name'].strip():
                credentialid = credential_metadata['id']
        return(credentialid) 
    def set_credential_template_by_name(self, credentialname, templatename):
        templateid = self.get_id_template(templatename)
        credentialid = self.get_id_credential(credentialname)
        return self.tower.set_credential_template(credentialid, templateid)

    def get_template_by_name(self, templatename):
        templateid = self.get_id_template(templatename)
        return(self.tower.get_job_template(templateid))

    def run_template_by_name(self, templatename, params_run_template = {}):
        templateid = self.get_id_template(templatename)
        return(self.tower.run_job_template(templateid, params_run_template))
        
    def modify_job_template_by_name(self, payload, templatename):
        templateid = self.get_id_template(templatename)
        return(self.tower.modify_job_template(payload, templateid))
        




