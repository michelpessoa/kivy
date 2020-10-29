#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text="Teste"
    lb.italic=True
    lb.bold=True
    lb.font_size=50
    return lb

app = App()
app.build = build
app.run()