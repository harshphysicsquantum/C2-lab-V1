import executor 
def process_task(task):
    task_id = task[0]
    task_type = task[1]
    result = executor.execute_task(task_type)
    return task_id, result