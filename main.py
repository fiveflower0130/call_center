# -*- coding: utf-8 -*-
import random
import threading

class PM(object):
    pm_call_list = []
    pm_work_status = False
    pm_id = None
    pm_level = None

    def __init__(self, ID, LEVEL):
        self.pm_id = ID
        self.pm_level = LEVEL

    def run(self):
        # for customer in range(len(self.pm_call_list)):
        for customer in self.pm_call_list:
            print("PM processed customer id=" + str(customer.cus_id))
            self.cancel_pm_call_list(customer)

    def register_pm_call_list(self, customer):
        self.pm_call_list.append(customer)
        self.pm_work_status = True

    def cancel_pm_call_list(self, customer):
        self.pm_call_list.remove(customer)
        if len(self.pm_call_list) == 0:
            self.pm_work_status = False

class TL(object):
    tl_call_list = []
    tl_work_status = False
    tl_id = None
    tl_level = None

    def __init__(self, ID, LEVEL):
        self.tl_id = ID
        self.tl_level = LEVEL

    def run(self):
        # for customer in range(len(self.tl_call_list)):
        for customer in self.tl_call_list:
            print("TL processed customer id=" + str(customer.cus_id))
            self.cancel_tl_call_list(customer)          
        
    def register_tl_call_list(self, customer):
        self.tl_call_list.append(customer)
        self.tl_work_status = True

    def cancel_tl_call_list(self, customer):
        self.tl_call_list.remove(customer)
        if len(self.tl_call_list) == 0:
            self.tl_work_status = False

class EP(object):
    # ep_work_status = False
    ep_call_list = []
    ep_num = None

    def __init__(self, num):
        self.ep_num = num

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def process_call(self, i):
        for customer in self.ep_call_list:
            print("EP"+str(i)+" processed customer id=" + str(customer.cus_id))
            self.cancel_ep_call_list(customer)

    def register_ep_call_list(self, customer):
        self.ep_call_list.append(customer)

    def cancel_ep_call_list(self, customer):
        self.ep_call_list.remove(customer)

    def run(self):
        ep_list = []
        for i in range(self.ep_num):
            ep = threading.Thread(target=self.process_call, args = (str(i+1)))
            ep_list.append(ep)
        for i in range(self.ep_num):
            ep_list[i].start()
        for i in range(self.ep_num):
            ep_list[i].join()

class Customer(object):
    cus_id = None
    cus_level = None

    def __init__(self, ID, LEVEL):
        self.cus_id = ID
        self.cus_level = LEVEL
    
    def __str__(self):
        return str(self.__dict__)

class Center(object):
    num_of_employee = None
    customers_call_list = []
    pm = None
    tl = None
    ep = None

    def __init__(self):
        
        self.num_of_employee = self.get_value("Please write number of employees: ",
                                            "Incorrect value. Number of employees should be integer higher than 1.", 1)
        customers_num = self.get_value("Please write number of customers: ",
                                       "Incorrect value. Number of customers should be non-negative integer.", 0)
        # for i in range(self.num_of_employee):
        #     self.employee_list.append(EP(i+1, 1))
        
        for i in range(customers_num):
            call_level = random.randint(1, 3)
            self.customers_call_list.append(Customer(i+1, call_level))
        self.pm = PM(1, 3)
        self.tl = TL(1, 2)
        self.ep = EP(self.num_of_employee)

    def get_value(self, message, incorrect_message, minimal_value):
        """Interface method for acquiring integer value from user, higher than minimal value."""
        val = None
        try:
            val = int(input(message))
        except ValueError:
            print(incorrect_message)
            return self.get_value(message, incorrect_message, minimal_value)
        if val < minimal_value:
            print(incorrect_message)
            return self.get_value(message, incorrect_message, minimal_value)
        else:
            return val

    def enter_customers(self):
        """Function to get all customers from class list."""
        for customer in self.customers_call_list:
            print(customer)
            if customer.cus_level < self.tl.tl_level:
                self.ep.register_ep_call_list(customer)
                self.customers_call_list.remove(customer)
                # print("ep list: ", self.ep.ep_call_list, "cus list: ",self.customers_call_list)
            else:
                if customer.cus_level < self.pm.pm_level:
                    self.tl.register_tl_call_list(customer)
                    self.customers_call_list.remove(customer)
                    # print("tl list: ",self.tl.tl_call_list, "cus list: ",self.customers_call_list)
                else:
                    self.pm.register_pm_call_list(customer)
                    self.customers_call_list.remove(customer)
                    # print("pm list: ",self.pm.pm_call_list, "cus list: ",self.customers_call_list)

    def run(self):
        """Core step function. Every time when called:
        - awaiting customers enter the call center (register_customer is called)
        - according to customer level to put in list
        - ep, tl and pm process customer depending on customer level
        - any customer leaves the call center (cancel_customer is called)
        """

        self.enter_customers()
        self.pm.run()
        self.tl.run()
        self.ep.run()

    def output(self):
        """Returns total number of steps done by call center in set strategy."""
        total_number = 0
        while self.awaiting_customers():
            self.run()
            total_number += 1
        return total_number

    def awaiting_customers(self):
        """returns True if there is at least one customer not on process. Otherwise returns False."""
        if len(self.customers_call_list) > 0:
            return True
        return False


def main():
    """main function"""

    call_center = Center()
    print("total spend " + str(call_center.output()) + " times for processing customers")
    
if __name__ == "__main__":
    main()