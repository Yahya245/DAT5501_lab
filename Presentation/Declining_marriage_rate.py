import numpy as np
import matplotlib.pyplot as plt

# Data
reasons = np.array([
    'Rise in births outside marriage',
    'Increase in cohabitation',
    'Delayed marriage age',
    'Greater economic independence',
    'Legal recognition of unmarried couples',
    'Cultural acceptance of diverse families'
])
impact_score = np.array([90, 85, 80, 75, 70, 65])  # hypothetical impact scores out of 100

# Create horizontal bar chart
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(reasons, impact_score, color='skyblue')

# Labeling
ax.set_xlabel('Impact Score', fontsize=12)
ax.set_ylabel('Reason', fontsize=12)
ax.set_title('Reasons Marriage Is Declining Despite Steady Birth Rates', fontsize=14)
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()