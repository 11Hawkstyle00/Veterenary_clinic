from repository.diseaseRepo import DiseaseRepo

class DiseaseService:
    def __init__(self):
        self._DiseaseRepo = DiseaseRepo()

    # def get_by_id(self,id):
    #     diseases = None
    #     for item in self._DiseaseRepo.get_diseases():
    #         if item.get_id() == id:
    #             diseases = item
    #     return diseases

    def get_by_name(self,name):
        diseases = None
        for item in self._DiseaseRepo.get_diseases():
            if item.get_name() == name:
                diseases = item
        return diseases

    def all_get_diseases(self):
        return self._DiseaseRepo.get_diseases()

    # def del_by_id(self):
    #      for item in self._DiseaseRepo.get_diseases():
    #         if item.get_id() == id:
    #             self._DiseaseRepo.get_diseases().remove(self.get_by_id(id))

    def create(self,diseases):
        if diseases.get_name() == ' ':
            print('Имя не может быть пустым')
            self._DiseaseRepo.get_diseases().append(diseases)

    # def edit(self,diseases):
    #     for item in self._DiseaseRepo.get_diseases():
    #         if item.get_id() == diseases.id:
    #             item.set_name(diseases.get_name())