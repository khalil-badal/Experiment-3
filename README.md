# EXPERIMENT 3 - PANDAS

Khalil T. Badal                                             
2ECE-B
September 19,2024

### I. Intended Learning Outcomes:
To identify the codes and functions incorporated in the Pandas library
To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

#### PROBLEM 1: Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:                    
a. Load the corresponding .csv file into a data frame named cars using pandas               
b. Display the first five and last five rows of the resulting cars.

Start by importing pandas library
```python
import pandas as pd
```
### a.)
Load the csv file 
```python
cars_df = pd.read_csv('cars.csv')
```
Display the csv file
```python
print(cars_df)

```
### b.)
Display the first five rows of the resulting cars. 
Use df.head() method to display the first five rows
```python
cars_df.head()

```
Display the last five rows of the resulting cars. 
```python
cars_df.tail()



