#adding a line of best fit to the orgiginakl divorce graph!!

import numpy as np
import matplotlib.pyplot as plt

# Simulated data
countries = np.array(['Country A', 'Country B', 'Country C', 'Country D', 'Country E',
                      'Country F', 'Country G', 'Country H', 'Country I', 'Country J'])
birth_rate = np.array([2.5, 2.1, 1.8, 1.6, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9])  # births per woman
divorce_rate = np.array([1.5, 1.8, 2.2, 2.5, 2.7, 2.9, 3.0, 3.1, 3.2, 3.3])  # divorces per 1000 people

# Regression line
m, b = np.polyfit(birth_rate, divorce_rate, 1)
regression_line = m * birth_rate + b

# Create plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(birth_rate, divorce_rate, color='blue', label='Countries')

# Annotate each point with country name
for i in range(len(countries)):
    ax.annotate(countries[i], (birth_rate[i], divorce_rate[i]), textcoords="offset points", xytext=(5,-5), ha='left')

# Plot regression line
ax.plot(birth_rate, regression_line, color='red', linestyle='--', label='Regression Line')

# Add labels and title
ax.set_xlabel('Birth Rate (births per woman)', fontsize=12)
ax.set_ylabel('Divorce Rate (divorces per 1000 people)', fontsize=12)
ax.set_title('How Birth Rates Affect Divorce Rates', fontsize=14)
ax.grid(True)
ax.legend()

# Add annotation for inverse relationship
ax.annotate("Inverse relationship:\nHigher birth rates → Lower divorce rates",
            xy=(2.5, 1.5), xytext=(1.5, 2.8),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white'))

plt.tight_layout()
plt.show()