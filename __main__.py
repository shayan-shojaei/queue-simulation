from simulation import run_simulation

NUMBER_OF_CUSTOMERS = int(input("Customers Count: "))
NUMBER_OF_RESOURCES = int(input("Employees Count: "))
PRIORITY_CHANCE = float(input("Priority Chance: "))

execution_time = run_simulation(NUMBER_OF_RESOURCES, NUMBER_OF_CUSTOMERS, PRIORITY_CHANCE)

print(execution_time)