from find_peaks import detect_peaks
from scipy.signal import savgol_filter as sgf
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from algorithm import mod_polyfit, find_peaks


class Spectrum:

    def __init__(self, name, L, I) -> None:
        """initiate spectrum objcet

        Args:
            L (iterable): raman shift waves of the spectrum
            I (iterable): corresponding intensities to the raman shifts
        """
        self.raman_shift = np.array(L)
        self.raw_intensity = np.array(I)
        self.intensity = self.raw_intensity
        self.name = name
        self.fingerprint = "Normalize to generate the spectral fingerprint"

    def _repr_html_(self):
        self.plot().to_html()

    def denoise(self, polyorder=3, section_size=5):
        """_summary_

        Args:
            polyoder (int, optional): order of polynimal fit. Defaults to 1.
            section_size (int, optional): convoluting section size. Defaults to 7.
        """
        self.intensity = sgf(
            self.intensity, window_length=section_size, polyorder=polyorder)
        return self

    def plot(self):
        """_summary_

        Returns:
            potly figure: _description_
        """

        if type(self.fingerprint) != str:
            peaks = px.scatter(
                x=self.fingerprint[:, 0], y=self.fingerprint[:, 1])
            peaks.update_traces(marker=dict(
                size=8, symbol='arrow-down', color='red'))
            spectrum = px.line(x=self.raman_shift, y=self.intensity)
            figure = go.Figure(data=spectrum.data+peaks.data)
        else:
            figure = px.line(x=self.raman_shift, y=self.intensity)
        return figure.add_hline(y=0, line_width=1, line_dash="dash", line_color="grey")

    def correct_baseline(self, polyorder=4):
        """_summary_

        Args:
            polyorder (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        self.intensity = self.intensity - np.array(mod_polyfit(self.raman_shift, self.intensity,
                                                               order=polyorder, iterations=200))
        return self

    def min_max_normalize(self):
        """normalizes spectrum in range 0 to 1

        Returns:
            Spectrum: Min-max normalized spectrum
        """
        max_intensity = self.intensity.max()
        self.intensity = self.intensity/max_intensity
        self.fingerprint = self.generate_fingerprint()
        return self

    def generate_fingerprint(self):
        peak_indices = find_peaks(self.intensity)[0]
        fingerprint = np.array(
            [[self.raman_shift[p], self.intensity[p]] for p in peak_indices])
        return fingerprint
