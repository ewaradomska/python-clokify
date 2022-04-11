import requests
import json
from datetime import date

s = requests.Session()
s.headers = {"X-Api-Key": "MDU3YmYxZDYtYjVhZC00N2VjLThmOGUtNGUxNGMyNmEzZmQ2"}
request_exception = requests.RequestException
connection_exception = requests.ConnectionError
http_error = requests.HTTPError


def get_user_data():
    try:
        user = s.get("https://api.clockify.me/api/v1/user")
    except [request_exception, connection_exception, http_error]:
        return
    return json.loads(user.text)


def get_user_projects(user_workspace):
    try:
        projects = s.get(f"https://api.clockify.me/api/v1/workspaces/{user_workspace}/projects")
    except [request_exception, connection_exception, http_error]:
        return
    return json.loads(projects.text)


def get_time_records(project_id, user_id, workspace):
    year = date.today().year
    try:
        time_records = s.get(f"https://api.clockify.me/api/v1/workspaces/{workspace}/user/{user_id}/time-entries?start={year}-01-01T00:00:00.00Z&end={year}-12-31T00:00:00.00Z&project={project_id}")
    except [request_exception, connection_exception, http_error]:
        return
    return json.loads(time_records.text)


def get_paid_time_off_task_id(workspace, project_id):
    try:
        tasks = s.get(f"https://api.clockify.me/api/v1/workspaces/{workspace}/projects/{project_id}/tasks")
        json_tasks = json.loads(tasks.text)
        for task in json_tasks:
            if task['name'] == "Paid TimeOff":
                return task['id']
    except [request_exception, connection_exception, http_error]:
        return
