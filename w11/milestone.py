import csv

filename = "life-expectancy.csv"

with open(filename) as file:
    reader = csv.reader(file)
    data = list(reader)


header = data[0]
data = data[1:]  # Skip the header row

life_expectancies = []

for row in data:
    country = row[0]
    year = int(row[2])
    life_expectancy = float(row[3])
    life_expectancies.append(life_expectancy)


min_life_expectancy = min(life_expectancies)
max_life_expectancy = max(life_expectancies)

print(f"The lowest life expectancy in the dataset is: {min_life_expectancy}")
print(f"The highest life expectancy in the dataset is: {max_life_expectancy}")


min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_country = min_year = max_country = max_year = None

for row in data:
    country = row[0]
    year = int(row[2])
    life_expectancy = float(row[3])

    if life_expectancy < min_life_expectancy:
        min_life_expectancy = life_expectancy
        min_country = country
        min_year = year

    if life_expectancy > max_life_expectancy:
        max_life_expectancy = life_expectancy
        max_country = country
        max_year = year

print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_year}")


year_of_interest = int(input("Enter the year of interest: "))

year_life_expectancies = []
year_min_life_expectancy = float('inf')
year_max_life_expectancy = float('-inf')
year_min_country = year_max_country = None

for row in data:
    country = row[0]
    year = int(row[2])
    life_expectancy = float(row[3])

    if year == year_of_interest:
        year_life_expectancies.append(life_expectancy)
        
        if life_expectancy < year_min_life_expectancy:
            year_min_life_expectancy = life_expectancy
            year_min_country = country
        
        if life_expectancy > year_max_life_expectancy:
            year_max_life_expectancy = life_expectancy
            year_max_country = country

average_life_expectancy = sum(year_life_expectancies) / len(year_life_expectancies)

print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {average_life_expectancy}")
print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")
