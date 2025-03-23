from ._anvil_designer import createAppointmentTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time


class createAppointment(createAppointmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.type_dropdown.items = ["Normal", "Telemático", "Urgente", "Privado"]
    self.startTime = int(time.time())

    # Any code you write here will run before the form opens.

  def save_button_click(self, **event_args):
    open_form('Citas')

  def discard_button_click(self, **event_args):
    open_form('Citas')

  def type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    elapsed_time = int(time.time()) - self.startTime  # Tiempo transcurrido en segundos
    elapsed_minutes = elapsed_time // 60  # Obtiene los minutos
    elapsed_seconds = elapsed_time % 60   # Obtiene los segundos restantes
    
    # Formatea MM:SS con ceros a la izquierda
    self.appointment_timer.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"