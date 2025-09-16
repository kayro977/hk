import flet as ft
import sqlite3
import dataclasses,datetime


@dataclasses.dataclass
class Producto:
    nombre:str
    cantidad:int
    precio:float
    fecha:str

class inventario_page():
    def __init__(self):
        self.nombre
        self.cantidad
        self.precio
        self.fecha = datetime.datetime.now()


    def build(self):
        return
    




def main(page):
    page.theme_mode = ft.ThemeMode.DARK
    pagina_inventario = inventario_page().build()
    page.add(pagina_inventario)
    
ft.app(target=main)