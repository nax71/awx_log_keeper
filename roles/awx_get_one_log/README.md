Role Name
=========

Save the ansible log from AWX for a given log_id.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

log_path_root: The path where the logs will be saved: log_path_root/DD-MM-YYYY/job_id/output_... and the json jjob description 

Awx specific information:                                    
awx.tower_base_url: "https://awx.prod.com" 
awx.tower_username: awx_username
awx.tower_password: awx_password
