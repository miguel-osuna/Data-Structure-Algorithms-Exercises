from queue import Queue
import random


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

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time, pages):
        self.pages = pages
        self.timestamp = time

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute, numStudents, averagePages):

    # Set up
    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask(numStudents):
            pages = random.randrange(1, averagePages + 1)
            task = Task(currentSecond, pages)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingTimes.append(nexttask.waitTime(currentSecond))
            printer.startNext(nexttask)

        printer.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print(
        "Average wait {} secs {} tasks remaining.".format(
            averageWait, printQueue.size()
        )
    )


def newPrintTask(numStudents):
    # Seconds per task
    secondsPerTask = 1800 // numStudents

    num = random.randrange(1, secondsPerTask + 1)
    if num == secondsPerTask:
        return True
    else:
        return False


def main():
    for _ in range(10):
        simulation(3600, 10, 10, 20)


if __name__ == "__main__":
    main()
