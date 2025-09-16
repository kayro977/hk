import flet as ft 



class login_page():
    def __init__(self):
        super().__init__()
        self.nombre = ft.TextField(label="usuario",border_color=ft.Colors.RED)
        self.contraseña =  ft.TextField(label="contraseña",password=True,border_color=ft.Colors.RED)


    def build(self):
        return ft.Column([self.nombre,self.contraseña])




def main(page):
    page.theme_mode = ft.ThemeMode.DARK
    login_pagina = login_page().build()
    page.add(login_pagina)


ft.app(target=main)