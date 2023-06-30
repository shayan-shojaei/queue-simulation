import pandas as pd


def display_stats(customers_data, server_stats, total_time):
    customers_data = sorted(customers_data, key=lambda q: q.start_time)
    customer_arrival = []
    customer_service_start = []
    customer_service_end = []
    customer_service_time = []
    customer_service_wait = []
    customer_total_time = []
    customer_server = []

    # customer stats
    for customer in customers_data:
        customer_arrival.append(customer.start_time)
        customer_service_start.append(customer.service_start)
        customer_service_end.append(customer.service_end)
        customer_service_time.append(customer.service_end - customer.service_start)
        customer_service_wait.append(customer.service_start - customer.start_time)
        customer_total_time.append(customer.service_end - customer.start_time)
        customer_server.append(customer.server)

    customer_stats = pd.DataFrame(
        data=zip(
            customer_arrival,
            customer_service_start,
            customer_service_end,
            customer_service_time,
            customer_service_wait,
            customer_total_time,
            customer_server,
        ),
        columns=[
            "arrival",
            "service_start",
            "service_end",
            "service_time",
            "service_wait",
            "total_time",
            "server#",
        ],
    )
    print("Simulation states:")
    print(customer_stats.head(10))

    print("Customer stats:")
    print(customer_stats.describe().drop(columns=["server#"]))

    # server stats
    # for server in server_stats:
