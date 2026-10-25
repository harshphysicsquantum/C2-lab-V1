import database
import agent
database.init_db()


while True:
    print("==============================")
    print("       C2-Lab Console")
    print("==============================")
    print("1. Add a task")
    print("2. View pending tasks")
    print("3. Process next task")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if (choice == '1'):
        print("Adding a new task....")
        task = input("Enter task type: ")
        task_id = database.add_task(task)
        print(f"Task ID: {task_id}")

    elif choice == '2':
        print("Viewing pending tasks....")
        pending_task = database.get_pending_tasks()

        if not pending_task:
            print("No pending tasks.")
        else:
            for task in pending_task:
                print(f"Task ID: {task[0]} | Type: {task[1]} | Status: {task[2]} | Created: {task[3]}")

    
    elif choice == '3':
        print("Processing next task")
        next_pending_task = database.get_next_pending_task()

        if not next_pending_task:
            print("No pending tasks.")
        else:
            print(f"Task ID: {next_pending_task[0]} | Type: {next_pending_task[1]} | Status: {next_pending_task[2]} | Created: {next_pending_task[3]}")

            database.update_task_status(next_pending_task[0], "running")

            try:
                task_id, result = agent.process_task(next_pending_task)
                if result is not None:
                    print("Task result:", result)
                    database.update_task_status(task_id, "completed")
                else:
                    print("Task failed")
                    database.update_task_status(task_id, "failed")
                
            except Exception as e:
                print(f"something went wrong: {e}")
                database.update_task_status(next_pending_task[0], "failed")
                
    elif choice == '4':
        print("Exiting the C2-lab")
        break

    else:
        print("Invalid choice")