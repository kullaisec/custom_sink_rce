from engine import TaskEngine

def process_task(task_name):
    engine = TaskEngine()
    return engine.execute(task_name)
