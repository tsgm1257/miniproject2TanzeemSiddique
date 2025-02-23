### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 1

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

foods = pd.read_csv("daily_food_nutrition_dataset.csv", index_col=0)

print(foods.head())

# plt.savefig(f"charts/{ticker}.png")