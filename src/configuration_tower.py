import os
import logging

logging.basicConfig(level=logging.NOTSET)
ANSIBLE_TOWER_INSTANCE = 'https://controller.example.com/'
INTEGRATION_TEST_PAYLOAD = '/home/kashekha/projects/adp/git_repo/tower_engin/payload_integration_test.json'

JOB_CHECK_INTERVAL = 2
JOB_RUN_TIMEOUT = 4 
