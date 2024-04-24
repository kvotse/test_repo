class Employees:
    def get_paid(self):
        pass


class Worker(Employees):
    def get_paid(self):
        return 400


class Worker2(Employees):
    def get_paid(self):
        return 500


manager = Worker()
worker = Worker2()

print(manager.get_paid())
print(worker.get_paid())
