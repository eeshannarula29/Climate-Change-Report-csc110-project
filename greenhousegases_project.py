"""CSC110 Project Greenhouse Gases Visualization from greenhouse_gas_inventory_data_data.csv
By Garv Mohan Sood
"""
import csv
import datetime
from typing import Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Plot1

# https: // www.geeksforgeeks.org / box - plot - in -python - using - matplotlib /

def read_csv_data_boxplot_co2(filepath: str) -> List[List[int]]:
    """
    Reads csv file to extract data for C02 (carbon dioxide) emissions (to make a boxplot) to analyse emission
    data of 2 countries/regions (USA and the European Union)

    Return a list of lists with CO2 (carbon dioxide) emissions of 2 regions (USA and the EU)
    in separate lists from the data mapped from a CSV file.

    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        america_data_so_far = []
        eu_data_so_far = []
        for row in reader:
            # row is a list of strings
            # This extracts the relevant data from row and adds it
            # to the accumulator.
            if row[3] == 'carbon_dioxide_co2_emissions_without_land_use_land_use_change_' \
                         'and_forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'United States of America':
                    list.append(america_data_so_far, float(row[2]))
                if row[0] == 'European Union':
                    list.append(eu_data_so_far, float(row[2]))

        return [america_data_so_far, eu_data_so_far]


def plot_csv_data_boxplot_co2(filepath: str) -> None:
    """
    Uses read_csv_data_boxplot_co2() to read data and plots 2 boxplots showing amount of
        carbon dioxide (CO2) emissions (million tonnes) in
        USA and the European Union over all the years (from 1990 to 2014)
    """
    data = read_csv_data_boxplot_co2(filepath)

    x1 = np.array(data[0])  # value of CO2 emissions in the USA
    x2 = np.array(data[1])  # value of CO2 emissions in the EU

    # The most simple boxplot
    plt.boxplot(x1)
    plt.show()

    # Changing some of its features
    plt.boxplot(x1, notch=False, sym="o")  # sym="o" to shown outliers in data
    plt.show()

    # Showing multiple boxplots on the same window
    plt.boxplot((x1, x2), notch=False, sym="o", labels=["America", "European Union"])

    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in million kilotonnes) from 1990 - 2014 ", fontsize=9)
    plt.title("Aggregated Carbon Dioxide emissions for 2 regions", fontsize=10, fontweight="bold")
    plt.show()

########################################################################################################################
# Plot2

# https: // www.geeksforgeeks.org / box - plot - in -python - using - matplotlib /


def read_csv_data_notched_boxplot_ghgs(filepath: str) -> List[List[int]]:
    """
    Reads csv file to extract data for greenhouse gas (ghgs) emissions (to make a  notched boxplot) to analyse emission
    data of 2 countries (Canada and France)

    Return a list of lists with greenhouse gas (ghgs) emissions of 2 regions (Canada and France)
    in separate lists from the data mapped from a CSV file.

    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        canada_data_so_far = []
        france_data_so_far = []
        for row in reader:
            # row is a list of strings
            # This extracts the relevant data from row and adds it
            # to the accumulator.
            if row[3] == 'greenhouse_gas_ghgs_emissions_without_land_use_land_use_change_' \
                         'and_forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'Canada':
                    list.append(canada_data_so_far, float(row[2]))
                if row[0] == 'France':
                    list.append(france_data_so_far, float(row[2]))

        return [canada_data_so_far, france_data_so_far]


def plot_csv_data_notched_boxplot_ghgs(filepath: str) -> None:
    """
        Uses read_csv_data_notched_boxplot_ghgs() to read data and plots 2 notched boxplots showing amount of
            greenhouse gas emissions (ghgs) (kilotonnes) in
            USA and France over all the years (from 1990 to 2014)
        """
    data = read_csv_data_notched_boxplot_ghgs(filepath)

    x1 = np.array(data[0])  # value of greenhouse gas emissions in the USA
    x2 = np.array(data[1])  # value of greenhouse gas emissions in France

    # The most simple boxplot
    plt.boxplot(x1)
    plt.show()

    # Changing some of its features
    plt.boxplot(x1, notch=True, sym="o")  # sym="o" to shown outliers in data
    plt.show()

    # Showing multiple boxplots on the same window
    plt.boxplot((x1, x2), notch=True, sym="o", labels=["America", "European Union"])

    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in million kilotonnes) from 1990 - 2014 ", fontsize=9)
    plt.title("Notched boxplot with Aggregated Greenhouse Gas emissions for 2 regions", fontsize=10, fontweight="bold")
    plt.show()

########################################################################################################################
# Plot3

# https: // www.geeksforgeeks.org / box - plot - in -python - using - matplotlib /


def read_csv_data_boxplot_all_countries_year(filepath: str) -> List[List[int]]:
    """
        Reads csv file to extract data of nitrogen triflouride (TF3) emissions for all countries for each year
        between 2010 and 2014 (to make a boxplot) of 3 countries/regions (USA, Canada and the European Union)

        Return a list of lists with year-wise emissions of TF3 from all countries
        in separate lists from the data mapped from a CSV file.

        """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        data_so_far2010 = []
        data_so_far2011 = []
        data_so_far2012 = []
        data_so_far2013 = []
        data_so_far2014 = []
        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it
            # to the accumulator.
            if row[3] == 'nitrogen_trifluoride_nf3_emissions_in_kilotonne_co2_equivalent':
                if row[1] == '2010':
                    list.append(data_so_far2010, float(row[2]))
                if row[1] == '2011':
                    list.append(data_so_far2011, float(row[2]))
                if row[1] == '2012':
                    list.append(data_so_far2012, float(row[2]))
                if row[1] == '2013':
                    list.append(data_so_far2013, float(row[2]))
                if row[1] == '2014':
                    list.append(data_so_far2014, float(row[2]))

        return [data_so_far2010, data_so_far2011, data_so_far2012, data_so_far2013, data_so_far2014]


def plot_all_countries_data_peryear_boxplot(filepath: str) -> None:
    """
    Uses read_csv_data_boxplot_all_countries_year() to read data and plots 5 boxplots showing amount of
        nitrogen triflouride (NF3) emissions (kilotonnes) in
        all countries taken together over the years 2010, 2011, 2012, 2013 and 2014
    """
    data = read_csv_data_boxplot_all_countries_year(filepath)
    x1 = np.array(data[0])  # NF3 emissions for all countries in 2010
    x2 = np.array(data[1])  # NF3 emissions for all countries in 2011
    x3 = np.array(data[2])  # NF3 emissions for all countries in 2012
    x4 = np.array(data[3])  # NF3 emissions for all countries in 2013
    x5 = np.array(data[4])  # NF3 emissions for all countries in 2014

    # The most simple boxplot
    plt.boxplot(x1)
    plt.show()

    # Changing some of its features
    plt.boxplot(x1, notch=False, sym="o")  # Use sym="" to shown no fliers; also showfliers=False
    plt.show()
    axes = plt.gca()
    axes.set_ylim([0, 250])  # setting range of y axis

    # Showing multiple boxplots on the same window
    plt.boxplot((x1, x2, x3, x4, x5), notch=False, sym="o", labels=["2010", "2011", "2012", "2013", "2014"])
    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in kilotonnes) ", fontsize=9)
    plt.title("Aggregated Carbon Dioxide emissions for 5 years (from all countries) ", fontsize=10, fontweight="bold")
    plt.show()

########################################################################################################################
# Plot4

#  https: // www.kite.com / python / answers / how - to - color - a - scatter - plot - by - category - using - matplotlib - in -python


def read_csv_data_scatter_co2(filepath: str) -> List[List[int]]:
    """
      Reads csv file to extract data for C02 (carbon dioxide) emissions (to make a scatterplot) to analyse emission
    data of 3 countries/regions (USA, Canada and the European Union)

      Return a list of lists with CO2 (carbon dioxide) emissions of 3 regions (USA, Canada and the EU)
      in separate lists from the data mapped from a CSV file.

      """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        data_so_far = []
        country_so_far = []
        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it
            # to the accumulator.
            if row[3] == 'carbon_dioxide_co2_emissions_without_land_use_land_use' \
                         '_change_and_forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'Canada':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'Canada')
                if row[0] == 'United States of America':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'United States of America')
                if row[0] == 'European Union':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'European Union')

        return [data_so_far, country_so_far]


def plot_csv_data_scatter_co2(filepath: str) -> None:
    """
    Uses read_csv_data_scatter_co2() to read data and it plots a scatterplot showing amount of
    carbon dioxide (CO2) emissions (kilotonnes) in
    USA, Canada and the European Union each year (between 1990 and 2014)
    """
    data = read_csv_data_scatter_co2(filepath)
    y = data[0]  # emission data
    labels = data[1]  # list of countries
    x = 3 * [year for year in range(1990, 2015)]

    data = pd.DataFrame({"X Value": x, "Y Value": y, "Category": labels})

    groups = data.groupby("Category")  # to group the data by region/country

    for name, group in groups:
        plt.plot(group["X Value"], group["Y Value"], marker="o", linestyle="-", label=name)
    plt.xlabel("Years", fontsize=15)
    plt.ylabel("Emissions of Gases (in million  kilotonnes)", fontsize=15)
    plt.title("Carbon Dioxide emissions each year")
    plt.legend()


########################################################################################################################
# Plot5


#  https: // www.kite.com / python / answers / how - to - color - a - scatter - plot - by - category - using - matplotlib - in -python


def read_csv_data_scatter_n2o(filepath: str) -> List[List[int]]:
    """
      Reads csv file to extract data for N2O (nitrous oxide) emissions (to make a scatterplot) to analyse emission
    data of 3 countries/regions (USA, Canada and the European Union)

      Return a list of lists with N2O (nitrous oxide) emissions of 3 regions (USA, Canada and the EU)
      in separate lists from the data mapped from a CSV file.

      """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        data_so_far = []
        country_so_far = []
        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it
            # to the accumulator.
            if row[3] == 'nitrous_oxide_n2o_emissions_without_land_use_land_use_' \
                         'change_and_forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'Canada':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'Canada')
                if row[0] == 'United States of America':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'United States of America')
                if row[0] == 'European Union':
                    list.append(data_so_far, float(row[2]))
                    list.append(country_so_far, 'European Union')

        return [data_so_far, country_so_far]


def plot_csv_data_scatter_n2o(filepath: str) -> None:
    """
        Uses read_csv_data_scatter_n2o() to read data and plots a scatterplot showing amount of
        nitrous oxide (N2O) emissions (kilotonnes) in
        USA, Canada and the European Union each year (between 1990 and 2014)
        """
    data = read_csv_data_scatter_n2o(filepath)
    y = data[0]  # emission data
    labels = data[1]  # list of countries
    x = 3 * [year for year in range(1990, 2015)]

    data = pd.DataFrame({"X Value": x, "Y Value": y, "Category": labels})

    groups = data.groupby("Category")  # to group the data by region/country

    for name, group in groups:
        plt.plot(group["X Value"], group["Y Value"], marker="o", linestyle="-", label=name)
    plt.xlabel("Years", fontsize=15)
    plt.ylabel("Emissions of Gases (in kilotonnes)", fontsize=15)
    plt.title("Nitrous Oxide emissions each year")
    plt.legend()

########################################################################################################################
# Plot6

# https: // plotly.com / python / box - plots /


def read_csv_data_plotly_scatterboxplot(filepath: str) -> List[List[int]]:
    """
    Reads csv file to extract data for C02 (carbon dioxide) emissions (to make a boxplot with a scatterplot)
    to analyse emission data of 3 sparsely populated countries (Austria, Belarus and Bulgaria)

    Return a list of lists with CO2 (carbon dioxide) emissions of 2 countries (Austria, Belarus and Bulgaria)
    in separate lists from the data mapped from a CSV file.

    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        austria_data_so_far = []
        belarus_data_so_far = []
        bulgaria_data_so_far = []
        for row in reader:
            # row is a list of strings
            # This extracts the relevant data from row and adds it
            # to the accumulator.
            if row[3] == 'carbon_dioxide_co2_emissions_without_land_use_land_use_change_' \
                         'and_forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'Austria':
                    list.append(austria_data_so_far, float(row[2]))
                if row[0] == 'Belarus':
                    list.append(belarus_data_so_far, float(row[2]))
                if row[0] == 'Bulgaria':
                    list.append(bulgaria_data_so_far, float(row[2]))

        return [austria_data_so_far, belarus_data_so_far, bulgaria_data_so_far]


def plot_csv_data_plotly_scatterboxplot_sparsely_pop(filepath: str) -> None:
    """
            Uses read_csv_data_plotly_scatter_boxplot() to read data and plots a scatterplot and a box plot together
            showing distribution of amount of carbon dioxide (CO2) emissions (kilotonnes) in
            Austria, Belarus and Bulgaria in the 24 year period (between 1990 and 2014).
            The scatterplot shows each year's emissions data for the 3 aforementioned countries
            and the boxplot aggregates and visualizes this data.
            """
    import plotly.graph_objects as go

    x_data = ['Austria', 'Belarus', 'Bulgaria']
    data = read_csv_data_plotly_scatterboxplot(filepath)

    y0 = data[0]
    y1 = data[1]
    y2 = data[2]

    y_data = [y0, y1, y2]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
              'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)']

    fig = go.Figure()

    for xd, yd, cls in zip(x_data, y_data, colors):
        fig.add_trace(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls)
        )

    fig.update_layout(
        title='Carbon Dioxide (CO2) Emissions in kilotonnes for 3 sparsely populated countries (from 1990 - 2014)',
        margin=dict(
            l=40,
            r=30,
            b=80,
            t=100,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
        showlegend=False
    )

    fig.show()

########################################################################################################################
# Plot7

# https: // plotly.com / python / box - plots /


def read_csv_data_plotly_scatter_boxplot_1990_2014(filepath: str) -> List[List[int]]:
    """
    Reads csv file to extract data for hydrofluorocarbon (hfcs) emissions (to make a boxplot with a scatterplot)
    to analyse emission data in 1990, 2002 and 2014 (in all countries taken together).

    Return a list of lists with hydrofluorocarbon (hfcs) emissions in 1990, 2002 and 2014
    in separate lists from the data mapped from a CSV file.

    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        data_so_far_1990 = []
        data_so_far_2002 = []
        data_so_far_2014 = []
        for row in reader:
            # row is a list of strings
            # This extracts the relevant data from row and adds it
            # to the accumulator.
            if row[3] == 'hydrofluorocarbons_hfcs_emissions_in_kilotonne_co2_equivalent':
                if row[1] == '1990':
                    list.append(data_so_far_1990, float(row[2]))
                if row[1] == '2002':
                    list.append(data_so_far_2002, float(row[2]))
                if row[1] == '2014':
                    list.append(data_so_far_2014, float(row[2]))

        return [data_so_far_1990, data_so_far_2002, data_so_far_2014]


def plot_csv_data_scatter_boxplot_1990_2014(filepath: str) -> None:
    """
                Uses read_csv_data_plotly_scatter_boxplot_1990_2014() to read data and plots a scatterplot and a
                box plot together showing distribution of hydrofluorocarbon (hfcs) emissions in 1990, 2002 and 2014
                (in all countries taken together).
                The scatterplot shows each country's emissions data for the 3 aforementioned years and the boxplot
                aggregates and visualizes this data.
                """
    import plotly.graph_objects as go

    x_data = ['1990', '2002', '2014']
    data = read_csv_data_plotly_scatter_boxplot_1990_2014(filepath)

    y0 = data[0]
    y1 = data[1]
    y2 = data[2]

    y_data = [y0, y1, y2]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
              'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)']

    fig = go.Figure()

    for xd, yd, cls in zip(x_data, y_data, colors):
        fig.add_trace(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls)
        )

    fig.update_layout(
        title='Hydrofluorocarbon (hfcs) Emissions in kilotonnes by all countries (aggregated together) for 1990, 2002, 2014 ',
        margin=dict(
            l=40,
            r=30,
            b=80,
            t=100,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
        showlegend=False
    )

    fig.show()

########################################################################################################################
# Plot8


def read_csv_data_bargraph(filepath: str) -> List[List[int]]:
    """
    Reads csv file to extract data for methane emissions (to make a  grouped bargraph) to analyse emission
    data of 2 countries/regions (EU and France)

    Return a list of lists with methane emissions of 2 regions (EU and France)
    in separate lists from the data mapped from a CSV file.

    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators
        eu_data_so_far = []
        france_data_so_far = []
        for row in reader:
            # row is a list of strings
            # This extracts the relevant data from row and adds it
            # to the accumulator.
            if row[3] == 'methane_ch4_emissions_without_land_use_land_use_change_and_' \
                         'forestry_lulucf_in_kilotonne_co2_equivalent':
                if row[0] == 'European Union':
                    list.append(eu_data_so_far, float(row[2]))
                if row[0] == 'France':
                    list.append(france_data_so_far, float(row[2]))

        return [france_data_so_far, eu_data_so_far]


def plot_csv_data_bargraph(filepath: str) -> None:
    """
    Uses read_csv_data_bargraph() to read data and plots a grouped bargraph with methane emissions in the
    European Union and France. It also shows the methane emissions inthe European Union minus those from France.
    The bargraph resulting from this function shows data for years 1990 -2014.
    """
    data = read_csv_data_bargraph(filepath)
    years = [x for x in range(1990, 2014)]
    fig = go.Figure(data=[
        go.Bar(name='Methane emissions in France ', x=years, y=data[0]),
        go.Bar(name='Methane emissions in the EU other than France', x=years, y=data[1]),

    ])
    title = f' Model: Methane emissions of France in comparison with Methane emissions of the European Union ' \
            f'(share of methane emissions of France compared to the rest of the EU'
    fig.update_layout(barmode='stack',
                      title=title,
                      xaxis_title='Years',
                      yaxis_title='Methane Emissions (in kilotonnes)')
    fig.show()

