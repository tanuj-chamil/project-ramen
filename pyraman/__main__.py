from spectrum.raman import RamanSpectrum as rs
from preprocessing import baseline
from preprocessing import denoise
import pandas as pd
from random import randint as r
import numpy as np
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
    plt.plot(spectrum.shift,spectrum.intensity)
    if baseline : plt.plot(spectrum.shift,spectrum.baseline)
    plt.ylabel("Intensity")
    plt.xlabel("Shift (cm$^{-1}$)")
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.savefig(filename+'.pdf')
    return

def tempplot(spectrum):
    plt.figure(figsize=(3, 2))
    plt.plot(spectrum.shift,spectrum.intensity)
    plt.ylabel("Intensity")
    plt.xlabel("Shift (cm$^{-1}$)")
    plt.show()
    return

compound = "riboflavin"
file_path = "pyraman\\resources\\databases\\csv\\{}.csv".format(compound)
data = pd.read_csv(file_path)
molecule =  rs(compound, data['L'], data['I'])


noise = np.random.normal(0,1,len(molecule.shift))

molecule =  rs(compound, data['L'], data['I'])
molecule.intensity += noise
tempplot(molecule)

molecule  = denoise.salvitzky_golay_smooth(molecule,window=25,order=4)
molecule  = baseline.mod_polyfit(molecule,order=6)
molecule.intensity = molecule.intensity/molecule.intensity.max()
tempplot(molecule)


# for i in range(1,5):
#     for j in [5,7,11,15,19,23,25]:
#         molecule =  rs(compound, data['L'], data['I'])
#         molecule.intensity += noise
#         molecule  = denoise.lowess_smooth(molecule,window=j,order=i)
#         plot(molecule,"C:\\Users\\Tanuj\\Desktop\\figures\\lowess-{}-{}".format(compound,100+i,1000+j))


