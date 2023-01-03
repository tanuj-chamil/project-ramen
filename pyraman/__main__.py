from spectrum.raman import RamanSpectrum as rs
from preprocessing import baseline
import pandas as pd
from random import randint as r



def save_to_csv(spectrum,file_path):
    string = "shift, intensity\n"
    for i in range(len(spectrum.shift)):
        string += "{}, {}\n".format(spectrum.shift[i],spectrum.intensity[i])
    f = open(file_path,'w')
    f.write(string)
    f.close()

file_path = "pyraman\\resources\\databases\\csv\\chitin.csv"
data = pd.read_csv(file_path)

molecule =  rs('adenine', data['L'], data['I'])

molecule = baseline.mod_polyfit(molecule,order=6, iterations = 1)
molecule.plot(baseline=True)

save_to_csv(molecule,"processed_data\\csv\\1.csv")

print(molecule.fingerprint)
