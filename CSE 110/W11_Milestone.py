import csv

# Put the CSV file in the same directory as this Python script


def load_data(filename):
    """
    Load data from the CSV file and return a list of dictionaries.
    Each dictionary represents a row in the dataset.
    """
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def find_lowest_highest_life_expectancy(data):
    """
    Find the lowest and highest life expectancies in the dataset.
    """
    lowest = float('inf')
    highest = float('-inf')
    lowest_country = ""
    highest_country = ""
    for row in data:
        life_expectancy = float(row['Period life expectancy at birth - Sex: all - Age: 0'])
        country = row['Entity']
        if life_expectancy < lowest:
            lowest = life_expectancy
            lowest_country = country
        if life_expectancy > highest:
            highest = life_expectancy
            highest_country = country
    return lowest, lowest_country, highest, highest_country

def find_average_life_expectancy(data, year):
    """
    Find the average life expectancy for a given year.
    """
    total_life_expectancy = 0
    count = 0
    min_life_expectancy = float('inf')
    min_country = ""
    max_life_expectancy = float('-inf')
    max_country = ""
    for row in data:
        if int(row['Year']) == year:
            life_expectancy = float(row['Period life expectancy at birth - Sex: all - Age: 0'])
            total_life_expectancy += life_expectancy
            count += 1
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = row['Entity']
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = row['Entity']
    if count == 0:
        return None, None, None, None
    average = total_life_expectancy / count
    return average, min_country, min_life_expectancy, max_country, max_life_expectancy

def main():
    # Load data from the CSV file
    filename = r'C:\Users\jacob\Documents\VSCode for School\CSE 110\life-expectancy.csv'    
    data = load_data(filename)

    # Find lowest and highest life expectancies
    lowest, lowest_country, highest, highest_country = find_lowest_highest_life_expectancy(data)
    print("Lowest life expectancy in the dataset:", lowest, "from", lowest_country)
    print("Highest life expectancy in the dataset:", highest, "from", highest_country)

    # Allow the user to input a year
    year = int(input("Enter the year of interest: "))

    # Find average life expectancy for the given year
    average, min_country, min_life_expectancy, max_country, max_life_expectancy = find_average_life_expectancy(data, year)
    if average is not None:
        print("\nFor the year", year, ":")
        print("The average life expectancy across all countries was:", average)
        print("The max life expectancy was in", max_country, "with", max_life_expectancy)
        print("The min life expectancy was in", min_country, "with", min_life_expectancy)
    else:
        print("No data available for the year", year)

if __name__ == "__main__":
    main()