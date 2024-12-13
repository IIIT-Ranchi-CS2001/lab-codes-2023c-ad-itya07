import numpy as np
import matplotlib.pyplot as plt

# Dataset: Daily COVID-19 cases for 5 countries over 7 days
covid_data = np.array([
    [1500, 2300, 1900, 1800, 900],
    [1600, 2100, 1500, 950, 2000],
    [1700, 2200, 2400, 1000, 1400],
    [1550, 2150, 1950, 1450, 1020],
    [1750, 2250, 2450, 1200, 900],
    [1800, 2800, 2100, 1500, 1050],
    [1900, 2400, 2200, 1600, 1100]
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# 1. Basic Statistics
total_cases = covid_data.sum(axis=0)
print("Total cases for each country:", total_cases)

highest_cases_country = countries[np.argmax(total_cases)]
print("Country with highest total cases:", highest_cases_country)

# 2. Daily Analysis
average_daily_cases = covid_data.mean(axis=1)
print("Average daily cases across all countries:", average_daily_cases)

highest_cases_day = np.argmax(covid_data.sum(axis=1)) + 1
print("Day with the highest total cases across all countries:", highest_cases_day)

# 3. Trends
percentage_change = ((covid_data[1:] - covid_data[:-1]) / covid_data[:-1]) * 100
print("Percentage change in cases from Day 1 to Day 7:\n", percentage_change)

highest_increase_country = countries[np.argmax(percentage_change.max(axis=0))]
print("Country with the highest percentage increase:", highest_increase_country)

# 4. Data Transformation
normalized_data = (covid_data - covid_data.min()) / (covid_data.max() - covid_data.min())
print("Normalized dataset:\n", normalized_data)

# 5. Visualization
# Line chart for daily cases of each country
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country)

# Highlight the day with the highest total cases
day_with_max_cases = np.argmax(covid_data.sum(axis=1)) + 1
plt.axvline(day_with_max_cases, color='red', linestyle='--', label='Highest Total Cases Day')

plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()
plt.show()
