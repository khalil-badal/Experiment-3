# EXPERIMENT 3 - PANDAS
# I. Intended Learning Outcomes:
# To identify the codes and functions incorporated in the Pandas library
# To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

# PROBLEM 2: Save your file as Surname_Pandas-P2.py
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.¶
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# start
# import pandas library
import pandas as pd

# load the csv file
cars_df = pd.read_csv("cars.csv")

# Concatenate a predefined number of spaces in order to neatly print the data frame title
print(" " * 38 + "Car List")

# Display the csv file to serve as reference for the dataframe
print(cars_df)

# Print a new line
print("\n")


# a.) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# Slice the DataFrame: Select all rows, and every second column starting from the first
odd_columns_df = cars_df[cars_df.columns[::2]]

# Display the category
print(
    "a.) The first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars."
)

# Display the first five rows by using the data frame method df.head()
print(odd_columns_df.head())

# Print a new line
print("\n")


# b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# By indexing, filter the DataFrame to get rows where 'Model' is 'Mazda RX4'
row_Model_Mazda_RX4 = cars_df[cars_df["Model"] == "Mazda RX4"]

# Display the category
print("b.) Display The row that contains the Model of Mazda RX")

# Display the result
print(row_Model_Mazda_RX4)

# Print a new line
print("\n")


# c.) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# By subsetting, use i.loc select row 23 and columns 0 and 2 from the DataFrame cars_df.
cyl_Camaro_Z28 = cars_df.iloc[[23], [0, 2]]

# Display the category
print("c.) Cylinder Count for Camaro Z28")

# Display the model, and cyl as a result
print(cyl_Camaro_Z28)


# Print a new line
print("\n")


# d.) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# by indexing,  display how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
gear_and_cyl = cars_df.loc[[1, 18, 28], ["Model", "cyl", "gear"]]

# Display the category
print("d.) Cylinder and Gear count")

# Display the model, cyl and gear as a result
print(gear_and_cyl)

# end
