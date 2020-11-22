"""
Our objective is to do the following with the csv data that we have:

- Display:
 1. Show the land temperature of Canada and USA from 1990-2013.
 2. Show the land temperature of United States, Canada and rest of the world form 1990-2013.
 3. Show avg land temperature of various countries from 1990-2013.
 4. Show the land temperature between Most Developed and Least Developed country from 1990-2013.
 5. Show the land temperature between those countries whose land temperature exceeds the global
    average land temperature form 1990-2013.

- Various computations performed within helper functions :
 1. Prepare the data format for all countries with the help of appropriate functions.
 2. Convert the data into relevant data types if needed.
 3. Ignore those data entries whose values are empty.
 4. Extraction of data from a specific period of 1990-2013.
"""
from datetime import datetime
from typing import List, Dict
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import data_handler as dh


def get_avg_by_year(filepath: str, countries: List[str]) -> List[List[float]]:
    """Return a list containing average temperature for every year for every country.

    @param filepath: path of the dataset
    @param countries: countries for which we need the yearly average
    @return: a list containing list for every countries yearly average
    """
    # load the data
    data = dh.read_csv(filepath)
    # remove the unnecessary columns
    data = dh.delete(data, [2, 3])
    # remove the rows with no values
    data = dh.remove_na(data)
    # convert each column to its respective datatype
    data = dh.transform(data, [datetime, float, str], year_only=True)
    # only keep values from year 1990 to 2013
    data = dh.filter_by_value(data, 0, list(range(1990, 2014)))
    # group the data by country
    grouped_data = dh.group_by(data, 2)

    averages = []  #ACCUMILATOR: store the list with yearly average of every country

    for country in countries:
        # extract data for <country> country
        country_data = grouped_data[country]
        # group the data by year an calculate average for that year
        averages.append(dh.calculate_average(country_data, 0, 1)[1])

    return averages


def get_avg_by_country(filepath: str, countries: List[str]) -> Dict[str, float]:
    """Return the average of all the years from 1990 to 2013 land temperature for
    all the countries in a dictionary where country name is mapped to average temperature.

    @param filepath: path to the dataset
    @param countries: countries for which we want the average
    @return: a dict mapping country to its average land temperature
    """
    # load the data
    data = dh.read_csv(filepath)
    # remove the unnecessary columns
    data = dh.delete(data, [2, 3])
    # remove the rows with no values
    data = dh.remove_na(data)
    # convert each column to its respective datatype
    data = dh.transform(data, [datetime, float, str], year_only=True)
    # only keep values from year 1990 to 2013
    data = dh.filter_by_value(data, 0, list(range(1990, 2014)))
    # group the data by country
    grouped_data = dh.group_by(data, 2)

    return_dict = {}  #ACCUMILATOR: store the country and its average

    for country in countries:
        # extracting the data for a country and then calculating the
        # average of average temperature column in the dataset.
        return_dict[country] = dh.calc_avg_col(grouped_data[country], 1)

    return return_dict


def plot_data_can_usa(filepath: str) -> None:
    """This function plots a graph between the yearly land temperature averages between
    United States and Canada between 1990 - 2013.

    @param filepath: path of the dataset
    """

    avg = get_avg_by_year(filepath, ['United States', 'Canada'])

    us, canada = avg
    years = list(range(1990, 2014))

    fig = go.Figure(data=[
        go.Bar(name='United States', x=years, y=us, width=0.4),
        go.Bar(name='Canada', x=years, y=canada, width=0.4)

    ])
    title = 'Comparison of land temperature between Canada and United States from 1990-2013'
    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature (in °C)',
                      bargap=0.5)
    fig.show()

    """"
    In this graph, we visualize the varying land temperature between United States and Canada 
    from 1990- 2013 with a bar plot. We observe that despite both Canada and United States being
    highly developed countries, United States has a much higher land temperature as compared to
    Canada. One of the main reasons for this is the levels of various greenhouse gases in those 
    countries. The emissions of greenhouse gases like Carbon Dioxide, Nitrous Oxide, etc are much
    higher in United States as compared to Canada. Rising levels of greenhouse gases contribute 
    greatly to greenhouse effect which is positively correlated to rising land temperatures. Thus
    we can observe from our graph why United States is much warmer as compared to Canada which is 
    much cooler.
    """


def plot_data_greater_average(filepath: str) -> None:
    """This function plots a modified pie chart between the yearly land temperature averages
    between all countries in the csv file between 1990 - 2013.

   @param filepath: path of the dataset
   """
    countries = ['Brazil', 'India', 'China', 'Australia']
    country_average = list(get_avg_by_country(filepath, countries).values())

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    plt.pie(country_average, labels=countries, explode=[0.05 for _ in range(0, 4)],
            autopct='%.2f%%', shadow=True, startangle=45, colors=colors)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')

    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Average land temperatures of countries that exceed the global land temperatures '
              'from 1990-2013')

    plt.legend(countries, loc="center", prop={"size": 12})
    plt.show()

    """
    In this graph, we plot the varying land temperature between those countries whose land 
    temperature exceeds the global average land temperature of approximately 13.19 with the
    help of pie chart from 1990-2013 in terms of percentage composition. 
    
    We can observe that majority of the countries in this list are developing countries. 
    Developing countries have fewer developed technologies and increasing emission of greenhouse
    gases which show a direct correlation with increasing land temperature. As a result, they do
    not have the adequate resources to combat climate change effectively thus resulting in having
    increasing land temperature over the years. 
    """


def plot_data_mostdev_leastdev(filepath: str) -> None:
    """ This function plots a line-plot between the yearly land temperature averages between
    United States (Most Developed) and Brazil (Least Developed) between 1990 - 2013.

    @param filepath: path of the dataset
    """
    yearly_temp_bra, yearly_temp_usa = get_avg_by_year(filepath, ['Brazil', 'United States'])
    years = list(range(1990, 2014))

    plt.plot(years, yearly_temp_usa, label="United States")
    plt.plot(years, yearly_temp_bra, label="Brazil")

    plt.xlabel('Years')
    plt.ylabel('Average Land Temperature (in °C)')

    plt.fill_between(years, yearly_temp_usa, alpha=0.30, color='red', interpolate=True)
    plt.fill_between(years, yearly_temp_bra, alpha=0.30, color='blue', interpolate=True)

    plt.legend(['United States', 'Brazil'], loc="center right")

    plt.title('Comparison of land temperatures between United States (Most Developed) and Brazil '
              '(Least Developed) FROM 1990- 2012')

    plt.show()

    """
    In this graph, we visualize the varying land temperature changes from 1990-2013 between United 
    States (Most Developed) and Brazil (Least Developed) with the help of line plot. 
    
    Developing countries have fewer developed technologies and increasing emission of greenhouse 
    gases which show a direct correlation with increasing land temperature. As a result, country
    like Brazil which is still developing do not have the adequate resources to combat climate 
    change effectively thus resulting in increasing land temperature over the years. 
    
    United States on the other hand is a much more developed country and thus has comparatively 
    lesser changing land temperatures compared to Brazil.
    """


def plot_data_all(filepath: str) -> None:
    """This function plots a scatter plot between the yearly land temperatures from 1990-2013 of
    all countries whose from the csv file.

    @param filepath: path of the dataset
    """
    countries = ['Brazil', 'India', 'Canada', 'United States', 'Russia', 'Australia', 'China']
    data = get_avg_by_year(filepath, countries)
    years = list(range(1990, 2014))

    for country_data in data:
        plt.scatter(x=years, y=country_data)

    plt.title('Comparison of average global land temperature between various countries from '
              '1990- 2013')

    plt.xlabel('Years')
    plt.ylabel('Average land temperature (in °C)')
    plt.legend(countries, loc='center right', prop={"size": 7})
    plt.show()

    """
    In this graph, we are plotting the yearly average land temperatures between various countries 
    given in our csv file. By visualizing our data through a scatter plot, we can better understand
    the change in temperature between various countries. We can identify which countries have 
    higher land temperature and which ones have lower land temperature. These levels will vary 
    depending on how developed the country is and the developing countries will have a higher land
    temperature compared to the developed countries. This nature of land temperature is evident 
    from our graph.
    """


def plot_data_usa_can_all(filepath: str) -> None:
    """This function plots a bar graph between the yearly land temperature averages between
    United States, Canada and the Rest of the World from the csv file between 1990 - 2013.

    @param filepath: path of the dataset
    """
    countries = ['Brazil', 'India', 'Canada', 'United States', 'Russia', 'Australia', 'China']
    data = get_avg_by_year(filepath, countries)
    years = list(range(1990, 2014))

    yearly_temp_usa = data.pop(3)
    yearly_temp_can = data.pop(2)

    avg_temp_rest_world = [0 for _ in range(len(years))]

    for country_data in data:
        for index in range(len(years)):
            avg_temp_rest_world[index] += country_data[index] / len(data)

    fig = go.Figure(data=[
        go.Bar(name='Canada', x=years, y=yearly_temp_can),
        go.Bar(name='United States', x=years, y=yearly_temp_usa),
        go.Bar(name='Rest of the world', x=years, y=avg_temp_rest_world)
    ])

    title = 'Comparison of land temperature between Canada, United States and Rest of the World ' \
            'from 1990-2013'

    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature (in °C)',
                      bargap=0.4)
    fig.show()

    """
    In this graph, we visualize and compare the changing land temperature between United States, 
    Canada, and the Rest of the world from our csv file with the help of bar chart. We can observe
    that over the years, the land temperature of Canada was low and sometimes negative indicating
    that the land temperatures were low and the country was cooler during this period. However, we
    can observe higher land temperature over the years in United States and the Rest of the World
    indicating they were relatively warm over the years to a varying degree depending on the 
    temperature changes that occurred.
    """
