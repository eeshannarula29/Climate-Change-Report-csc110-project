"""
This file will run all the visualizations and programs
"""

import analyze_data
import greenhousegases_project
import global_land_temp
import future_predict

# initializing filepath

Greenhouse_emissions_data = 'datasets/greenhouse_gas_inventory_data_data.csv'
Co2_per_capita_data = 'datasets/emissions_per_capita.csv'
Land_temp_data = 'datasets/filtered_land_temp.csv'
Twitter_data = 'datasets/climate-change-sentiment.csv'


def run_greenhouse_visualizations() -> None:
    """
    Plots visualizations for Greenhouse gas emissions visualizations
    """
    greenhousegases_project.plot_all_countries_peryear(Greenhouse_emissions_data)
    greenhousegases_project.plot_scatter_n2o(Greenhouse_emissions_data)
    greenhousegases_project.scatterboxplot_sparsely_pop(Greenhouse_emissions_data)
    greenhousegases_project.plot_scatter_boxplot_1990_2014(Greenhouse_emissions_data)

    greenhousegases_project.plot_emission_per_gdp(Co2_per_capita_data)
    greenhousegases_project.dist_2016(Co2_per_capita_data)


def run_land_temp_visualizations() -> None:
    """
    Plots visualizations for Land temperature related visualizations
    """
    global_land_temp.plot_data_greater_average(Land_temp_data)
    global_land_temp.plot_data_usa_can_all(Land_temp_data)


def twitter_visualizations() -> None:
    """
    Plot the visualizations for twitter data
    """
    analyze_data.plot_sentiments(Twitter_data)
    analyze_data.plot_top_10(Twitter_data)


def predictions_visualizations() -> None:
    """
    Plot the best fit lines and cost function graphs
    for Co2 emissions and Land temperature from 1990
    to 2014 and 2013 respectively, and print the
    predictions for 2015 2016 and 2017
    """
    future_predict.predict_temp_and_emissions(Land_temp_data, Greenhouse_emissions_data)


if __name__ == '__main__':

    print('Hi! welcome to our project')

    commands = ['run_land_temp_visualizations()',
                'run_greenhouse_visualizations()',
                'twitter_visualizations()',
                'predictions_visualizations()']

    want_to_exit = False

    while not want_to_exit:
        print('choose an option')
        print('1. look at average land temperature data visualizations')
        print('2. look at Greenhouse gas data visualizations')
        print('3. look at Twitter data visualizations')
        print("4. look at the visualizations and predictions of Canada's Co2 emissions for 2015, 2016 and 2017 ")
        print('5. exit')

        human_input = input('type an option from 1 to 5 : ')

        if human_input in ['1', '2', '3', '4', '5']:
            if human_input == '5':
                want_to_exit = True
            else:
                eval(commands[int(human_input) - 1])
