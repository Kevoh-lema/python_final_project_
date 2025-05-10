# COVID-19 Global Data Tracker
#This project analyzes COVID-19 data globally using real-world data from Our World in Data.
## 1. Data Loading and Preview

import pandas as pd

# Load dataset
df = pd.read_csv("owid-covid-data.csv")
df.head()

## 2. Data Cleaning

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter countries of interest
countries = ['Kenya', 'USA', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing total_cases or total_deaths
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Fill missing numeric values
df.fillna(0, inplace=True)

df.head()

## 3. Exploratory Data Analysis

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.show()


# Plot total deaths over time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.show()


# Plot new daily cases
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)
plt.title("New Daily COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.show()

## 4. Vaccination Progress

# Vaccination Progress Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)
plt.title("COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.show()

## 5. Optional Choropleth Map (requires full dataset)

import plotly.express as px

latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    title="Total COVID-19 Cases by Country")
fig.show()

## 6. Key Insights

#1. USA reports the highest total COVID-19 cases and deaths among the selected countries.
#2. India's vaccination effort ramped up dramatically in 2021.
#3. Kenya saw more gradual increases in both cases and vaccinations.
#4. Death rates spiked during major global surges.
#5. There are noticeable differences in data completeness between countries.
