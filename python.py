import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("all_recs.xlsx - Sheet1.csv", encoding='unicode_escape')

motive_order = df['Motive'].value_counts().index
plt.figure(figsize=(20, 8))
plt.title("Attack Frequency by Motive")
sb.countplot(data=df, y='Motive', color=sb.color_palette()[0], order=motive_order)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

location_order = df['Location'].value_counts().index
plt.figure(figsize=(20, 8))
plt.title("Attack Frequency by Location")
sb.countplot(data=df, y='Location', color=sb.color_palette()[3], order=location_order)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()