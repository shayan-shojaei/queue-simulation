from system import System
from mqueue import MQueue
from distributions import customer_entry
import numpy as np
from customer import Customer


CLOCK_STEP = 0.01


def run_simulation(server_count: int, customer_count: int, priority_chance=0.1):
    system = System(server_count)
    queue = MQueue()
    
    customer_arrival_times = customer_entry(customer_count)
    print(customer_arrival_times)

    queued_customers = 0

    # Each tick of the clock is 0.01 seconds
    clock = 0

    finish_events = []

    finished_customers = []
    
    customers_data = {}
    customer_id = 0
    while not queue.is_empty() or len(finish_events) > 0 or queued_customers != customer_count:
        if queued_customers < customer_count and customer_arrival_times[0] == clock:
            customer_id += 1
            # Customer entry
            new_customer_arrival_time = customer_arrival_times.pop(0)
            new_customer_priority_state = np.random.uniform() < priority_chance
            queued_customers += 1
            customer = Customer(arrival_time=new_customer_arrival_time, priority=new_customer_priority_state)
 

            if customer.priority:
                queue.enqueue_priority(customer)
            else:
                queue.enqueue(customer)
            
            print(f"{clock} \t # \t New customer arrived and queued.")

        elif not queue.is_empty() and system.can_serve():
            # Job assignment
            customer = queue.dequeue()
            
            server, service_time = system.serve()
            customer.start_service(clock, server)
            finish_events.append({ 'server': server, 'time': round(clock+service_time, 2), 'customer': customer })

            finish_events = sorted(finish_events, key=lambda e: e['time'])

            print(f"{clock} \t @ \t Customer assigned to server {server+1} and is set to finish in {round(clock+service_time, 2)}")

        elif len(finish_events) > 0 and clock == finish_events[0]['time']:
            # Customer served
            event = finish_events.pop(0)
            event['customer'].end_service(clock)
            system.free_server(event['server'])

            finished_customers.append(event['customer'])

            print(f"{clock} \t * \t Server {event['server']+1} finished proccessing and is free.")
        else:
            clock = round(clock + CLOCK_STEP, 2)
    
    return finished_customers, system.server_stats, clock


