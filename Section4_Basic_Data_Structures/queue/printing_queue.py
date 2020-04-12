# Standard library imports
import random

# Local application imports
from queue1 import Queue1


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time, pages):
        self.pages = pages
        self.timestamp = time

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


def simulation(num_seconds, pages_per_minute, num_students, avg_pages):
    """ Printing simulation """

    # Set up
    printer = Printer(pages_per_minute)
    print_queue = Queue1()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(num_students):
            pages = random.randrange(1, avg_pages + 1)
            task = Task(current_second, pages)
            print_queue.enqueue(task)

        if (not printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            printer.start_next(nexttask)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        "Average wait {} secs {} tasks remaining.".format(
            average_wait, print_queue.size()
        )
    )


def new_print_task(num_students):
    """Generate a print task"""
    # Seconds per task
    seconds_per_task = 1800 // num_students

    num = random.randrange(1, seconds_per_task + 1)
    if num == seconds_per_task:
        return True
    else:
        return False


def main():
    for _ in range(10):
        simulation(3600, 10, 10, 20)


if __name__ == "__main__":
    main()
