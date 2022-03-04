import csv
import matplotlib.pyplot as plt

header = []
data = []


filename = "100kOhm.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for datapoint in csvreader:

        values = [float(value) for value in datapoint]
        data.append(values)

print(header)
print(data[0])
print(data[1])

frekvens = [p[0] for p in data]
ch1 = [p[1] for p in data]
ch2 = [p[3] for p in data]

plt.plot(frekvens,ch1, frekvens, ch2)
plt.xlabel("frekvens(Hz)")
plt.ylabel("Demping(dB)")
plt.legend(["CH1", "CH2"])
plt.grid(True)
plt.show()

    
