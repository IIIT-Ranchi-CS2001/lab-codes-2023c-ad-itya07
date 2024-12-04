import matplotlib.pyplot as plt
import numpy as np

# Q1: Party-wise seat share (Assembly Elections 2023)

# Data
mp_results = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
rj_results = {"BJP": 115, "INC": 69, "BSP": 2, "Others": 13}

# Pie chart for Madhya Pradesh
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(mp_results.values(), labels=mp_results.keys(), autopct='%1.1f%%', explode=[0.1 if v == max(mp_results.values()) else 0 for v in mp_results.values()])
plt.title("Madhya Pradesh - Seat Share")

# Pie chart for Rajasthan
plt.subplot(1, 2, 2)
plt.pie(rj_results.values(), labels=rj_results.keys(), autopct='%1.1f%%', explode=[0.1 if v == max(rj_results.values()) else 0 for v in rj_results.values()])
plt.title("Rajasthan - Seat Share")
plt.tight_layout()
plt.show()

# Bar chart for both states
states = ["MP", "Rajasthan"]
parties = list(mp_results.keys())
bar_width = 0.35
x = np.arange(len(parties))

mp_seats = list(mp_results.values())
rj_seats = list(rj_results.values())

plt.bar(x - bar_width / 2, mp_seats, bar_width, label="MP")
plt.bar(x + bar_width / 2, rj_seats, bar_width, label="Rajasthan")

plt.xticks(x, parties)
plt.xlabel("Party")
plt.ylabel("Seats Won")
plt.title("Seat Distribution by Party")
plt.legend()
plt.show()

# 2nd question
