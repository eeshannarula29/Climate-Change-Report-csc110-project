"""This file is used for the visualization of the trends in Greenhouse Gases
and carbon emissions.

Resources:
- https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
- https://www.kite.com/python/answers/how-to-color-a-scatter-plot-by-category-using-matplotlib-in-python
- https://plotly.com/python/box-plots/

TODO:
- check for wrong country labels on the graph
- remove "using read_csv..." from the docstrings
- add or delete graphs on their relevance and if we could make a question of of the graph
- rewrite docstrings and explain what we want to do with the graph, and add @param and @return
"""

from typing import List
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from data_handler import read_csv_and_transform, filter_by_value, group_by, extract_column


def data_by_tags_and_country_or_year(filepath: str,
                                     tags: List[str],
                                     countries_or_years: list,
                                     country_or_year: int) -> List[List[float]]:
    """The function would take in the filepath of the dataset from which it would extract the data
    covert every variable in the row into its appropriate datatype and then filter out the data
    containing only the tags we want, and only for the countries or years we want, and then return emission values
    separately for all the countries or years.

    @param filepath: the path of the dataset
    @param tags: list of all the categories of emissions we want in the data
    @param countries_or_years: The countries or years for which we want the data
    @param country_or_year: 0 or 1 based on if we want to categorise by country or year
    @return: Return a list containing lists for every countries emission value
    """

    # extract dataset and covert all variables into their respective datatype
    data = read_csv_and_transform(filepath, [str, int, float, str])

    # keeping rows with tags we want
    data = filter_by_value(data, 3, tags)

    # splitting by countries
    grouped_data = group_by(data, country_or_year)

    # Extracting emission values for the countries we want to analyze
    countries_so_far = []

    for county in countries_or_years:
        county_data = grouped_data[county]
        countries_so_far.append(extract_column(county_data, 2))

    return countries_so_far


def data_by_tags(filepath: str,
                 tags: List[str],
                 country_filter: List[str] = None,
                 year_filter: List[int] = None) -> List[List]:
    """The function would take in the filepath of the dataset from which it would extract the data
    covert every variable in the row into its appropriate datatype and then filter out the data
    containing only the tags we want, and return the emission values along side the respective
    country and year.

    We can pass in optional lists to only get rows with specific coutry or year

    @param filepath: the path of the dataset
    @param tags: list of all the categories of emissions we want in the data
    @param country_filter: list of countries we want data for
    @param year_filter: list of years we want data for
    @return: Return a list with emission value alongside the respective country and year
    """

    # extract dataset and covert all variables into thir respective datatype
    data = read_csv_and_transform(filepath, [str, int, float, str])

    # keeping rows with tags we want
    data = filter_by_value(data, 3, tags)

    # filtering countries and years
    if country_filter:
        data = filter_by_value(data, 0, country_filter)
    if year_filter:
        data = filter_by_value(data, 1, year_filter)

    # extract the values and countries
    values = extract_column(data, 2)
    countries = extract_column(data, 0)
    year = extract_column(data, 1)

    return [values, countries, year]


# Plot1
def plot_csv_data_boxplot_co2(filepath: str) -> None:
    """Uses read_csv_data_boxplot_co2() to read data and plots two
    boxplots showing amount of carbon dioxide (CO2) emissions (million
    tonnes) in USA and the European Union over all the years (from 1990
    to 2014)
    """
    countries = ['United States of America', 'European Union']

    tags = ['carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, countries, 0)

    x1 = np.array(data[0])  # value of CO2 emissions in the USA
    x2 = np.array(data[1])  # value of CO2 emissions in the EU

    plt.boxplot((x1, x2), notch=False, sym="o", labels=["America", "European Union"])

    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in million kilotonnes) from 1990 - 2014 ", fontsize=9)
    plt.title("Aggregated Carbon Dioxide emissions for 2 regions", fontsize=10, fontweight="bold")
    plt.show()


# Plot2
def plot_csv_data_notched_boxplot_ghgs(filepath: str) -> None:
    """Uses read_csv_data_notched_boxplot_ghgs() to read data and
    plots 2 notched boxplots showing amount of greenhouse gas emissions
    (ghgs) (kilotonnes) in Canada and France over all the years (from 1990 to 2014)
    """

    countries = ['Canada', 'France']

    tags = ['greenhouse_gas_ghgs_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, countries, 0)

    x1 = np.array(data[0])  # value of greenhouse gas emissions in the USA
    x2 = np.array(data[1])  # value of greenhouse gas emissions in France

    plt.boxplot((x1, x2), notch=True, sym="o", labels=["Canada", "France"])

    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in million kilotonnes) from 1990 - 2014 ", fontsize=9)
    plt.title("Notched boxplot with Aggregated Greenhouse Gas emissions for 2 regions", fontsize=10, fontweight="bold")
    plt.show()


# Plot3
def plot_all_countries_data_peryear_boxplot(filepath: str) -> None:
    """ Uses read_csv_data_boxplot_all_countries_year() to read data
    and plots 5 boxplots showing amount of nitrogen triflouride (NF3)
    emissions (kilotonnes) in all countries taken together over the
    years 2010, 2011, 2012, 2013 and 2014
    """

    years = [2010, 2011, 2012, 2013, 2014]

    tags = ['nitrogen_trifluoride_nf3_emissions_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, years, 1)
    x1 = np.array(data[0])  # NF3 emissions for all countries in 2010
    x2 = np.array(data[1])  # NF3 emissions for all countries in 2011
    x3 = np.array(data[2])  # NF3 emissions for all countries in 2012
    x4 = np.array(data[3])  # NF3 emissions for all countries in 2013
    x5 = np.array(data[4])  # NF3 emissions for all countries in 2014

    plt.boxplot((x1, x2, x3, x4, x5), notch=False, sym="o", labels=["2010", "2011", "2012", "2013", "2014"])
    plt.xlabel("Region/Country", fontsize=15)
    plt.ylabel("Aggregated Emissions of Gases (in kilotonnes) ", fontsize=9)
    plt.title("Aggregated Carbon Dioxide emissions for 5 years (from all countries) ", fontsize=10, fontweight="bold")
    plt.show()


# Plot4
def plot_csv_data_scatter_co2(filepath: str) -> None:
    """Uses read_csv_data_scatter_co2() to read data and it
    plots a scatterplot showing amount of carbon dioxide (CO2)
    emissions (kilotonnes) in USA, Canada and the European Union
    each year (between 1990 and 2014)
    """

    countries = ['Canada', 'United States of America', 'European Union']

    tags = ['carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags(filepath, tags, country_filter=countries)

    y = data[0]  # emission data
    labels = data[1]  # list of countries
    x = data[2]  # list of years

    data = pd.DataFrame({"X Value": x, "Y Value": y, "Category": labels})

    groups = data.groupby("Category")  # to group the data by region/country

    for name, group in groups:
        plt.plot(group["X Value"], group["Y Value"], marker="o", linestyle="-", label=name)

    plt.xlabel("Years", fontsize=15)
    plt.ylabel("Emissions of Gases (in million  kilotonnes)", fontsize=15)
    plt.title("Carbon Dioxide emissions each year")
    plt.legend()
    plt.show()


# Plot5
def plot_csv_data_scatter_n2o(filepath: str) -> None:
    """Uses read_csv_data_scatter_n2o() to read data and plots
    a scatterplot showing amount of nitrous oxide (N2O) emissions
    (kilotonnes) in USA, Canada and the European Union each year
    (between 1990 and 2014)
    """

    countries = ['Canada', 'United States of America', 'European Union']

    tags = ['nitrous_oxide_n2o_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags(filepath, tags, country_filter=countries)

    y = data[0]  # emission data
    labels = data[1]  # list of countries
    x = data[2] # list of years

    data = pd.DataFrame({"X Value": x, "Y Value": y, "Category": labels})

    groups = data.groupby("Category")  # to group the data by region/country

    for name, group in groups:
        plt.plot(group["X Value"], group["Y Value"], marker="o", linestyle="-", label=name)

    plt.xlabel("Years", fontsize=15)
    plt.ylabel("Emissions of Gases (in kilotonnes)", fontsize=15)
    plt.title("Nitrous Oxide emissions each year")
    plt.legend()
    plt.show()


# Plot6
def plot_csv_data_plotly_scatterboxplot_sparsely_pop(filepath: str) -> None:
    """ Uses read_csv_data_plotly_scatter_boxplot() to read data and plots a
    scatterplot and a box plot together showing distribution of amount of carbon
    dioxide (CO2) emissions (kilotonnes) in Austria, Belarus and Bulgaria in the
    24 year period (between 1990 and 2014). The scatterplot shows each year's
    emissions data for the 3 aforementioned countries and the boxplot aggregates
    and visualizes this data.
    """

    import plotly.graph_objects as go

    countries = ['Austria', 'Belarus', 'Bulgaria']

    tags = ['carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, countries, 0)

    y0 = data[0]
    y1 = data[1]
    y2 = data[2]

    emission_values = [y0, y1, y2]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
              'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)']

    fig = go.Figure()

    for xd, yd, cls in zip(countries, emission_values, colors):
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


# Plot7
def plot_csv_data_scatter_boxplot_1990_2014(filepath: str) -> None:
    """Uses read_csv_data_plotly_scatter_boxplot_1990_2014() to read data
    and plots a scatterplot and a box plot together showing distribution of
    hydrofluorocarbon (hfcs) emissions in 1990, 2002 and 2014 (in all countries
    taken together). The scatterplot shows each country's emissions data for the
    3 aforementioned years and the boxplot aggregates and visualizes this data.
    """
    import plotly.graph_objects as go

    years = [1990, 2002, 2014]

    tags = ['hydrofluorocarbons_hfcs_emissions_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, years, 1)

    y0 = data[0]
    y1 = data[1]
    y2 = data[2]

    emission_values = [y0, y1, y2]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
              'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)']

    fig = go.Figure()

    for xd, yd, cls in zip(years, emission_values, colors):
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


# Plot8
def plot_csv_data_bargraph(filepath: str) -> None:
    """Uses read_csv_data_bargraph() to read data and plots a grouped
    bargraph with methane emissions in the European Union and France.
    It also shows the methane emissions inthe European Union minus
    those from France. The bargraph resulting from this function shows
    data for years 1990 -2014.
    """

    countries = ['European Union', 'France']

    tags = ['methane_ch4_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent']

    data = data_by_tags_and_country_or_year(filepath, tags, countries, 0)
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
