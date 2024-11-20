from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = anvil.server.call('get_direktor', self.gefaengnisse_drop_down.selected_value)
    self.label_freie_zellen.text = anvil.server.call('get_freiezellen', self.gefaengnisse_drop_down.selected_value)
    zellen = anvil.server.call('get_zellen', self.gefaengnisse_drop_down.selected_value)
    zellendata = []
    for zelle in zellen:
      zellendata.append({'zellennummer': zelle[0], 'anzahl_häftlinge': zelle[1]})
    print(zellendata)
    self.repeating_zellen.items = zellendata

  def gefaengnisse_drop_down_change(self, **event_args):
    self.label_direktor.text = anvil.server.call('get_direktor', self.gefaengnisse_drop_down.selected_value)
    self.label_freie_zellen.text = anvil.server.call('get_freiezellen', self.gefaengnisse_drop_down.selected_value)
    zellen = anvil.server.call('get_zellen', self.gefaengnisse_drop_down.selected_value)
    zellendata = []
    for zelle in zellen:
      zellendata.append({'zellennummer': zelle[0], 'anzahl_häftlinge': zelle[1]})
    print(zellendata)
    self.repeating_zellen.items = zellendata

 



  
 
