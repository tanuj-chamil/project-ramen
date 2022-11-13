from find_peaks import detect_peaks
from scipy.signal import savgol_filter as sgf
import numpy as np
import plotly.express as px
from algorithm import mod_polyfit,find_peaks

class Spectrum:

    def __init__(self,name,L,I) -> None:
        """initiate spectrum objcet

        Args:
            L (iterable): raman shift waves of the spectrum
            I (iterable): corresponding intensities to the raman shifts
        """
        self.raman_shift = np.array(L)
        self.intensity = np.array(I)
        self.name= name
        self.fingerprint = self.generate_fingerprint()
    
    def denoise(self, polyoder = 1, section_size = 7):
        """_summary_

        Args:
            polyoder (int, optional): order of polynimal fit. Defaults to 1.
            section_size (int, optional): convoluting section size. Defaults to 7.
        """
        self.intensity = sgf(self.intensity,window_length=section_size, polyorder=polyoder)

    def plot(self):
        """_summary_

        Returns:
            potly figure: _description_
        """
        graph=px.line(x=self.raman_shift, y=self.intensity, title=self.name)
        return graph

    def correct_baseline(self, polyoder = 4):
        self.intensity = self.intensity - np.array(mod_polyfit(self.raman_shift,self.intensity,order=polyoder, iterations= 200))

    def generate_fingerprint(self):
        peak_indices = find_peaks(self.intensity)[0]
        fingerprint = np.array([[self.raman_shift[p],self.intensity[p]] for p in peak_indices])
        return fingerprint



