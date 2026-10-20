
import flet as ft

from Models.lista_enlazada import ListaEnlazada
from Views.vista import Vista
from Controller.controlador import Controlador


def main(page: ft.Page):
    vista = Vista(page)
    modelo = ListaEnlazada()
    Controlador(vista, modelo)


if __name__ == "__main__":
    ft.run(main)

