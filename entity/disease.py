from utils.Autogenerator import Autogenerator

ai = Autogenerator()

class Disease:
    def __init__(self,name) -> None:
        self._name = name
        # self._id = ai.unique_id()

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name 
    