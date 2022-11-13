from scipy.signal import savgol_filter
from scipy.signal import find_peaks as fp
from numpy import polyfit
from numpy import polyval
import numpy as np

def mod_polyfit(x,y, order=4, iterations=100):
    pre_fit = y
    for _ in range(iterations):
        new_fit = polyval(polyfit(x,pre_fit,deg=order),x)
        new_fit = [min(new_fit[i],pre_fit[i]) for i in range(len(x))]
        pre_fit = new_fit
    return new_fit

def find_peaks(intensities):
    peak_indices = fp(intensities,prominence=5)
    return peak_indices
