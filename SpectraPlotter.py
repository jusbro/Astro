import matplotlib.pyplot as plt
import numpy as np
import csv
  
x = []
y = []
  
with open('sunSpectrum.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
plt.style.use('dark_background') 
plt.plot(x, y, color = 'r', linestyle=":", linewidth=2)
plt.xticks(np.arange(1.8, 900, 41))
#plt.yticks(np.arange(0, 3, 1))
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('Solar Spectrum 12/5/22')
#plt.xticks([300,350,400,450,500,550,600,650,700,750,800,850,900])
#plt.annotate('H', xy=(656.3,0.2), xytext = (630,0.3), arrowprops=dict(facecolor='green', shrink=0.05))
#Hydrogen Alpha
#plt.axvline(306.3, color = 'white', label="Hydrogen", linestyle = "--")
#Calcium II
#plt.axvline(396.8, color = 'white', label="Calcium II", linestyle = "--")
#Sodium I
plt.axvline(589.6, color = 'white', label="Sodium I", linestyle = "--")
plt.show()
