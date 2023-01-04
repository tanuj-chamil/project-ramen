import numpy as np

def min_max_norm(spectrum, height = 1):
    norm_factor = max(spectrum.intensity)*height
    spectrum.intensity = spectrum.intensity/norm_factor
    spectrum.processing_history.append ['normalize-min_max-height-{}'.format(height)]
    return spectrum

