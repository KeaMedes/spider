# -*- coding: utf-8 -*-
from website_conf import website_config
class Scheduler(object):
    def __init__(self):
        pending_queue = []
        retry_queue = []
        last_visit_time = {}

        self._pending_queue = pending_queue
        self._retry_queue = retry_queue
        self._last_visit_time = last_visit_time

    def init_task(self, task):
        self._pending_queue.append(task)

    def _is_netloc_interval_satisfied(self, task):
        netloc = task.url.netloc
        netloc_interval = website_config.interval(netloc)
        if netloc not in self._last_visit_time:
            return True
        else:
            from time import time
            current_time = int(round(time() * 1000))
            if netloc_interval + self._last_visit_time[netloc] <= current_time:
                return True
            else:
                return False

    def schedule(self):
        from time import time
        from executor import executor
        current_time = int(round(time() * 1000))
        _is_task_interval_satisfied = lambda task: \
            task.create_time + task.delay <= current_time

        next_tasks = [t for t in self._pending_queue if \
                      _is_task_interval_satisfied(t) and \
                      self._is_netloc_interval_satisfied(t)]

        if not next_tasks:
            next_tasks = [t for t in self._retry_queue if \
                          _is_task_interval_satisfied(t) and \
                          self._is_netloc_interval_satisfied(t)]

        if not next_tasks:
            print("Finish all tasks")

        next_task = max(next_tasks, key=lambda t: t.priority)

        executor.execute(next_task)

        if next_task.status ==
