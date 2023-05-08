class AppointmentsRepo:
    def __init__(self):
        self._appointments = []

    def get_appointments(self):
        return self._appointments

    def set_appointments(self,appointments):
        self._doctors = appointments

        