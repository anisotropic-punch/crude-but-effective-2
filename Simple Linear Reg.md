

```python
print("Simple Linear Regression")
# Simple Linear Regression


#<p align="center">
#  <img src="https://github.com/Avik-Jain/100-Days-Of-ML-Code/blob/master/Info-graphs/Day%202.jpg">
#</p>


# Step 1: Data Preprocessi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\Deborah Novich\Desktop\PythonTest\studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

print("pre sklearn")

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 

# Step 2: Fitting Simple Linear Regression Model to the training set
# 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)
# Step 3: Predecting the Result
Y_pred = regressor.predict(X_test)
 
 # Step 4: Visualization 
 ## Visualising the Training results
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
 
 ## Visualizing the test results

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
```

    Simple Linear Regression
    pre sklearn
    




    [<matplotlib.lines.Line2D at 0x4f098d0>]




![png](output_0_2.png)

