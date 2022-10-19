import spectrum as s
import csv_read
import matplotlib.pyplot as plt

file_path = "databases\csv\cytosine.csv"
data = csv_read.get_data(file_path)

molecule =  s.Spectrum(*data)

plt.plot(molecule.wavenlength,molecule.intensity)
plt.plot(*molecule.fingerprint,"xr")
plt.show()

print(molecule.fingerprint)