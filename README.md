# Ansible Automation Platform - API Python Project


## What is?
Example to create/modify/delete/read Ansible tower objects(like template, jobs, credentials etc)

test_tower_engin.py uses the class and takes parameters from json object. Sample json object.
ExecuteIntegration.py: Executes jobs in json payload

## How run?

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -e . # editable mode
aap-e2e # runs the `test_tower_engin` application
```
