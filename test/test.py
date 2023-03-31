from ansible.module_utils.basic import AnsibleModule
import json
import requests


tower_base_url = "http://172.168.0.212"
tower_username = "admin"
tower_password = "isecurepassword"
tower_job_id = "5"

url = f"/api/v2/jobs/{tower_job_id}/stdout/?format=txt_download"
responses = []
hosts = {}

response = requests.get(tower_base_url + url, auth=requests.auth.HTTPBasicAuth(tower_username, tower_password), verify=False)

