from ._anvil_designer import RowDetailsClickTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowDetailsClick(RowDetailsClickTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Details_click(self, **event_args):
    parent = self.parent.parent.parent.parent
    zellennummer = self.item['zellennummer']
    print(zellennummer)
    hids = anvil.server.call('get_hid', zellennummer)
    print("hids")
    print(hids)
    zellendetails = anvil.server.call('get_häftlinge_data', hids)
    print("Zellendatails")
    print(zellendetails)
    data = []
    for zellendatail in zellendetails:
      data.append({'haeftlingsnummer': zellendatail[0], 'einzug': zellendatail[2], 'auszug': zellendatail[3], 'haftdauer': zellendatail[1]})
    print("Data")
    print(data)
    parent.repeating_panel_zellendetails.items = data
