import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name, GID from Gefaengnis"))
  return res

@anvil.server.callable
def get_direktor(gid):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = cursor.execute(f"SELECT Direktor from Verwaltung WHERE GID={gid}").fetchone()
  return res[0]

@anvil.server.callable
def get_freiezellen(gid):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = cursor.execute(f"SELECT FreieZellen from Verwaltung WHERE GID={gid}").fetchone()
  return res[0]

@anvil.server.callable
def get_zellen(gid):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Zellennummer, AnzahlHäftlinge from Zelle WHERE GID={gid}"))
  return res

@anvil.server.callable
def get_häftlinge_data(hid):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  data = []
  for x in hid:
    res = list(cursor.execute(f"SELECT Häftlingsnummer, Haftdauer from Häftling WHERE HID={x[0]}"))
    print("res")
    print(res)
    ergebnis = [res[0][0], res[0][1], x[1], x[2]]
    data.append(ergebnis)
  return data

@anvil.server.callable
def get_hid(zellennumer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  zid = anvil.server.call('get_zid', zellennumer)
  res = list(cursor.execute(f"SELECT HID, Einzug, Auszug from Bewohnen WHERE ZID={zid}"))
  return res

@anvil.server.callable
def get_zid(zellennummer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = cursor.execute(f"SELECT ZID from Zelle WHERE Zellennummer={zellennummer}").fetchone()
  return res[0]







