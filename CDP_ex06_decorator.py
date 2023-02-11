# Title:CPD_ex06_decorator
# Purpose : To add functionality to a class using a decorator
# Instructions : Review the code below that uses a class to hold energy use
#               The class will initialise on client name and use of electricity
#               The last code block tests this, add a decorator pattern to append
#               An indicator if the use is {'normal' <= 40 KWh},
#               {'above average' >40 KWh <=110 KWh} {'very high' > 110 KWh}
#               You will have to override some of the builtin methods (getattr)
#               and str

class EnergyClient(object):

    def __init__(self, client_name, electricity_use):
        self.client_name = client_name
        self.electricity_use = electricity_use

    def __str__(self):
        return f"client {self.client_name} usage {self.electricity_use} KWh"



clients = []
clients.append(EnergyClient("Peter Parker", 100))
clients.append(EnergyClient("Jessica Ribbit", 500))
clients.append(EnergyClient("Phil Cat", 10))

for client in clients:
    print(client)
