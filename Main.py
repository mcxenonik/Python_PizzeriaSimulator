from Pizzeria import Pizzeria
from time import ctime, sleep


if __name__ == "__main__":
    numOfTables = 5
    numOfWaiters = 4
    numOfCustomers = 11

    sim_pizzeria = Pizzeria()

    for i in range(numOfTables):
        sim_pizzeria.addTable()

    for i in range(numOfWaiters):
        sim_pizzeria.addWaiter()
    
    for i in range(numOfCustomers):
        sim_pizzeria.addCustomer()

    run_sim = True
    end_list = []


    while(run_sim):
        for customer in sim_pizzeria.getCustomersList():
            customer.doAction(sim_pizzeria)
            if(customer.getState() == "OUT" and customer.getID() not in end_list):
                end_list.append(customer.getID())

        for waiter in sim_pizzeria.getWaitersList():
            waiter.doTask(sim_pizzeria)

        print("============================================")
        print(ctime())
        print(len(end_list))
        print("============================================")
        sleep(2)

        if (len(end_list) == numOfCustomers):
            run_sim = False
