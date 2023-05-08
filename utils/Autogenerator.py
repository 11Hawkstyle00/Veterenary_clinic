class Autogenerator:
    def __init__(self) -> None:
        self._id = 0

    def unique_id(self):
         self._id += 1 
         return self._id
    