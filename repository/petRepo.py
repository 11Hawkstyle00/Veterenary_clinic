class PetRepo:
    def __init__(self):
        self._pets = []

    def get_pets(self):
        return self._pets

    def set_pets(self,pets):
        self._pets = pets

    