from ._anvil_designer import TemplateTemplate
from anvil import *


class Template(TemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def appointmentsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Citas')

  def statisticsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('stats')

  def reportsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def reset_links(self, **event_args):
    self.homeLink.role = ''
    self.statisticsLink.role = ''
    self.appointmentsLink.role = ''
    self.reportsLink.role = ''

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

