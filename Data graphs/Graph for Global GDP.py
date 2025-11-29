# As the UAE is and has been one of the rapidly growing economies of the world I have decided to extract just that data
# and create a graph using that information. 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Raw UAE GDP growth data exactly as provided (1960–2023)
data = [
    "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "36.612377853309","39.0796375886666","76.6201550367608","14.4980412677649","6.22740138862785","16.52685650611","21.4393301703121",
    "-1.58960331985861","20.9235730768488","23.8747749106529","4.65917667398332","-6.7193161856808","-4.74582069985286","4.01695127951223",
    "-3.59447651738608","-14.9581365646216","3.38198170911019","-2.61890770379125","12.337891282123","18.3279855336306","0.860081947717788",
    "3.34494485849439","1.26119094566637","6.89614855343777","6.68788645972637","5.79840406919965","8.1903986491688","0.291994342094142",
    "2.90221363963286","10.852704215378","1.39908503706675","2.43345681089617","8.80054081355328","9.56643663767056","4.85514119553352",
    "9.83731976923958","3.18439017324607","3.19183627331816","-5.24292190385027","1.60285004671354","6.21612181664371","1.8244807850986",
    "5.05555965807969","4.16569184064922","6.78677287656618","5.56149075979933","0.735068713941203","1.31391388153578","1.10834813453296",
    "-4.95705243303316","4.35475529659919","7.50969703496445","3.61870653118159","3.76161544553149"
]

# Convert to numeric and drop blanks
values = pd.to_numeric(pd.Series(data), errors="coerce").dropna().reset_index(drop=True)

# Generate matching year numbers
start_year = 1960
years = pd.Series(range(start_year, start_year + len(values)))

# Create tidy dataframe
df = pd.DataFrame({"Year": years, "GDP growth %": values})

# Last 10 years
last_10 = df.tail(10)

# Plot scatter
plt.scatter(last_10["Year"], last_10["GDP growth %"], label="GDP growth (%)")

# Line of best fit
m, b = np.polyfit(last_10["Year"], last_10["GDP growth %"], 1)
plt.plot(last_10["Year"], m*last_10["Year"] + b, label="Line of Best Fit")

# Labels
plt.title("United Arab Emirates — GDP Growth (Annual %) — Last 10 Years")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.grid(True)
plt.legend()
plt.show()


