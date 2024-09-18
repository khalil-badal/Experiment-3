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
### a.)
Load the csv file 
```python
cars_df = pd.read_csv('cars.csv')
```
Display the csv file
```python
print(cars_df)

```

|   | Model             | mpg  | cyl | disp  | hp  | drat | wt    | qsec | vs | am | gear | carb |
|---|-------------------|------|-----|-------|-----|------|-------|------|----|----|------|------|
| 0 | Mazda RX4        | 21.0 | 6   | 160.0 | 110 | 3.90 | 2.620 | 16.46| 0  | 1  | 4    | 4    |
| 1 | Mazda RX4 Wag    | 21.0 | 6   | 160.0 | 110 | 3.90 | 2.875 | 17.02| 0  | 1  | 4    | 4    |
| 2 | Datsun 710        | 22.8 | 4   | 108.0 | 93  | 3.85 | 2.320 | 18.61| 1  | 1  | 4    | 1    |
| 3 | Hornet 4 Drive    | 21.4 | 6   | 258.0 | 110 | 3.08 | 3.215 | 19.44| 1  | 0  | 3    | 1    |
| 4 | Hornet Sportabout | 18.7 | 8   | 360.0 | 175 | 3.15 | 3.440 | 17.02| 0  | 0  | 3    | 2    |
| 5 | Valiant           | 18.1 | 6   | 225.0 | 105 | 2.76 | 3.460 | 20.22| 1  | 0  | 3    | 1    |
| 6 | Duster 360        | 14.3 | 8   | 360.0 | 245 | 3.21 | 3.570 | 15.84| 0  | 0  | 3    | 4    |
| 7 | Merc 240D         | 24.4 | 4   | 146.7 | 62  | 3.69 | 3.190 | 20.00| 1  | 0  | 4    | 2    |
| 8 | Merc 230          | 22.8 | 4   | 140.8 | 95  | 3.92 | 3.150 | 22.90| 1  | 0  | 4    | 2    |
| 9 | Merc 280          | 19.2 | 6   | 167.6 | 123 | 3.92 | 3.440 | 18.30| 1  | 0  | 4    | 4    |
| 10| Merc 280C         | 17.8 | 6   | 167.6 | 123 | 3.92 | 3.440 | 18.90| 1  | 0  | 4    | 4    |
| 11| Merc 450SE        | 16.4 | 8   | 275.8 | 180 | 3.07 | 4.070 | 17.40| 0  | 0  | 3    | 3    |
| 12| Merc 450SL        | 17.3 | 8   | 275.8 | 180 | 3.07 | 3.730 | 17.60| 0  | 0  | 3    | 3    |
| 13| Merc 450SLC       | 15.2 | 8   | 275.8 | 180 | 3.07 | 3.780 | 18.00| 0  | 0  | 3    | 3    |
| 14| Cadillac Fleetwood| 10.4 | 8   | 472.0 | 205 | 2.93 | 5.250 | 17.98| 0  | 0  | 3    | 4    |
| 15| Lincoln Continental| 10.4 | 8  | 460.0 | 215 | 3.00 | 5.424 | 17.82| 0  | 0  | 3    | 4    |
| 16| Chrysler Imperial  | 14.7 | 8  | 440.0 | 230 | 3.23 | 5.345 | 17.42| 0  | 0  | 3    | 4    |
| 17| Fiat 128          | 32.4 | 4   | 78.7  | 66  | 4.08 | 2.200 | 19.47| 1  | 1  | 4    | 1    |
| 18| Honda Civic       | 30.4 | 4   | 75.7  | 52  | 4.93 | 1.615 | 18.52| 1  | 1  | 4    | 2    |
| 19| Toyota Corolla    | 33.9 | 4   | 71.1  | 65  | 4.22 | 1.835 | 19.90| 1  | 1  | 4    | 1    |
| 20| Toyota Corona     | 21.5 | 4   | 120.1 | 97  | 3.70 | 2.465 | 20.01| 1  | 0  | 3    | 1    |
| 21| Dodge Challenger  | 15.5 | 8   | 318.0 | 150 | 2.76 | 3.520 | 16.87| 0  | 0  | 3    | 2    |
| 22| AMC Javelin       | 15.2 | 8   | 304.0 | 150 | 3.15 | 3.435 | 17.30| 0  | 0  | 3    | 2    |
| 23| Camaro Z28        | 13.3 | 8   | 350.0 | 245 | 3.73 | 3.840 | 15.41| 0  | 0  | 3    | 4    |
| 24| Pontiac Firebird  | 19.2 | 8   | 400.0 | 175 | 3.08 | 3.845 | 17.05| 0  | 0  | 3    | 2    |
| 25| Fiat X1-9         | 27.3 | 4   | 79.0  | 66  | 4.08 | 1.935 | 18.90| 1  | 1  | 4    | 1    |
| 26| Porsche 914-2     | 26.0 | 4   | 120.3 | 91  | 4.43 | 2.140 | 16.70| 0  | 1  | 5    | 2    |
| 27| Lotus Europa      | 30.4 | 4   | 95.1  | 113 | 3.77 | 1.513 | 16.90| 1  | 1  | 5    | 2    |
| 28| Ford Pantera L    | 15.8 | 8   | 351.0 | 264 | 4.22 | 3.170 | 14.50| 0  | 1  | 5    | 4    |
| 29| Ferrari Dino      | 19.7 | 6   | 145.0 | 175 | 3.62 | 2.770 | 15.50| 0  | 1  | 5    | 6    |
| 30| Maserati Bora     | 15.0 | 8   | 301.0 | 335 | 3.54 | 3.570 | 14.60| 0  | 1  | 5    | 8    |
| 31| Volvo 142E        | 21.4 | 4   | 121.0 | 109 | 4.11 | 2.780 | 18.60| 1  | 1  | 4    | 2    |

### b.)
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

### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
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
### b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
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
### c.) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
import pandas library
```python
import pandas as pd
```
load the csv file
```python
cars_df = pd.read_csv('cars.csv')
```
# Display the number of cyl of the car model Camaro Z28 by subsetting 
# Using i.loc select row 23 and columns 0 and 2 from the DataFrame cars_df.
```python
cyl_Camaro_Z28 = cars_df.iloc[[23],[0,2]]
```
Display the model, and cyl as a result
```python
cyl_Camaro_Z28

```
### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
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

### Authors
#### Khalil Badal

