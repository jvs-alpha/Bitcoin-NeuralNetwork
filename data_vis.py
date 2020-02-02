import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv("BCHAIN-AVBLS.csv")
csv_data.plot(kind="line",x="Date",y="Value")
plt.show()
