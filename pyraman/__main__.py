from spectrum.raman import RamanSpectrum as rs
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as r

file_path = "pyraman\\resources\\databases\\csv\\chitin.csv"
data = pd.read_csv(file_path)

molecule =  rs('adenine', data['L'], data['I'])



molecule.plot().show()
print(molecule.fingerprint)
