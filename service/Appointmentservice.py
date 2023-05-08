from repository.appointmentRepo import AppointmentsRepo

class AppointmentService:
    def __init__(self):
        self._AppointmentsRepo = AppointmentsRepo()

    def get_by_id(self,id):
        reception = None
        for item in self._AppointmentsRepo.get_appointments():
            if item.get_id() == id:
                reception = item
        return reception

    def get_by_name(self, name):
        reception = None
        for item in self._AppointmentsRepo.get_appointments():
            if item.get_name() == name:
                reception = item
        return reception

    def all_get_appointments(self):
        return self._AppointmentsRepo.get_appointments()

    def del_by_id(self):
         for item in self._AppointmentsRepo.get_appointments():
            if item.get_id() == id:
                self._AppointmentsRepo.get_appointments().remove(self.get_by_id(id))

    def create(self,reception):
        if reception.get_name() == ' ':
            print('Имя не может быть пустым')
            self._AppointmentsRepo.get_appointments().append(reception)

    def edit(self,reception):
        for item in self._AppointmentsRepo.get_appointments():
            if item.get_id() == reception.id:
                item.set_name(reception.get_name())