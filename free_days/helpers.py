def get_user_id(user_data):
    return user_data['id']


def get_user_workspace(user_data):
    return user_data['activeWorkspace']


def get_free_time_id(projects):
    for project in projects:
        if project['name'] == "TimeOff":
            return project['id']


def count_free_days_left(time_records_list, paid_time_of_id):
    days_free_in_year = 20
    for record in time_records_list:
        if record['taskId'] == paid_time_of_id:
            days_free_in_year = days_free_in_year - 1
    return days_free_in_year
