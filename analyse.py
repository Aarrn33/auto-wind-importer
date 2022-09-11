import os
import json
import matplotlib.pyplot as plt

# Gets every json (data) file in the current directory
files = [i for i in os.listdir('.') if i[-5:] == ".json" and i[0:13] == "wind_villers_"]
# Makes a dictionnary with all the data
data = {}
for i in files:
    day = i[13:23]
    with open(i, "r") as file:
        day_data = json.load(file)
    data[day] = day_data

# Gets the data for every hour in the current day (no mid-term prevision)
x = []
y = []
for i in list(data.values()):
    for place, j in enumerate(i["hours"]):
        if place < 24:
            x.append(j["time"][0:13])
            y.append(j["windSpeed"]["sg"])

# Plots the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Changes the label's name
x_labels = []
for place, i in enumerate(x):
    if place in range(0, len(x), 168):
        x_labels.append(i[0:10])
plt.xticks(range(0, len(x), 168), x_labels, ha="right", rotation=45)

# Adds margin for the rotated labels
plt.subplots_adjust(bottom=0.20, left=0.15)

# Saves the final plot
plt.savefig("wind_villers.png")

# Shows the plot
plt.show()
