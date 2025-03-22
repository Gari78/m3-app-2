from ._anvil_designer import createAppointmentTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class createAppointment(createAppointmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.type_dropdown()

    # Any code you write here will run before the form opens.

  def save_button_click(self, **event_args):
    open_form('Citas')

  def discard_button_click(self, **event_args):
    open_form('Citas')

  def type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
