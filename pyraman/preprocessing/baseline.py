from numpy import polyfit
from numpy import polyval
import numpy as np

def mod_polyfit(spectrum, order=4, iterations=128):
    baseline = spectrum.intensity
    for _ in range(iterations):
        fit = polyval(polyfit(spectrum.shift,baseline,deg=order),spectrum.shift)
        baseline = [min(baseline[i],fit[i]) for i in range(len(spectrum.shift))]
    else:
        spectrum.intensity = spectrum.intensity - baseline
        spectrum.processing_history.append ['baseline-mod_polyfit-order-{}-iterations-{}'.format(order,iterations)]
    return spectrum