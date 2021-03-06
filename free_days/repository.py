import requests
import json
from consts import *
from datetime import date

s = requests.Session()
s.headers = API_KEY
request_exception = requests.RequestException
connection_exception = requests.ConnectionError
http_error = requests.HTTPError


def get_user_data():
    try:
        user = s.get(BASE_URL + "/user")
    except [request_exception, connection_exception, http_error]:
        return
    return json.loads(user.text)


def get_user_projects(user_workspace):
    try:
        projects = s.get(BASE_URL + f"/workspaces/{user_workspace}/projects")
    except [request_exception, connection_exception, http_error]:
        return

    return json.loads(projects.text)


def get_time_records(project_id, user_id, workspace):
    year = date.today().year
    try:
        time_records = s.get(BASE_URL + f"/workspaces/{workspace}/user/{user_id}/time-entries?start={year}-01-01T00:00:00.00Z&end={year}-12-31T00:00:00.00Z&project={project_id}")
    except [request_exception, connection_exception, http_error]:
        return

    return json.loads(time_records.text)


def get_paid_time_off_task_id(workspace, project_id):
    try:
        tasks = s.get(BASE_URL + f"/workspaces/{workspace}/projects/{project_id}/tasks")
        json_tasks = json.loads(tasks.text)
        for task in json_tasks:
            if task['name'] == TIME_PAIDOFF_PROJECT:
                return task['id']
    except [request_exception, connection_exception, http_error]:
        return

