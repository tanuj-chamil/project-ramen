from find_peaks import detect_peaks
class Spectrum:
    def __init__(self,x,y) -> None:
        self.wavenlength = x
        self.intensity = y
        self.fingerprint = detect_peaks(x,y,threshold=0.20)
    
#fgnrkrvkrvrkv