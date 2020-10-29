#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button

def build():
    bt = Button(text="Clique aqui")
    return bt

app = App()
app.build = build
app.run()
