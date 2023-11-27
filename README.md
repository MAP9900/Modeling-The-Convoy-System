# Modeling-The-Convoy-System
DESCRIPTION:
Data from various World War II convoys are examined to create models and classifiers able to predict convoys at low and high risk of suffering losses. Sourced from the Arnold Hague Convoy Database, nearly 70,000 merchant and escort ships were collected. This ship data was then cleaned and verified through data from uboat.net. 

Currently five different denominations of convoys are being examined: OB, ONS, ON, SC, HX. All are North Atlantic Convoys traveling from North America to the United Kingdom or vice versa. In the future additional North Atlantic convoy denominations will be added such as OA convoys. 

A series of models were fitted attempting to predict overall sink percentages of specific convoys, but due to the complex nature of convoys and submarine attacks, the models fit both the train and test data poorly. A switch to classifying convoys as low vs high risk (low being no ships sunk, high being at least one ship sunk) was taken and produced much better results through Random Forest and Gradient Boosting Classification.

From here, the classifiers were optimized through Grid Search Cross-Validation, among other methods and feature analysis was performed to identify leading factors at predicting convoy vulnerability. Graphing of the data was also done to identify trends in the convoy data and also to help visualize some of the factors that put convoys at risk. 

In the future, further refinement of the classifiers will be done, along with more plotting of the data. Additionally, performing time series analysis on the data to create a more realistic approach to predicting convoy vulnerability where future data is not used in the predictions. 
