from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt # sklearn < 0.22.0
# line: y = 1.2x + 2
# points: (2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)

pointX = [2, 5, -4, -7, 8]
pointY = [-2, 6, -4, 1, 14]

pointYHat = [] # to store y hat values

# Finding the y-hat and store it in an array
for px in pointX:
    pointYHat.append(1.2*px + 2)

# Reference https://stackoverflow.com/questions/17197492/is-there-a-library-function-for-root-mean-square-error-rmse-in-python
# rms = mean_squared_error(pointY, pointYHat, squared=False) # sklearn >= 0.22.0
rms = sqrt(mean_squared_error(pointY, pointYHat)) # sklearn < 0.22.0
print(mean_absolute_error(y_true=pointY, y_pred=pointYHat))
print(rms)

# of without sklearn
# MAE
def mae(ytrue, yhat):
    error = sum([abs(y-yh) for (y, yh) in zip(ytrue, yhat)])/len(ytrue)
    return error
# MSE
def mse(ytrue, yhat) :
    error = sum([(y - yh)**2 for (y, yh) in zip(ytrue, yhat)])/(2*len(ytrue))
    return error

points = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
ytrue = [p[1] for p in points]
yhat = []
for x in [p[0] for p in points]:
    yhat.append(1.2*x+2)
print(mae(ytrue, yhat))
print(mse(ytrue, yhat))
