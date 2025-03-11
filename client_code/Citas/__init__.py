from ._anvil_designer import CitasTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Citas(CitasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    data = [
        {"nombre": "Item 1", "descripcion": "Descripción 1"},
        {"nombre": "Item 2", "descripcion": "Descripción 2"},
        {"nombre": "Item 3", "descripcion": "Descripción 3"},
    ]
    self.AppointmentListPanel.items = data

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.appointmentsLink.role = 'selected'
    #response = await fetch("https://api.tuservicio.com/endpoint");
    
