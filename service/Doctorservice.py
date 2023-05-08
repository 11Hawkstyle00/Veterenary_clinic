from repository.doctorRepo import DoctorsRepo

class DoctorService:
    def __init__(self):
        self._doctorsRepo = DoctorsRepo()

    def get_by_id(self,id):
        doctor = None
        for item in self._doctorsRepo.get_doctors():
            if item.get_id() == id:
                doctor = item
        return doctor

    def get_by_name(self,name):
        doctor = None
        for item in self._doctorsRepo.get_doctors():
            if item.get_name() == name:
                doctor = item
        return doctor

    def all_get_doctors(self):
        return self._doctorsRepo.get_doctors()

    def del_by_id(self):
         for item in self._doctorsRepo.get_doctors():
            if item.get_id() == id:
                self._doctorsRepo.get_doctors().remove(self.get_by_id(id))

    def create(self,doctor):
        if doctor.get_name() == ' ':
            print('Имя не может быть пустым')
            self._doctorsRepo.get_doctors().append(doctor)

    def edit(self,doctor):
        for item in self._doctorsRepo.get_doctors():
            if item.get_id() == doctor.id:
                item.set_name(doctor.get_name())

