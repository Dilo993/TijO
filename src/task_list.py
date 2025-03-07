class TaskList:

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def tasks(self):
        return self._tasks