# csc110-project
# Reverberations of Climate Change on Earth and Humans

Hi! everyone, this is a project by first year computer science students at the University of Toronto, on the topic climate change. The autors of this project are: 

- Eeshan Narula
- Garv Sood
- Avnish Pasari
- Aakash Vaithyanathan

## Introdunction 

Our planet is becoming warmer day by day, from the North to the South pole. Human activities have lead to an exponential rise in the temperature of the earth, and its impacts have started to prevail. The effects of global warming are appearing right now, glaciers are melting, sea level is rising, people are getting sick, more wildfires are being produced, and carbon emissions are increasing. (1)

The rising global land temperature has a detrimental impact on the ecosystem affecting various other components of the earth. It has a serious effect on vegetation and causes various health problems for humans. Furthermore, an increase in land temperatures across the globe results in the melting of glaciers, permafrost, and ice sheets all of which in turn contribute to an increase in sea levels which affects the coastal inhabitants and results in loss of habitat for fishes, birds, and plants.(2)

Human activities such as the burning of fossil fuels and large-scale deforestation in recent years have led to the release of greenhouse gases on a scale that has never been seen before. The rise of the concentration of greenhouse gases in the air is an indication that we are turning up the dial on global warming. The greenhouse effect (due to increased greenhouse gas emissions) traps the Sun’s radiation and re-radiates it. This is causing catastrophic effects by altering ecosystems, raising sea levels, and causing more frequent extreme weather events.(2)

These increasing emissions vary from country to country, continent to continent. Developed countries are taking steps to decrease climate change, but developing countries are emitting more gasses which is why more people are getting sick in those areas. Thus there is a relation between the GDP of a country and the deaths per year.(3)

The question we want to analyze in our project is that **How with time, climate change has affected and will affect the environment and humans? How has the human response to climate change grown over time?**


1. https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-climate-change-k4.html 

2. https://climate.nasa.gov/effects/

3. https://cleanair.camfil.us/2017/10/30/air-pollution-in-developing-countries/


## Datasets

- The first dataset consists of levels of emissions for different greenhouse gases and for dif- ferent countries from 1990 to 2014. The columns we would be using are country_or_area, year, value and category.
   
Source: Kaggle: https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions 

Format: csv

- The second dataset contains land temperature for different countries from 1743-11-01 to 2013-09-01. Although we would only be using data from 1990 to 2013. The columns we would be using are dt(date), AverageTemperature, Country.

Source: Kaggle: https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature- data

Format: csv

- The third dataset contains CO2 emissions (kg per PPP $ of GDP) for different countries from 1960 to 2020, but the data has consistent values from 1990 to 2016, thus we only use columns for 1990 to 2016, and Country Name.

Source: Worldbank: https://data.worldbank.org/indicator/EN.ATM.CO2E.PP.GD 

Format: csv

- The forth dataset is made by us, using the Twitter API to fetch the most recent tweets from 31st October to 9th November, for previous 10 days. We also added sentiment scores and sentiment type(neutral, positive or negative) to the dataset. The columns we would be using are tweet_text, senti-score,senti-type and created_at.

Source: made by us using Twitter API 

Format: csv

- The last dataset contains words with their sentiment score. This dataset is used to calculate the sentiment score for the 4th dataset. The dataset only has two columns, which are the words and the sentiment scores, and we are using both of the columns.

Source: HLT: https://hlt-nlp.fbk.eu/technologies/sentiwords

Format: text
