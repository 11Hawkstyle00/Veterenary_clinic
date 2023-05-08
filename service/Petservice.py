from repository.petRepo import PetRepo

class PetService:
    def __init__(self):
        self._petsRepo = PetRepo()

    def get_by_id(self,id):
        pet = None
        for item in self._petsRepo.get_pets():
            if item.get_id() == id:
                pet = item
        return pet

    def get_by_name(self, name):
        pet = None
        for item in self._petsRepo.get_pets():
            if item.get_name() == name:
                pet = item
        return pet

    def all_get_pets(self):
        return self._petsRepo.get_pets()

    def del_by_id(self):
         for item in self._petsRepo.get_pets():
            if item.get_id() == id:
                self._petsRepo.get_pets().remove(self.get_by_id(id))

    def create(self,pet):
        if pet.get_name() == ' ':
            print('Имя не может быть пустым')
            self._petsRepo.get_pets().append(pet)

    def edit(self, pet):
        for item in self._petsRepo.get_pets():
            if item.get_id() == pet.id:
                item.set_name(pet.get_name())

