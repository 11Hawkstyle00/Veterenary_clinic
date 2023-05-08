class DoctorsRepo:
    def __init__(self):
        self._doctors = []

    def get_doctors(self):
        return self._doctors

    def set_doctors(self,doctors):
        self._doctors = doctors