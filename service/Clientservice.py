from repository.clientRepo import ClientsRepo

class ClientService:
    def __init__(self):
        self._clientsRepo = ClientsRepo()

    def get_by_id(self,id):
        client = None
        for item in self._clientsRepo.get_clients():
            if item.get_id() == id:
                client = item 
        return client

    def all_get_clients(self):
        return self._clientsRepo.get_clients()

    def del_by_id(self,id):
        for item in self._clientsRepo.get_clients():
            if item.get_id() == id:
                self._clientsRepo.get_clients().remove(self.get_by_id(id))

    def create(self,client):
        if client.get_name()==' ':
            print('Имя не может быть пустым')
            self._clientsRepo.get_clients().append(client)

    def edit(self,id,client):
        for item in self._clientsRepo.get_clients():
            if item.get_id() == id:
                item.set_name(client.get_name())

