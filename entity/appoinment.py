from entity.client import Client
from utils.Autogenerator import Autogenerator

ai = Autogenerator()


class Appoinment:
    def __init__(self,client,pet,doctor) -> None:
        self._id = ai.unique_id()
        self._client = client
        self._pet = pet
        self._doctor = doctor

    def to_str(self):
        return "ID: " + str(self._id) + "Client: " + str(self._client.name) + "Doctor" + str(self._doctor) + "Pet" + str(self._pet)
    def get_id(self):
        return self._id
    
    def set_id(self,id):
        self._id = id
    
    def get_pet(self):
        return self._pet

    def set_pet(self,pet):
        self._pet = pet

    def get_doctor(self):
        return self._doctor()

    def set_doctor(self,doctor):
        self._doctor = doctor

    
    
