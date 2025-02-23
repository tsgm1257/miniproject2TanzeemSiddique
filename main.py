### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os
import random

os.makedirs("charts", exist_ok=True)

try:
    foods = pd.read_csv("daily_food_nutrition_dataset.csv")
except FileNotFoundError:
    print("Error: daily_food_nutrition_dataset.csv not found.")
    exit()

user_ids = foods['User_ID'].unique()[:100]

random_user_ids = random.sample(list(user_ids), 5)

dfs = []

for user_id in random_user_ids:
    user_data = foods[foods['User_ID'] == user_id]

    meal_calories = user_data.groupby('Meal_Type')['Calories (kcal)'].sum().reset_index()
    meal_calories['User_ID'] = user_id

    dfs.append(meal_calories)

    plt.figure(figsize=(10, 6))
    plt.bar(meal_calories['Meal_Type'], meal_calories['Calories (kcal)'], color=['skyblue', 'lightgreen', 'lightcoral'])
    plt.title(f'User {user_id} - Calories per Meal Type')
    plt.xlabel('Meal Type')
    plt.ylabel('Total Calories (kcal)')
    plt.savefig(f"charts/User_{user_id}_meal_calories.png")
    plt.close()

for df in dfs:
    print("\n" + str(df))