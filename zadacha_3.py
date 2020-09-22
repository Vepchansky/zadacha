import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        self.log(msg)

zhora = LoggableList()
zhora.append('suka')
