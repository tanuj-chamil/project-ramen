from spectrum.raman import RamanSpectrum as rs
from preprocessing import baseline
import pandas as pd
from random import randint as r

import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science','bright'])
plt.rcParams.update({'figure.dpi': '300', 'lines.linewidth' : 0.6})
plt.rcParams.update({'figure.max_open_warning': 0})

def save_to_csv(spectrum,file_path):
    string = "shift, intensity\n"
    for i in range(len(spectrum.shift)):
        string += "{}, {}\n".format(spectrum.shift[i],spectrum.intensity[i])
    f = open(file_path,'w')
    f.write(string)
    f.close()

def plot(spectrum,filename,baseline=False):
    plt.figure(figsize=(3, 2))
    plt.plot(spectrum.shift,spectrum.raw_intensity)
    if baseline : plt.plot(spectrum.shift,spectrum.baseline)
    plt.ylabel("Intensity")
    plt.xlabel("Shift (cm$^{-1}$)")
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.savefig(filename+'.pdf')
    return

compound = "cellulose"
file_path = "pyraman\\resources\\databases\\csv\\{}.csv".format(compound)
data = pd.read_csv(file_path)

for i in range(1,11):
    for j in [1,2,5,10,20,50,100,200]:
        molecule =  rs(compound, data['L'], data['I'])
        molecule = baseline.mod_polyfit(molecule,order=i, iterations = j)
        plot(molecule,"C:\\Users\\Tanuj\\Desktop\\figures\\{}-{}-{}".format(compound,100+i,1000+j),baseline=True)


