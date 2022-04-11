import repository
import helpers
import info_model
from datetime import date

def main():
    user_data = repository.get_user_data()
    workspace = helpers.get_user_workspace(user_data)
    user_id = helpers.get_user_id(user_data)
    projects = repository.get_user_projects(workspace)
    proj_id = helpers.get_free_time_id(projects)
    time_records = repository.get_time_records(proj_id, user_id, workspace)
    paid_time_task_id = repository.get_paid_time_off_task_id(workspace, proj_id)
    days = helpers.count_free_days_left(time_records, paid_time_task_id)
    year = date.today().year
    print(info_model.create_info_about_free_days(days, year))


main()
