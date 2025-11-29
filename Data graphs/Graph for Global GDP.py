# creating a graph for Gloabl GDP 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Load your dataset ===
df = pd.read_csv("Global GDP data.csv")   # Make sure file name matches exactly

# === Sort by year (if not already) ===
df = df.sort_values("Year")

# === Subsample: Keep only the past 10 years ===
last_10_years = df.tail(10)

# Extract values
x = last_10_years["Year"]
y = last_10_years["GDP"]

# === Scatter plot ===
plt.scatter(x, y, label="GDP Observations")

# === Line of best fit ===
coeffs = np.polyfit(x, y, 1)  # slope & intercept for linear regression
best_fit_line = np.poly1d(coeffs)

plt.plot(x, best_fit_line(x), label="Line of Best Fit")

# === Graph labels / formatting ===
plt.title("Global GDP — Past 10 Years")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.grid(True)
plt.legend()
plt.show()

