class ClientsRepo:
    def __init__(self):
        self._clients = []

    def get_clients(self):
        return self._clients

    def set_clients(self,clients):
        self._clients = clients
        