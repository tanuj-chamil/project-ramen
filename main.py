import spectrum as s
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as r

file_path = "databases\\csv\\chitin.csv"
data = pd.read_csv(file_path)

molecule =  s.Spectrum('adenine', data['L'], data['I'])



molecule.correct_baseline(polyoder=6)
molecule.plot().show()
print(molecule.fingerprint)
