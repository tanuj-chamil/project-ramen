from scipy.signal import savgol_filter 
from numpy import polyfit
from numpy import polyval

def mod_polyfit(x,y, order=4, iterations=100):
    pre_fit = y
    for _ in range(iterations):
        new_fit = polyval(polyfit(x,pre_fit,deg=order),x)
        new_fit, pre_fit = [min(new_fit[i],pre_fit[i]) for i in range(len(x))], new_fit
    return new_fit

