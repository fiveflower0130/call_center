# -*- coding: utf-8 -*-
import random

class PM(object):
    pm_call_list = []
    pm_work_status = False
    pm_level = None

    def __init__(self, LEVEL):
        self.pm_level = LEVEL

    def process_call(self):
        for mission in range(len(pm_call_list)):
            print("PM processed call")
            cancel_pm_call_list(mission)

    def register_pm_call_list(self, mission):
        self.pm_call_list.append(mission)
        self.pm_work_status = True

    def cancel_pm_call_list(self, mission):
        self.pm_call_list.remove(mission)
        if len(self.pm_call_list) == 0:
            self.pm_work_status = False

class TL(object):
    tl_call_list = []
    tl_work_status = False
    tl_level = None

    def __init__(self, LEVEL):
        self.tl_level = LEVEL

    def process_call(self):
        for mission in range(len(self.tl_call_list)):
            print("TL processed call")
            cancel_tl_call_list(mission)
            # if mission <= 2  and work_status == False:
            #     print("TL processed call")
            #     cancel_tl_call_list(mission)
            # else:
            #     print("TL can not process call hand over to PM ")
            #     cancel_tl_call_list(mission)
            #     return mission
                
        
    def register_tl_call_list(self, mission):
        self.tl_call_list.append(mission)
        self.tl_work_status = True

    def cancel_tl_call_list(self, mission):
        self.tl_call_list.remove(mission)
        if len(self.tl_call_list) == 0:
            self.tl_work_status = False

class EP(object):
    # ep_work_status = False
    ep_ID = None
    ep_level = None

    def __init__(self, ID, LEVEL):
        self.ep_ID = ID
        self.ep_level = LEVEL

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def process_call(self):
        print("EP processed call")

    # def register_ep_call_list(self, mission):
    #     self.ep_call_list.append(mission)
    #     self.ep_work_status = True

    # def cancel_pm_call_list(self, mission):
    #     self.ep_call_list.remove(mission)
    #     if len(self.ep_call_list) == 0:
    #         self.ep_self.work_status = False

class Customer(object):
    ID = None
    LEVEL = None

    def __init__(self, ID, LEVEL):
        self.ID = ID
        self.LEVEL = LEVEL
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Center(object):
    num_of_employee = None
    customers_call_list = []
    pm = None
    tl = None
    employee_list = []

    def __init__(self):
        
        self.num_of_employee = self.get_value("Please write number of employees: ",
                                            "Incorrect value. Number of employees should be integer higher than 1.", 1)
        customers_num = self.get_value("Please write number of customers: ",
                                       "Incorrect value. Number of customers should be non-negative integer.", 0)
        for i in range(self.num_of_employee):
            self.employee_list.append(EP(i, 1))
        
        for i in range(customers_num):
            call_level = random.randint(1, 3)
            self.customers_call_list.append(Customer(i, call_level))
        self.pm = PM(3)
        self.tl = TL(2)

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


def main():
    """main function"""

    call_center = Center()
    for i in range(len(call_center.employee_list)):
        print(call_center.employee_list[i])
    
    for i in range(len(call_center.customers_call_list)):
        print(call_center.customers_call_list[i])


if __name__ == "__main__":
    main()