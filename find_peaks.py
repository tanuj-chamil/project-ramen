from scipy.signal import find_peaks

def detect_peaks(x,y,threshold=0):
    max_peak = max(y)
    peaks = find_peaks(y,prominence=1,height = max(y)*threshold)
    
    x_peaks = [x[i] for i in peaks[0]]
    y_peaks = [y[i] for i in peaks[0]]

    return(x_peaks,y_peaks)
    # print(_x)
    # plt.plot(x, y)
    # plt.plot(_x, _y, "xr")
    # plt.show()