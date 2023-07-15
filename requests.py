from models import db, task

def active_tasks_list():
    tasks_query = task.TaskModel.query.all()
    my_list = []
    for x in tasks_query:
        
        # Only activated tasks will return
        if (x.status == 1):
            my_list.append(x.__str__())

    return my_list

def add_task(new_task):
    new_task_query = task.TaskModel(creator=new_task['name'], task=new_task['body'])
    print(new_task_query.__str__())
    db.session.add(new_task_query)
    db.session.commit()
    return new_task
    