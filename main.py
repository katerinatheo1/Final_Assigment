import matplotlib.pyplot as plt
import numpy as np

percentages = []

for i in range(4):
    percentages.append(np.random.randint(25))

percentages.append(100 - np.sum(percentages))

print(percentages)
