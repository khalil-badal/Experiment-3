# EXPERIMENT 3 - PANDAS

#### Khalil T. Badal                                             
#### 2ECE-B
#### September 19,2024

### I. Intended Learning Outcomes:
To identify the codes and functions incorporated in the Pandas library
To be able to apply and use the different codes and functions in creating a Python program using a Pandas library <br>


### PROBLEM 1: Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:                    
a. Load the corresponding .csv file into a data frame named cars using pandas               
b. Display the first five and last five rows of the resulting cars.

#### Start 
import pandas library
```python
import pandas as pd
```
#### a.)
Load the csv file 
```python
cars_df = pd.read_csv('cars.csv')
```
Display the csv file
```python
print(cars_df)

```


#### b.)
Display the first five rows of the resulting cars. 
Use df.head() method to display the first five rows
```python
cars_df.head()

```
Display the last five rows of the resulting cars.  <br>
```python
cars_df.tail()

```
### PROBLEM 2: Save your file as Surname_Pandas-P2.py


#### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.                    
##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.                
##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.            
##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

#### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
import pandas library
```python
import pandas as pd
```
load the csv file
```python
cars_df = pd.read_csv('cars.csv')

```
Display the first five rows with odd-numbered columns by slicing
Slice the DataFrame: Select all rows, and every second column starting from the first
Create a new DataFrame `odd_columns_df` by selecting only the odd-numbered columns from `cars_df`
The slice notation `::2` means "start at the first column and select every second column."
```python
odd_columns_df = cars_df[cars_df.columns[::2]]
```
Display the first five rows by using the data frame method df.head()
```python
odd_columns_df.head()

```
#### b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
import pandas library
```python
import pandas as pd
```
load the csv file
```python
cars_df = pd.read_csv('cars.csv')
```
Display the row that contains the 'Model' of 'Mazda RX4' by indexing
Filter the DataFrame to get rows where 'Model' is 'Mazda RX4'
```python
row_Model_Mazda_RX4 = cars_df[cars_df['Model'] == 'Mazda RX4']
```
Display the result
```python
row_Model_Mazda_RX4

```
#### c.) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
import pandas library
```python
import pandas as pd
```
load the csv file
```python
cars_df = pd.read_csv('cars.csv')
# Display the number of cyl of the car model Camaro Z28 by subsetting 
# Using i.loc select row 23 and columns 0 and 2 from the DataFrame cars_df.
```python
cyl_Camaro_Z28 = cars_df.iloc[[23],[0,2]]
```
Display the model, and cyl as a result
```python
cyl_Camaro_Z28

```
#### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
import pandas library
```python
import pandas as pd
```
load the csv file
```python
cars_df = pd.read_csv('cars.csv')
```
by indexing,  display how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
```python
gear_and_cyl = cars_df.loc[[1,18,28],['Model', 'cyl', 'gear']]
```
Display the model, cyl and gear as a result
```python
gear_and_cyl

```
#### End

#### Authors
Khalil Badal

