class Service:
    def __init__(self, service_name):
        self.service_name = service_name

    def print_service_name(self):
        print(f"Service name: {self.service_name}")

class Client:
    def __init__(self, service):
        self.service = service

    def print_service_name(self):
        self.service.print_service_name()

service = Service("Network Service")
client = Client(service)
client.print_service_name()
