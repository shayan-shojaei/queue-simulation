from time import time

class Customer:
    def __init__(self, arrival_time, priority = False):
        self.start_time = time()
        self.service_start = -1
        self.service_end = -1
        self.priority = priority
    
    def start_service(self, time):
        self.service_start = time

    def end_service(self, time):
        self.service_end = time