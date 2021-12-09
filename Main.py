from CustomerStates import CustomerStates
from Pizzeria import Pizzeria
from time import ctime, sleep


def setSimulationParameters():
    numOfTables = 8
    numOfWaiters = 2
    numOfCustomers = 20

    startTime = 8
    minutes = 0
    step = 2

    run_sim = True
    end_list = []

    parameters = (numOfTables, numOfWaiters, 
                  numOfCustomers, startTime, 
                  minutes, step, run_sim, end_list)

    return parameters


def formatTime(startTime, minutes):
    if (minutes >= 60):
        minutes = 0
        startTime += 1

    if (len(str(minutes)) == 1):
        min = "0" + str(minutes)
        hour = str(startTime)
    else:
        min = str(minutes)
        hour = str(startTime)

    return hour, min, startTime, minutes


if __name__ == "__main__":
    numOfTables, numOfWaiters, numOfCustomers, startTime, minutes, step, run_sim, end_list = setSimulationParameters()

    sim_pizzeria = Pizzeria(numOfTables, numOfWaiters, numOfCustomers)

    print("START:", str(startTime) + ":" + str(minutes))
    
    while(run_sim):
        for customer in sim_pizzeria.getCustomersList():
            customer.doAction(sim_pizzeria)

            if(customer.getState() == CustomerStates.OUT and customer.getID() not in end_list):
                end_list.append(customer.getID())

        print("----------------------------------------------------------------------------------------")

        for waiter in sim_pizzeria.getWaitersList():
            waiter.doTask(sim_pizzeria)

        sim_pizzeria.decreaseOrdersTime()

        if (len(end_list) == numOfCustomers):
            run_sim = False

        minutes += step
        hour, min, startTime, minutes = formatTime(startTime, minutes)
        print("========================================================================================")
        print("CZAS:", hour + ":" + min)
        print("WYSZLO:", len(end_list))
        print("========================================================================================")
        sleep(step)
