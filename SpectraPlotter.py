import matplotlib.pyplot as plt
import numpy as np
import csv
  
x = []
y = []
  
with open('AM15GSpectra.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
plt.style.use('dark_background') 
plt.plot(x, y, color = 'r', linestyle=":", linewidth=2)
plt.xticks(np.arange(0, 200, 4))
#plt.yticks(np.arange(0, 3, 1))
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('Solar Spectrum 12/5/22')
plt.annotate('Point', xy=(930,0.2), xytext = (900,0))
plt.show()
