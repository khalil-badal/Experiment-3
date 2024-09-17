# EXPERIMENT 3 - PANDAS
# I. Intended Learning Outcomes:
# To identify the codes and functions incorporated in the Pandas library
# To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

# PROBLEM 1: Save your file as Surname_Pandas-P1.py
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
