import flet as ft

class Presets():
    def main(self, page: ft.Page):
        page.fonts = {
            "Intro1": "C:/Users/Tima/Algebra/matrix_and_Vectors_withUI/fronts/IntroDemo-BlackCAPS.otf",
            "Forum": "C:/Users/Tima/Algebra/matrix_and_Vectors_withUI/fronts/Forum-Regular.ttf",
        }
    def frontText(self, frontChek:str):
        if frontChek == "1":
            style = ft.TextStyle(font_family="Forum")
        if frontChek == "2":
            style = ft.TextStyle(font_family="Intro1")

    def frontButton(self, frontChek):
        if frontChek == "1":
            style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Forum"))
        if frontChek == "2":
            style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))


#"#ff5757"