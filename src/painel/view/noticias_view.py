import streamlit as st
from src.painel.controller.noticias_controller import NoticasControler


class NoticiasView():

    def __init__(self, controller: NoticasControler) -> None:
        self.__controler = controller

    def exibir_tela(self):

        st.title('Feed de Noticias')
