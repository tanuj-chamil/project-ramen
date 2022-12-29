import numpy as np
import plotly.express as px
import plotly.graph_objects as go
class RamanSpectrum:
    def __init__(self, name, L, I) -> None:
        """initiate RamanSpectrum objcet

        Args:
            L (iterable): raman shift waves of the spectrum
            I (iterable): corresponding intensities to the raman shifts
        """
        self.shift = np.array(L)
        self.raw_intensity = np.array(I)
        self.intensity = self.raw_intensity
        self.name = name
        self.fingerprint = "Normalize to generate the spectral fingerprint"

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
            spectrum = px.line(x=self.shift, y=self.intensity)
            figure = go.Figure(data=spectrum.data+peaks.data)
        else:
            figure = px.line(x=self.shift, y=self.intensity)
        return figure.add_hline(y=0, line_width=1, line_dash="dash", line_color="grey")
