# Predict Flight Prices
## _Udacity Data Scientist Course_

In this project a dataset including 50 days of flights connecting 6 main India cities is analyzed. The objective is to find out what key factors influence flight prices and to explore machine learning algorithms to predict them. The project aims to answer these three main questions:

- How many days in advance is it cheapest to buy a flight ticket?
- What other parameters influence flight price and how?
- How well can naive machine learning predict flight prices?

## Libraries used

- _Pandas_ and _Numpy_ for data analysis
- _Sklearn_, _category_encoders_ and _xgboost_ for ML
- _Plotly_ for data visualization

## Files
- _code/exploratory_data_analysis.ipynb_: main notebook containing data wrangling, exploration of the data set, visualizations and machine learning.
- _data_: folder containing project's dataset.

## Dataset
The dataset is from Kaggle and can be obtained here ([link]). It is also found in the data folder.

## Results
Answering the three initial questions:
- It is best to buy flights more than 15 days in advance.
- Flight class greatly influences price. It is cheaper to flight late at night. Flight duration and price are linearly related fro flights with 0 layovers.
- Random forest algorithm allows to predict prices with an r2 of 0.985.

See blog post [medium_post], for analysis results.

## Acknowledgements
Dataset credit:
Kaggle - Shubham Bathwal


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
[link]: <https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction>
[medium_post]: https://medium.com/@sandracoll.97/can-we-guess-flight-prices-991bf3d67fe3