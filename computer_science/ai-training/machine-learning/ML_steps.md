# Machine Learning Problems Solving Steps

Inspired from this [post](https://www.linkedin.com/pulse/approaching-almost-any-machine-learning-problem-abhishek-thakur/) and this [post](https://www.kaggle.com/pktippa/titanic-data-science-solutions)

## Loading Data

### From CSV

#### Using `numpy`

```python
import numpy as np
# dtype=None means importing as record array, as opposed to normal array, need to understand more about the difference.
# names=True, indicates the csv contains the first row as header
data = np.genfromtxt('grades.txt', dtype=None, delimiter='\t', names=True)
```

#### Using `pandas`

```python
import pandas as pd
# path of csv with respect to current python file location
test_df = pd.read_csv('../input/test.csv')
```

## Separating features and labels

### From `numpy`

```python
# Required label name
label_name = 'return_'

# Here the train_data is data the loaded data as shown above.
# Extracting label from data 
y_train = train_data[label_name]

# Removing label from train_data using list compression
X_train = train_data[[b for b in list(train_data.dtype.names) if b != label_name]]
```

### From `pandas`

```python
# Extracting the last column from slicing
y_train = train_data.iloc[:,-1]

# Dropping last column using df.drop
train_data = train_data.drop(label_name, 1)
	
```

## Splitting the data into training and validation sets

### For Classification problems

#### For `numpy`

```python
# cross_validation is deprecated after 0.20
from sklearn.cross_validation import StratifiedKFold
eval_size = 0.10
kf = StratifiedKFold(y, round(1. / eval_size))
train_indices, valid_indices = next(iter(kf))
X_train, y_train = X[train_indices], y[train_indices]
X_valid, y_valid = X[valid_indices], y[valid_indices]
```
#### For `pandas`

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
```

### For Regression problems

#### For `numpy`

```python
from sklearn.cross_validation import KFold
eval_size = 0.10
kf = KFold(len(y), round(1. / eval_size))
train_indices, valid_indices = next(iter(kf))
X_train, y_train = X[train_indices], y[train_indices]
X_valid, y_valid = X[valid_indices], y[valid_indices]
```

#### For `pandas`

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
```

## Identification of different variables in data

### For `pandas`

```python
# For description of dataframe
df.describe(include='all')
# Listing columns datatypes
df.dtypes
```

## Separate out numerical variables first

