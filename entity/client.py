from utils.Autogenerator import Autogenerator

ai = Autogenerator()

class Client:
    def __init__(self,name):
        self._id = ai.unique_id()
        self._name = name

    def to_str(self):
        print('ID: ' + str(self._id) + " NAME: " + str(self._name))

    def get_id(self):
        return self._id
    
    def set_id(self,id):
        self._id = id

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name