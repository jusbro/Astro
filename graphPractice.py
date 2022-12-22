import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


wavelength = []
intensity = []
  
with open('SolarSpectrumDec21.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        wavelength.append(float(row[0]))
        intensity.append(float(row[1]))

dx = wavelength/wavelength.max()


dydx = np.gradient(intensity, dx)

#print(wavelength)
print(dydx)
#dydx = wavelength[1] - wavelength[0]
plt.style.use('classic') 
plt.subplot(2,1,1)
plt.plot(wavelength, dydx/intensity, color = 'b', linestyle="-", linewidth=2)

plt.xlabel('Wavelength (nm)', fontsize = 20)
plt.ylabel('Relative Intensity', fontsize = 20)
plt.title('Solar Spectrum 12/21/22', fontsize = 40)
plt.xticks([350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900])

plt.subplot(2,1,2)
plt.plot(wavelength, intensity, color = 'r', linestyle="-", linewidth=2)




plt.xticks([350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900])

plt.annotate('H α', xy=(656.3,0.2), xytext = (650,0.1), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Ca II', xy=(396.8,0.15), xytext = (400,0.05), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Na I', xy=(589.6,0.4), xytext = (589.6,0.2), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Ca II', xy=(393.4,0.15), xytext = (375,0.01), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('H ß', xy=(486.1,0.63), xytext = (486,0.45), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('O (terrestrial)', xy=(759.4,0.1), xytext = (760,0.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('O (terrestrial)', xy=(686.7,0.28), xytext = (687,0.45), arrowprops=dict(facecolor='green', shrink=0.05))




plt.xlabel('Wavelength (nm)', fontsize = 20)
plt.ylabel('Relative Intensity', fontsize = 20)
#plt.title('Solar Spectrum 12/21/22', fontsize = 40)

plt.show()
