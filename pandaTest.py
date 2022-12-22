
#     https://chat.openai.com/chat

import pandas as pd
import matplotlib.pyplot as plt

# Load the spectral data into a DataFrame
df = pd.read_csv('SolarSpectrumDec21.csv', sep=',', engine='python')

print(df)

# Normalize the flux values
df['flux'] = df['flux'] / df['flux'].max()

# Shift the wavelengths (optional)
#df['wavelength'] = df['wavelength'] - df['wavelength'].min()
plt.style.use('classic') 

plt.xlabel('Wavelength (nm)', fontsize = 20)
plt.ylabel('Relative Intensity', fontsize = 20)
plt.title('Solar Spectrum 12/21/22', fontsize = 40)
plt.xticks([325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900])

# Plot the standardized spectrum
plt.plot(df['wavelength'], df['flux'])

plt.show()
