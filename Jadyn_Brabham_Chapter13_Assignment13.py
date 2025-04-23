# Jadyn Brabham
# Chapter 13 Assignment 13
# This program creates a database for the population of 10 Florida cities in 2023,
# then it simulates the growth of the population for the next 20 years.
# Lastly, the program asks the user to input a city ,and it displays a plot
# of the population growth of the city.

import sqlite3
import matplotlib.pyplot as plt

# Function to create the database and insert 2023 data
def create_database():
    conn = sqlite3.connect("population_JB.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('CREATE TABLE IF NOT EXISTS population ('
                   'city TEXT, '
                   'year INTEGER,'
                   'population INTEGER)')

    # Cities in Florida with 2023 populations
    cities = {
        "Jacksonville": 985843,
        "Sarasota": 57602,
        "Tampa": 403364,
        "Orlando": 320742,
        "St. Petersburg": 263553,
        "Port St. Lucie": 245021,
        "Cape Coral": 224455,
        "Bradenton": 57076,
        "Tallahassee": 392645,
        "Fort Lauderdale": 184255
    }

    for city, pop in cities.items():
        cursor.execute("INSERT INTO population (city, year, population)"
                       "VALUES (?, ?, ?)",
                       (city, 2023, pop))

    conn.commit()
    conn.close()

# Function to simulate population growth for 20 years
def simulate_population_growth():
    conn = sqlite3.connect("population_JB.db")
    cursor = conn.cursor()

    # Get all cities and their 2023 population
    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cursor.fetchall()

    for city, pop in rows:
        current_population = pop
        for year in range(2024, 2024+20):
            current_population = int(current_population * 1.02)
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                           (city, year, current_population))

    conn.commit()
    conn.close()

# Function to show population growth plot
def show_population_growth():
    cities = ["Jacksonville", "Sarasota", "Tampa", "Orlando", "St. Petersburg",
              "Port St. Lucie", "Cape Coral", "Bradenton", "Tallahassee", "Fort Lauderdale"]

    print("Choose a ciy from the following list:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("Enter the number of the city: "))
    if choice < 1 or choice > len(cities):
        print("Invalid choice.")
        return

    selected_city = cities[choice - 1]

    conn = sqlite3.connect("population_JB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT year, population FROM population WHERE city = ? "
                   "ORDER BY year", (selected_city,))
    data = cursor.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth of {selected_city} (2023-2043)")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

# Run the program
if __name__ == "__main__":
    create_database()
    simulate_population_growth()
    show_population_growth()