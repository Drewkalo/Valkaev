import numpy as np
import matplotlib.pyplot as plt

with open("C:/Users/dinos/Desktop/homework/sem_2/data.txt", 'r') as data:
    data_set = np.array([float(i) for i in data.read().split("\n")])
with open("C:/Users/dinos/Desktop/homework/sem_2/settings.txt", 'r') as settings:
    sett_set = np.array([float(i) for i in settings.read().split("\n")])


voltage = data_set * sett_set[0]
time = np.arange(0, round(sett_set[1] * (len(data_set) -1), 3), sett_set[1])

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

ax.plot(time, voltage, label=f'U(t)', color='purple', linestyle='-', marker='o', markersize=5, markevery = 15)
y_min = np.min(voltage)
y_max = np.max(voltage)
x_min = np.min(time)
x_max = np.max(time)
ax.set_ylim(y_min - 0.1, y_max + 0.1) 
ax.set_xlim(x_min, x_max)


ax.set_xlabel('Время (с)')
ax.set_ylabel('Напряжение (В)')


title_text = "Зависимость напряжения от времени\nв процессе зарядки и разрядки конденсатора"
ax.set_title(title_text, loc='center', wrap=True)


ax.grid(True, linestyle=':', color='gray', alpha=0.9)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', color='lightgray', alpha=0.8)


text_str = f"Длительность эксперимента: {round(sett_set[1] * len(data_set), 2)} с\nШаг квантования: {sett_set[0]} В\nВремя зарядки: {round(384 * sett_set[1], 2)} c\nВремя разрядки: {round((514) * sett_set[1], 2)} c"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
ax.text(7, 3, text_str,  fontsize=10, verticalalignment='top', bbox=props)

ax.legend()
plt.savefig("voltage(time).svg")
plt.show()
