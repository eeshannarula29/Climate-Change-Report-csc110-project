"""
Our objective is to do the following with the csv data that we have:
- Display:
 1. Show the land temperature of Canada and USA from 1990-2013.
 2. Show the land temperature of United States, Canada and rest of the world form 1990-2013.
 3. Show avg land temperature of various countries from 1990-2013.
 4. Show the land temperature between Most Developed and Least Developed country from 1990-2013.
 5. Show the land temperature between those countries whose land temperature exceeds the global average land
    temperature form 1990-2013.

- Various computations performed within helper functions :
 1. Prepare the data format for all countries with the help of appropriate functions.
 2. Convert the data into relevant data types if needed.
 3. Ignore those data entries whose values are empty.
 4. Extraction of data from a specific period of 1990-2013.

"""
# Libraries used
import csv
import datetime
from typing import List, Dict, Tuple
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def prepare_data(filepath: str) -> Dict[str, List]:
    """
    This function reads through the csv file and returns a mapping of each country to an empty list to prepare the
    data for computations on each country.

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
    maps each country to a list of tuple of year and yearly average from 1990 to 2013.

    EG: {'Canada': [(1990, 14.5), (1991, 13.2) ], ...}

    We make use of prepare_data() to prepare the dictionary of each country mapped to an empty list.

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
            if year == int(row[0][0:4]) and year <= 2013:
                if row[4] == 'Canada' and row[1] != '':
                    list.append(yearly_can, float(row[1]))
                if row[4] == 'Brazil' and row[1] != '':
                    list.append(yearly_bra, float(row[1]))
                if row[4] == 'Russia' and row[1] != '':
                    list.append(yearly_rus, float(row[1]))
                if row[4] == 'China' and row[1] != '':
                    list.append(yearly_chi, float(row[1]))
                if row[4] == 'India' and row[1] != '':
                    list.append(yearly_ind, float(row[1]))
                if row[4] == 'Australia' and row[1] != '':
                    list.append(yearly_aus, float(row[1]))
                if row[4] == 'United States' and row[1] != '':
                    list.append(yearly_usa, float(row[1]))

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


def read_all_data(filepath: str) -> Dict[str, float]:
    """
    This function calculates the average land temperature between 1990-2013 of all the countries in the csv file and
    returns a dictionary where each country is mapped to its respective global average in the given time frame.

    We make use of all_countries_read() function to help us calculate the global average easily with the help of
    existing yearly average computed and returned by the function.

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
                list.append(temp_rest, float(row[1]))

        if len(temp_rest) != 0:
            return sum(temp_rest) / len(temp_rest)


def plot_data_can_usa(filepath: str) -> None:
    """
        This function plots a graph between the yearly land temperature averages between United States and
        Canada between 1990 - 2013.

        We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
        from which we can later extract relevant data for the required countries.

        filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)
    years = list(range(1990, 2014))

    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]
    yearly_temp_can = [data['Canada'][i][1] for i in range(0, len(data['Canada']))]

    fig = go.Figure(data=[
        go.Bar(name='Canada', x=years, y=yearly_temp_can, width=0.4),
        go.Bar(name='United States', x=years, y=yearly_temp_usa, width=0.4)

    ])
    title = 'Comparison of land temperature between Canada and United States from 1990-2013'
    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature (in °C)',
                      bargap=0.5)
    fig.show()

    """"
    In this graph, we visualize the varying land temperature between United States and Canada from 1990- 2013 with a 
    bar plot. We observe that despite both Canada and United States being highly developed countries, United States 
    has a much higher land temperature as compared to Canada. One of the main reasons for this is the levels of
    various greenhouse gases in those countries. The emissions of greenhouse gases like Carbon Dioxide, Nitrous Oxide, 
    etc are much higher in United States as compared to Canada. Rising levels of greenhouse gases contribute greatly 
    to greenhouse effect which is positively correlated to rising land temperatures. Thus we can observe from our graph
    why United States is much warmer as compared to Canada which is much cooler.
    """


def plot_data_greater_average(filepath: str) -> None:
    """
   This function plots a modified pie chart between the yearly land temperature averages between all countries in the
    csv file between 1990 - 2013.

   We use the read_all_data() function to obtain the global average of land temperatures for the countries.
   """
    model = read_all_data(filepath)
    countries = ['Brazil', 'India', 'China', 'Australia']
    country_average = [model[country] for country in ['Brazil', 'India', 'China', 'Australia']]

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    plt.pie(country_average, labels=countries, explode=[0.05 for _ in range(0, 4)],
            autopct='%.2f%%', shadow=True, startangle=45, colors=colors)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Average land temperatures of countries that exceed the global land temperatures from 1990-2013')
    plt.legend(countries, loc="center", prop={"size": 12})
    plt.show()

    """
    In this graph, we plot the varying land temperature between those countries whose land temperature exceeds the
    global average land temperature of approximately 13.19 with the help of pie chart from 1990-2013 in terms of
    percentage composition. 
    We can observe that majority of the countries in this list are developing countries. 
    Developing countries have fewer developed technologies and increasing emission of greenhouse gases which show a 
    direct correlation with increasing land temperature. As a result, they do not have the adequate 
    resources to combat climate change effectively thus resulting in having increasing land temperature over the years. 
    """


def plot_data_mostdev_leastdev(filepath: str) -> None:
    """
    This function plots a line-plot between the yearly land temperature averages between United States (Most Developed)
    and Brazil (Least Developed) between 1990 - 2013.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data of the countries.

    filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_bra = [data['Brazil'][i][1] for i in range(0, len(data['Brazil']))]
    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]

    y = list(range(1990, 2014))
    plt.plot(y, yearly_temp_usa, label="United States")
    plt.plot(y, yearly_temp_bra, label="Brazil")

    plt.xlabel('Years')
    plt.ylabel('Average Land Temperature (in °C)')

    plt.fill_between(y, yearly_temp_usa, alpha=0.30, color='red', interpolate=True)
    plt.fill_between(y, yearly_temp_bra, alpha=0.30, color='blue', interpolate=True)

    plt.legend(['United States', 'Brazil'], loc="center right")
    plt.title('Comparison of land temperatures between United States (Most Developed) and Brazil (Least Developed) '
              'FROM 1990- 2012')
    plt.show()

    """
    In this graph, we visualize the varying land temperature changes from 1990-2013 between 
    United States (Most Developed) and Brazil (Least Developed) with the help of line plot. 
    Developing countries have fewer developed technologies and increasing emission of greenhouse gases which show a 
    direct correlation with increasing land temperature. As a result, country like Brazil which is still developing 
    do not have the adequate resources to combat climate change effectively thus resulting in increasing 
    land temperature over the years. 
    United States on the other hand is a much more developed country and thus has comparatively lesser changing
    land temperatures compared to Brazil.
    """


def plot_data_all(filepath: str) -> None:
    """
    This function plots a scatter plot between the yearly land temperatures from 1990-2013 of all countries whose
    from the csv file.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data of the countries.

    filepath: data/filtered_land_temp.csv

    """
    model = all_countries_read(filepath)
    countries = [country for country in model]
    years = list(range(1990, 2014))
    bra_data = [model['Brazil'][i][1] for i in range(0, len(model['Brazil']))]
    ind_data = [model['India'][i][1] for i in range(0, len(model['India']))]
    can_data = [model['Canada'][i][1] for i in range(0, len(model['Canada']))]
    usa_data = [model['United States'][i][1] for i in range(0, len(model['United States']))]
    rus_data = [model['Russia'][i][1] for i in range(0, len(model['Russia']))]
    aus_data = [model['Australia'][i][1] for i in range(0, len(model['Australia']))]
    chi_data = [model['China'][i][1] for i in range(0, len(model['China']))]

    plt.scatter(x=years, y=bra_data)
    plt.scatter(x=years, y=ind_data)
    plt.scatter(x=years, y=can_data)
    plt.scatter(x=years, y=usa_data)
    plt.scatter(x=years, y=rus_data)
    plt.scatter(x=years, y=aus_data)
    plt.scatter(x=years, y=chi_data)

    plt.title('Comparison of average global land temperature between various countries from 1990- 2013')
    plt.xlabel('Years')
    plt.ylabel('Average land temperature (in °C)')
    plt.legend(countries, loc='center right', prop={"size": 7})
    plt.show()

    """
    In this graph, we are plotting the yearly average land temperatures between various countries given in our csv file.
    By visualizing our data through a scatter plot, we can better understand the change in temperature between various
    countries. We can identify which countries have higher land temperature and which ones have lower land temperature.
    These levels will vary depending on how developed the country is and the developing countries will have a higher 
    land temperature compared to the developed countries. This nature of land temperature is evident from our graph.
    """


def plot_data_usa_can_all(filepath: str) -> None:
    """
    This function plots a bar graph between the yearly land temperature averages between United States, Canada and the
    Rest of the World from the csv file between 1990 - 2013.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data.

    filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]
    yearly_temp_can = [data['Canada'][i][1] for i in range(0, len(data['Canada']))]
    avg_temp_rest_world = []
    years = list(range(1990, 2014))

    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

    for year in range(1990, 2014):
        list.append(avg_temp_rest_world, yearly_temp_rest(filepath, str(year)))

    fig = go.Figure(data=[
        go.Bar(name='Canada', x=years, y=yearly_temp_can),
        go.Bar(name='United States', x=years, y=yearly_temp_usa),
        go.Bar(name='Rest of the world', x=years, y=avg_temp_rest_world)
    ])

    title = 'Comparison of land temperature between Canada, United States and Rest of the World from 1990-2013'

    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature (in °C)',
                      bargap=0.4)
    fig.show()

    """
    In this graph, we visualize and compare the changing land temperature between United States, Canada, and the Rest of
    the world from our csv file with the help of bar chart. We can observe that over the years, the land temperature of
    Canada was low and sometimes negative indicating that the land temperatures were low and the country was cooler 
    during this period. However, we can observe higher land temperature over the years in United States and the 
    Rest of the World indicating they were relatively warm over the years to a varying degree depending on the 
    temperature changes that occurred.
    """
