# AWX Log Keeper

## Scope
The aim of this project is to use ans ansible role to export AWX logs on disk.

## Parameters
The variables used are described in the `playbooks/vars/awx_logs_keeper_vars.yml` as follows:

```yml
---
log_path_root: "/foo/bar/awx_logs"
awx:
  tower_base_url: "https://awx.prod.mytest.ch"
  tower_username: "{{ awx_username }}"
  tower_password: "{{ awx_password }}"
 job_id_interval:
   start: 2
   end: 5
date_interval:
  start: "2022-10-20T10:00:00"
  end: "2022-10-20T13:00:00"
```

- `log_pat_root`: Is the path where the logs will be saved
- `awx` section is used for awx credentials and web sevrver address
- `job_id_interval` 
   - instruct the playbook to get logs got all jobs from `job_id_interval.start` and `job_id_interval.end`.
   - optional 
- `date_interval` 
   - instruct the playbook to get logs got all jobs between `date_interval.start` date and `date_interval.end` date.
   - optional 


**Note**: 
> - `date_interval.start` must be lower than `date_interval.end`. 
> - `job_id_interval.start` must be lower than `job_id_interval.end`. 
> - Values of `job_id_interval` and `date_interval` are **not** mutual exclusive, but at least **one** of `date_interval` or `job_id-interval` must be given.

The playbook will test first if `date_interval` make sense, then it gets all `job_id` between these two dates. At the end it will add the `job_id_interval`, and get all logs for the obtained `job_id` list.

The output is written in `log_path_root/date_of_job_execution/job_id`. Two files are saved :
- `output_<job_id>_<DDMMYYY_HHMISS>.log` is the ansible output of the log.
- `<job_id>_<DDMMYYY_HHMISS>.json` is the json description of the job.

## Example:
```bash
# Execute the playbook by surcharging the devault value of log_path_root
$>  ansible-playbook playbooks/awx_logs_keeper_vars.yml -e "log_path_root=/tmp/awx_logs" --vault-password-file playbooks/vars/vault-pass

....
TASK [awx_get_one_log : Out the logfile path] **********************************************************************************************************
ok: [localhost] => {
    "msg": "Write Log for job id 324299 to /tmp/awx_logs/20-10-2022/324299"
}
....

$> cd /tmp/awx_logs/20-10-2022/324299
$> ls
324299_20102022_111602.json   output_324299_20102022_111602.log

```

**Note**: 
> In the example the `--vault-password-file playbooks/vars/vault-pass` is given to shaddow the Ansible Tower access credentials.  
```yml
......
gather_facts: true
  vars_files:
    - vars/secret.yml
    - vars/awx_logs_keeper_vars.yml
...
```
```
Shadowed parameters are: 
* `awx_password`
* `awx_password`
