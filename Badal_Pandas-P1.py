# EXPERIMENT 3 - PANDAS
# PROBLEM 1: 
# Using knowledge obtained from the experiment and demonstrations:
# a. Load the corresponding .csv file into a data frame named cars using pandas
# b. Display the first five and last five rows of the resulting cars.

# start
# import pandas library
import pandas as pd

# a.) 
# load the csv file
cars_df = pd.read_csv("cars.csv")

# Concatenate a predefined number of spaces in order to neatly print the data frame title
print(" " * 38 + "Car List")

# Display the csv file to serve as a reference
print(cars_df)

# Print a new line
print("\n")

# b.) 
# Concatenate a predefined number of spaces in order to neatly print the data frame title
print(" " * 20 + "First Five Rows of the Resulting Cars")

# Display the first five rows of the resulting cars.
print(cars_df.head())

# Print a new line
print("\n")

# Concatenate a predefined number of spaces in order to neatly print the data frame title
print(" " * 20 + "Last Five Rows of the Resulting Cars")

# Display the last five rows of the resulting cars.
print(cars_df.tail())

# end
