import numpy as np
import matplotlib.pyplot as plt

days = np.array([20,21,24,26,27,28],float)
deaths = np.array([18,17,15,14,16,15],float)

daysplt = np.linspace(days[0], days[-1])
deathsplt = np.array([], float)

for dayp in daysplt:
    deathp = 0
    for dayi, deathi in zip(days,deaths):
        deathp += deathi * np.prod((dayp - days[days != dayi]) / (dayi - days[days != dayi]))
        deathsplt = np.append(deathsplt, deathp)

plt.plot(days,deaths)
plt.xlabel("days")
plt.ylabel("deaths")
plt.show()