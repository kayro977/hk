import flet as ft
import openai


class chat_page():
    def __init__(self):
        super().__init__()
        self.dinero = [ft.Row(controls=[ft.Text("hola"),ft.Text("puta"),],spacing=100)]
        self.contenedor = ft.Container(bgcolor=ft.Colors.RED,width=900,height=500)
        self.pregunta = ft.TextField(label="pregunta",width=900)


    def build(self):
        return ft.Row(alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.VerticalAlignment.CENTER,controls=[
            ft.Column(controls=[
                *self.dinero,
                self.contenedor,
                self.pregunta
            ]),
        ])
    

def main(page):
    page.theme_mode = ft.ThemeMode.DARK
    page_chat = chat_page().build()
    page.add(page_chat)

ft.app(main)