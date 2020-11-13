"""
NOTE: ALL ENTRIES ARE AS STRINGS!

NOTE: All plots are bar graphs and will be changed. More functions will be added for different visualization.
      Function plot_data_usa_can_all() takes roughly 1 min to plot. Code will be modified to reduce time under 10s.

NOTE: Function docstrings are to be modified and preconditions will be added for all if any required.

NOTE: Commented functions will be removed later or completed.

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


def prepare_data(filepath: str) -> Dict[str, List]:
    """
    This function reads through the csv file and returns a mapping of each country to an empty list to prepare the
    data for various computations on each country.

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


# def yearly_temp_can(filepath: str, date: str) -> float:
#     temp_can = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'Canada' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_can, abs(float(row[1])))
#
#         if len(temp_can) != 0:
#             return sum(temp_can) / len(temp_can)
#
#
# def yearly_temp_usa(filepath: str, date: str) -> float:
#     temp_usa = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'United States' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_usa, abs(float(row[1])))
#
#         if len(temp_usa) != 0:
#             return sum(temp_usa) / len(temp_usa)
#
#
# def yearly_temp_bra(filepath: str, date: str) -> float:
#     temp_bra = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'Brazil' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_bra, abs(float(row[1])))
#
#         if len(temp_bra) != 0:
#             return sum(temp_bra) / len(temp_bra)
#
#
# def yearly_temp_aus(filepath: str, date: str) -> float:
#     temp_aus = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'Australia' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_aus, abs(float(row[1])))
#
#         if len(temp_aus) != 0:
#             return sum(temp_aus) / len(temp_aus)
#
#
# def yearly_temp_rus(filepath: str, date: str) -> float:
#     temp_rus = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'Russia' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_rus, abs(float(row[1])))
#
#         if len(temp_rus) != 0:
#             return sum(temp_rus) / len(temp_rus)
#
#
# def yearly_temp_ind(filepath: str, date: str) -> float:
#     temp_ind = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'India' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_ind, abs(float(row[1])))
#
#         if len(temp_ind) != 0:
#             return sum(temp_ind) / len(temp_ind)
#
#
# def yearly_temp_chi(filepath: str, date: str) -> float:
#     temp_chi = []
#     year = date[0:4]
#     with open(filepath) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#         for row in reader:
#             if row[4] == 'China' and row[1] != '' and \
#                     str(datetime.date(int(year), 1, 1)) <= row[0] <= str(datetime.date(int(year), 12, 1)):
#                 list.append(temp_chi, abs(float(row[1])))
#
#         if len(temp_chi) != 0:
#             return sum(temp_chi) / len(temp_chi)
#
#
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

# FUNCTION NOT COMPLETED YET

# def plot_data_greater_average(filepath: str) -> None:
#     """
#     This plot answers notepad qn 3.
#     Function not complete yet.
#
#     """
#     data = all_countries_read(filepath)
#     global_sum = [data[country][i][1] for country in data for i in range(0, len(data[country]))]
#     global_average = sum(global_sum) / len(global_sum)
#
#     # temp_can = []
#     # temp_usa = []
#     # temp_rus = []
#     # temp_ind = []
#     # temp_aus = []
#     # temp_chi = []
#     # temp_bra = []
#     #
#     # with open(filepath) as file:
#     #     reader = csv.reader(file)
#     #
#     #     # Skip header row
#     #     next(reader)
#     #
#     #     list.append(temp_usa, sum(data['United States']) / len(data['United States']))
#     #     list.append(temp_can, sum(data['Canada']) / len(data['Canada']))
#     #     list.append(temp_rus, sum(data['Russia']) / len(data['Russia']))
#     #     list.append(temp_chi, sum(data['China']) / len(data['China']))
#     #     list.append(temp_ind, sum(data['India']) / len(data['India']))
#     #     list.append(temp_bra, sum(data['Brazil']) / len(data['Brazil']))
#     #     list.append(temp_aus, sum(data['Australia']) / len(data['Australia']))
#
#     #  Write for those countries whose temp > global temp (Complete the below code)
#     fig = go.Figure(data=[
#         go.Bar(name='Canada', x=list(range(1990, 2013)), y=avg_temp_can, width=0.6),
#         go.Bar(name='United States', x=list(range(1990, 2013)), y=avg_temp_bra, width=0.4)
#
#     ])
#
#     title = 'Comparison of land temperature between Canada and United States from 1990-2013'
#
#     # Change the bar mode
#     fig.update_layout(barmode='group',
#                       title=title, xaxis_title='Years',
#                       yaxis_title='Average land temperature',
#                       bargap=0.5)
#     fig.show()


def plot_data_mostDev_leastDev(filepath: str) -> None:
    """
    This function plots a graph between the yearly land temperature averages between United States (Most Developed) and
    Brazil (Least Developed) between 1990 - 2012.

    We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
    from which we can later extract relevant data.

    filepath: data/filtered_land_temp.csv
    """
    data = all_countries_read(filepath)

    yearly_temp_bra = [data['Brazil'][i][1] for i in range(0, len(data['Brazil']))]
    yearly_temp_usa = [data['United States'][i][1] for i in range(0, len(data['United States']))]

    fig = go.Figure(data=[
        go.Bar(name='United States (Most Developed)', x=list(range(1990, 2013)), y=yearly_temp_usa, width=0.4),
        go.Bar(name='Brazil (Least Developed)', x=list(range(1990, 2013)), y=yearly_temp_bra, width=0.4)

    ])
    title = 'Comparison of land temperature between United States (Most Developed) and Brazil (Least Developed) ' \
            'from 1990-2012'
    # Change the bar mode
    fig.update_layout(barmode='group',
                      title=title, xaxis_title='Years',
                      yaxis_title='Average land temperature',
                      )
    fig.show()

# FUNCTION WILL BE COMPLETED. CODE MODIFICAITON REQUIRED.

# def plot_data_all(filepath: str) -> None:
#     """
#     This function plots a graph between the yearly land temperature averages between all countries in the csv file
#      between 1990 - 2012. The countries are grouped as Developed and Developing.
#
#     We use the all_countries_read() function to obtain the yearly average of land temperatures for all countries
#     from which we can later extract relevant data.
#     """
#     model = read_csv_data_all(filepath)
#
#     developed_countries = []
#     developed_countries_avg_temp = []
#     developing_countries = []
#     developing_countries_avg_temp = []
#     for key in model:
#         if key in ['Brazil', 'China', 'India', 'Russia']:
#             list.append(developing_countries, key)
#             list.append(developing_countries_avg_temp, sum(model[key]) / len(model[key]))
#         if key in ['Canada', 'United States', 'Australia']:
#             list.append(developed_countries, key)
#             list.append(developed_countries_avg_temp, sum(model[key]) / len(model[key]))
#
#     fig = go.Figure(data=[
#         go.Bar(name='Developed Countries', x=developed_countries, y=developed_countries_avg_temp, width=0.35),
#         go.Bar(name='Developing Countries', x=developing_countries, y=developing_countries_avg_temp, width=0.35)
#     ])
#     title = 'Average land temperatures of Developed and Developing countries from 1990- 2013'
#     # Change the bar mode
#     fig.update_layout(barmode='group',
#                       title=title, xaxis_title='Countries',
#                       yaxis_title='Average land temperature',
#                       bargap=0.5)
#     fig.show()


def plot_data_usa_can_all(filepath: str) -> None:
    """
    This function plots a graph between the yearly land temperature averages between United States, Canada and the
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
