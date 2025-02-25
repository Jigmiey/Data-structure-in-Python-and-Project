from model import Queue,Stack,Task

class task_service:
    def __init__(self):
        self.tasks=[]
        self.task_queue = Queue.Queue()
        self.task_history = Stack.Stack()
    def create_task(self,id,title,description):
        task = Task.Task(id,title,description)
        self.task_queue.enqueue(task)
        self.tasks.append(task)
        return task
    def complete_task(self):
        if not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            self.task_history.push(task)
            return (task.id, task.title, task.description)
        return None
    def get_task_history(self):
        return self.task_history
        