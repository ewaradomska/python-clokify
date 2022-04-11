import requests
import json
from datetime import date


def get_user_data():
    user = requests.get("https://api.clockify.me/api/v1/user",
                        headers={"X-Api-Key": "MDU3YmYxZDYtYjVhZC00N2VjLThmOGUtNGUxNGMyNmEzZmQ2"})
    return json.loads(user.text)


def get_user_projects(user_workspace):
    projects = requests.get("https://api.clockify.me/api/v1/workspaces/{user_workspace}/projects",
                            headers={"X-Api-Key": "MDU3YmYxZDYtYjVhZC00N2VjLThmOGUtNGUxNGMyNmEzZmQ2"})
    return json.loads(projects.text)


def get_time_records(project_id, user_id, workspace):
    year = date.today().year
    time_records = requests.get("https://api.clockify.me/api/v1/workspaces/{workspace}/user/{user_id}/time-entries?start={year}-01-01T00:00:00.00Z&end={year}-12-31T00:00:00.00Z&project={project_id}",
                                headers={"X-Api-Key": "MDU3YmYxZDYtYjVhZC00N2VjLThmOGUtNGUxNGMyNmEzZmQ2"})
    return json.loads(time_records.text)


def get_paid_time_off_task_id(workspace, project_id):
    tasks = requests.get("https://api.clockify.me/api/v1/workspaces/{workspace}/projects/{project_id}/tasks",
                         headers={"X-Api-Key": "MDU3YmYxZDYtYjVhZC00N2VjLThmOGUtNGUxNGMyNmEzZmQ2"})
    json_tasks = json.loads(tasks.text)
    for task in json_tasks:
        if task['name'] == "Paid TimeOff":
            return task['id']
