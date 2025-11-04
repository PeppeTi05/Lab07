import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdowm(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()


    # TODO

    # CALLBACKS DROPDOWN
    def handler_dd_musei(self, e):
        pass

    def handler_dd_artefatti(self, e):
        pass

    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def handler_btnArtefatti(self, e):
        pass

    # TODO
