import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from model import sheet

target_insta_id = "merumichandayo"
data = sheet.client.open("instaCrawling").worksheet(target_insta_id).get_all_records()

x = [row for row in range(1,len(data)+1)]
weaklyData_y = [row['인스타'] for row in data[-7:]]
monthlyData_y = [row['인스타'] for row in data[-30:]]
annuallyData_y = [row['인스타'] for row in data[-365:]]
wholeData_y = [col['인스타'] for col in data]

plt.plot(x,weaklyData_y,c="r", label = 'weakly')
plt.plot(x,monthlyData_y,c="b", label = 'monthly')
plt.plot(x,annuallyData_y,c="y", label = 'annually')
plt.plot(x,wholeData_y,c="g", label = 'alltime')

plt.xticks(x)
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%iday'))
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%iunit'))
plt.title("Follower Growth")
plt.legend(shadow=True,fancybox=True)
plt.show()
