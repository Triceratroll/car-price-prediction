import pandas as pd

def normalize_color(color):
    palabras = color.split(" ")
    primeraPalabra = palabras[0].upper()
    return palabras[0]