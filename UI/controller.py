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
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()

        # Do la possibilità all'utente di non applicare filtri per i musei
        self._view.dd_musei.options.append(ft.dropdown.Option("Nessun filtro"))
        for museo in musei:
            self._view.dd_musei.options.append(ft.dropdown.Option(str(museo.nome)))

        # Do la possibilità all'utente di non applicare filtri per i musei
        self._view.dd_epoche.options.append(ft.dropdown.Option("Nessun filtro"))
        for epoca in epoche:
            self._view.dd_epoche.options.append(ft.dropdown.Option(epoca))

        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    def on_select_museo(self, e):
        self.museo_selezionato = e.control.value

    def on_select_epoca(self, e):
        self.epoca_selezionata = e.control.value
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def handler_btnArtefatti(self, e):
        lista = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        if len(lista) == 0:
            self._view.show_alert("Nessun artefatto trovato")
            return
        self._view.lista_artefatti.controls.clear()
        for a in lista:
            self._view.lista_artefatti.controls.append(ft.Text(str(a)))
        self._view.update()

    # TODO
