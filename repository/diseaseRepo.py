class DiseaseRepo:
    def __init__(self):
        self._diseases = []

    def get_diseases(self):
        return self._diseases

    def set_diseases(self,diseases):
        self._diseases = diseases