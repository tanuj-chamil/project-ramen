from spectrum.raman import RamanSpectrum as rs
from preprocessing import baseline
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as r

file_path = "pyraman\\resources\\databases\\csv\\chitin.csv"
data = pd.read_csv(file_path)

molecule =  rs('adenine', data['L'], data['I'])

molecule.plot().show()

molecule = baseline.mod_polyfit(molecule,order=6, iterations = 200)


molecule.plot().show()
print(molecule.fingerprint)
