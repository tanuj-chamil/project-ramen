import numpy as np
from scipy.signal import savgol_filter,butter,filtfilt
from statsmodels.nonparametric.smoothers_lowess import lowess

#moving average
def moving_average(spectrum,window=3):
    c = np.ones[window]
    spectrum.intensity = np.convolve(spectrum.intensity, c, 'valid')
    return spectrum

#salvitzky golay
def salvitzky_golay(spectrum,order=1,window=7):
    spectrum.intensity = savgol_filter(spectrum.intensity,polyorder=order,window_length=window)
    return spectrum

#lowess
def lowess(spectrum,order=1,fraction=0.05):
    spectrum.intensity = lowess(spectrum.intensity,spectrum.shift,fraction=fraction,return_sorted=False)
    return spectrum

#butterworth 
def butterworth_lowpass(spectrum, order=4,cutoff=60):
    b,a = butter(order, cutoff*2*np.pi,btype='low',analog=False)
    spectrum.intensity = filtfilt(b,a,spectrum.intensity)
    return spectrum
