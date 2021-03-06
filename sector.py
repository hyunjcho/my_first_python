from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt


sp = SectorPerformances(key='AS0C1JP1LQY65GBK', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()



