"""
    NOTE:
    1. ALL ENTRIES ARE AS STRINGS!
    2.  Function docstrings are to be modified and preconditions will be added for all if any required.
    3. References will be added later.
    4. Modify code for plot_data_usa_can_all() and change the plot diagram for plot_data_usa_can()



Our current objective is to do the following with the csv data that we have:
- Display:
 1. Show the land temperature of Canada and USA from 1990- 2012.
 2. Show the land temperature of United States, Canada and rest of the world form 1990-2012
 3. Show avg land temp of 7 countries from 1990-2012.
 4. Show the land temp between Most Dev and Least Dev country from 1990-2012.

- Computations :
 1. Prepare the data format for all countries with the help of appropriate function( use read_all_countries() )
 2. Convert the data into relevant data types if needed.
 3. Ignore those data entries whose values are empty.

"""

import csv
import datetime
from typing import List, Dict, Tuple
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def prepare_data(filepath: str) -> Dict[str, List]:
    """
    This function reads through the csv file and returns a mapping of each country to an empty list to prepare the
    data for Wcomputations on each country.

    filepath: data/filtered_land_temp.csv
    """
    # ACCUMULATOR: List of all countries available from the csv file.
    list_countries = []

    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        for row in reader:
            if row[4] not in list_countries:
                list.append(list_countries, row[4])

    # ACCUMULATOR: Maps each country from the csv file to an empty list.
    model = {}

    for country in list_countries:
        model[country] = []

    return model


def all_countries_read(filepath: str) -> Dict[str, List[Tuple]]:
    """
    This function calculates the yearly average of all countries in the csv file and
    maps each country to a list of tuple of year and yearly average from 1990 to 2012.

    EG: {'Canada': [(1990, 14.5), (1991, 13.2) ], ...}

    Make use of prepare_data() to prepare the dictionary of each country mapped to an empty list.

    filepath: data/filtered_land_temp.csv
    """
    # ACCUMULATOR: To store the data as indicated above.
    data = prepare_data(filepath)
    # To take the initial date to begin calculating our data.
    year = 1990
    # ACCUMULATORS: To store the yearly average of all the countries.
    yearly_can = []
    yearly_aus = []
    yearly_usa = []
    yearly_chi = []
    yearly_bra = []
    yearly_ind = []
    yearly_rus = []
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        for row in reader:
            if year == int(row[0][0:4]) and year <= 2012:
                if row[4] == 'Canada' and row[1] != '':
                    list.append(yearly_can, abs(float(row[1])))
                if row[4] == 'Brazil' and row[1] != '':
                    list.append(yearly_bra, abs(float(row[1])))
                if row[4] == 'Russia' and row[1] != '':
                    list.append(yearly_rus, abs(float(row[1])))
                if row[4] == 'China' and row[1] != '':
                    list.append(yearly_chi, abs(float(row[1])))
                if row[4] == 'India' and row[1] != '':
                    list.append(yearly_ind, abs(float(row[1])))
                if row[4] == 'Australia' and row[1] != '':
                    list.append(yearly_aus, abs(float(row[1])))
                if row[4] == 'United States' and row[1] != '':
                    list.append(yearly_usa, abs(float(row[1])))

            else:
                if len(yearly_can) != 0:
                    list.append(data['Canada'], (year, sum(yearly_can) / len(yearly_can)))
                if len(yearly_usa) != 0:
                    list.append(data['United States'], (year, sum(yearly_usa) / len(yearly_usa)))
                if len(yearly_bra) != 0:
                    list.append(data['Brazil'], (year, sum(yearly_bra) / len(yearly_bra)))
                if len(yearly_rus) != 0:
                    list.append(data['Russia'], (year, sum(yearly_rus) / len(yearly_rus)))
                if len(yearly_aus) != 0:
                    list.append(data['Australia'], (year, sum(yearly_aus) / len(yearly_aus)))
                if len(yearly_ind) != 0:
                    list.append(data['India'], (year, sum(yearly_ind) / len(yearly_ind)))
                if len(yearly_chi) != 0:
                    list.append(data['China'], (year, sum(yearly_chi) / len(yearly_chi)))

                year += 1
                yearly_can = []
                yearly_aus = []
                yearly_usa = []
                yearly_chi = []
                yearly_bra = []
                yearly_ind = []
                yearly_rus = []

    return data


def read_all_data_rounded(filepath: str) -> Dict[str, float]:
    """
    Function returns global average of each country rounded to nearest integer.

    filepath: data/filtered_land_temp.csv
    """

    data = all_countries_read(filepath)
    global_average_countries = prepare_data(filepath)

    for country in data:
        for i in range(0, len(data[country])):
            list.append(global_average_countries[country], data[country][i][1])

    model = {country: round(sum(global_average_countries[country]) / len(global_average_countries[country]))
             for country in global_average_countries}

    return model


def read_all_data(filepath: str) -> Dict[str, float]:
    """
    Function returns global average of each country.

    filepath: data/filtered_land_temp.csv
    """

    data = all_countries_read(filepath)
    global_average_countries = prepare_data(filepath)

    for country in data:
        for i in range(0, len(data[country])):
            list.append(global_average_countries[country], data[country][i][1])

    model = {country: sum(global_average_countries[country]) / len(global_average_countries[country])
             for country in global_average_countries}

    return model


def yearly_temp_rest(filepath: str, date: str) -> float:
    """
    This function calculates the cumulative yearly average of all countries except USA and Canada.

    filepath: data/filtered_land_temp.csv
    """
    temp_rest = []
    year = date[0:4]
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)
        for row in reader:
            if row[4] not in ['United States', 'Canada'] and row[1] != '' and \
                    str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
                list.append(temp_rest, abs(float(row[1])))

        if len(temp_rest) != 0:
            return sum(temp_rest) / len(temp_rest)


def plot_data_can_usa(filepath: str) -> None:
    """
        This function plots a graph between the yearly land temperature averages between United States and
        Canada between 1990 - 2012.

        We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
        from which we can later extract relevant data.

        filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]
    yearly_temp_can = [data['Canada'][i][1] for i in range(0, len(data['Canada']))]

    fig = go.Figure(data=[
        go.Bar(name='Canada', x=list(range(1990, 2012)), y=yearly_temp_can, width=0.6),
        go.Bar(name='United States', x=list(range(1990, 2012)), y=yearly_temp_usa, width=0.4)

    ])
    title = 'Comparison of land temperature between Canada and United States from 1990-2012'
    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature',
                      bargap=0.5)
    fig.show()


def plot_data_greater_average(filepath: str) -> None:
    """
    This function plots a scatter plot between the yearly land temperatures from 1990-2012 of those countries whose
    cumulative yearly average exceeds the global average.

    filepath: data/filtered_land_temp.csv

    """
    model = all_countries_read(filepath)
    countries = ['Brazil', 'India', 'China', 'Australia']

    plt.scatter(x=list(range(1990, 2013)), y=[model['Brazil'][i][1] for i in range(0, len(model['Brazil']))])
    plt.scatter(x=list(range(1990, 2013)), y=[model['India'][i][1] for i in range(0, len(model['India']))])
    plt.scatter(x=list(range(1990, 2013)), y=[model['China'][i][1] for i in range(0, len(model['China']))])
    plt.scatter(x=list(range(1990, 2013)), y=[model['Australia'][i][1] for i in range(0, len(model['Australia']))])
    plt.title('Average land temperatures of countries that exceed the global land temperatures form 1990-2012')
    plt.xlabel('Years')
    plt.ylabel('Average land temperature')
    plt.legend(countries)
    plt.show()


def plot_data_mostDev_leastDev(filepath: str) -> None:
    """
    This function plots a line-plot between the yearly land temperature averages between United States (Most Developed)
    and Brazil (Least Developed) between 1990 - 2012.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data.

    filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_bra = [data['Brazil'][i][1] for i in range(0, len(data['Brazil']))]
    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]

    y = list(range(1990, 2013))
    plt.plot(y, yearly_temp_usa, label="United States")
    plt.plot(y, yearly_temp_bra, label="Brazil")

    plt.xlabel('Years')
    plt.ylabel('Average Land Temperature')

    plt.fill_between(y, yearly_temp_usa, alpha=0.30, color='red', interpolate=True)
    plt.fill_between(y, yearly_temp_bra, alpha=0.30, color='blue', interpolate=True)

    plt.legend(['United States', 'Brazil'], loc="center right")
    plt.title('COMPARISON OF LAND TEMPERATURES BETWEEN UNITED STATES (MOST DEVELOPED) AND BRAZIL (LEAST DEVELOPED) '
              'FROM 1990- 2012')
    plt.show()


def plot_data_all(filepath: str) -> None:
    """
    This function plots a modified pie chart between the yearly land temperature averages between all countries in the
     csv file between 1990 - 2012. The countries are grouped as Developed and Developing.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data.
    """
    model = read_all_data_rounded(filepath)

    countries = [country for country in model]
    global_temp_countries = [model[country] for country in model]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#6ef6ff', '#d982ef', '#ffff80']

    plt.pie(global_temp_countries, labels=countries, explode=[0.05 for _ in range(0, 7)],
            autopct='%.2f%%', shadow=True, startangle=45, colors=colors)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Comparison of average global land temperature between various countries from 1990- 2012')
    plt.legend(countries, loc="center", prop={"size": 10})
    plt.show()


def plot_data_usa_can_all(filepath: str) -> None:
    """
    NOTE: FUNCTION WILL BE MODIFIED BECAUSE IT TAKES CLOSE TO A MINUTE TO PLOT.

    This function plots a bar graph between the yearly land temperature averages between United States, Canada and the
    Rest of the World from the csv file between 1990 - 2012.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data.

    filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]
    yearly_temp_can = [data['Canada'][i][1] for i in range(0, len(data['Canada']))]
    avg_temp_rest_world = []

    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

    for year in range(1990, 2013):
        list.append(avg_temp_rest_world, yearly_temp_rest(filepath, str(year)))

    fig = go.Figure(data=[
        go.Bar(name='Canada', x=list(range(1990, 2013)), y=yearly_temp_can, width=0.7),
        go.Bar(name='United States', x=list(range(1990, 2013)), y=yearly_temp_usa, width=0.5),
        go.Bar(name='Rest of the world', x=list(range(1990, 2013)), y=avg_temp_rest_world, width=0.3)
    ])

    title = 'Comparison of land temperature between Canada, United States and Rest of the World form 1990-2012'

    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature',
                      bargap=0.6)
    fig.show()
