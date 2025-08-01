import math
import os
import random
import re
import sys

#Problem of LinearRegression but with a cap
#To solve this I needed to remove all the data that had a 8 as a Y, that's because the cap is 8,
#it means that the Y should be greater than that but was cropped as 8, so it is not so good, because
#it isn't learned using the LR model

if __name__ == '__main__':
    training_data = '''2.81,5.62
7.14,8.00
2.72,5.44
3.87,7.74
1.90,3.80
7.82,8.00
7.02,8.00
5.50,8.00
9.15,8.00
4.87,8.00
8.08,8.00
5.58,8.00
9.13,8.00
0.14,0.28
2.00,4.00
5.47,8.00
0.80,1.60
4.37,8.00
5.31,8.00
0.00,0.00
1.78,3.56
3.45,6.90
6.13,8.00
3.53,7.06
4.61,8.00
1.76,3.52
6.39,8.00
0.02,0.04
9.69,8.00
5.33,8.00
6.37,8.00
5.55,8.00
7.80,8.00
2.06,4.12
7.79,8.00
2.24,4.48
9.71,8.00
1.11,2.22
8.38,8.00
2.33,4.66
1.83,3.66
5.94,8.00
9.20,8.00
1.14,2.28
4.15,8.00
8.43,8.00
5.68,8.00
8.21,8.00
1.75,3.50
2.16,4.32
4.93,8.00
5.75,8.00
1.26,2.52
3.97,7.94
4.39,8.00
7.53,8.00
1.98,3.96
1.66,3.32
2.04,4.08
11.72,8.00
4.64,8.00
4.71,8.00
3.77,7.54
9.33,8.00
1.83,3.66
2.15,4.30
1.58,3.16
9.29,8.00
1.27,2.54
8.49,8.00
5.39,8.00
3.47,6.94
6.48,8.00
4.11,8.00
1.85,3.70
8.79,8.00
0.13,0.26
1.44,2.88
5.96,8.00
3.42,6.84
1.89,3.78
1.98,3.96
5.26,8.00
0.39,0.78
6.05,8.00
1.99,3.98
1.58,3.16
3.99,7.98
4.35,8.00
6.71,8.00
2.58,5.16
7.37,8.00
5.77,8.00
3.97,7.94
3.65,7.30
4.38,8.00
8.06,8.00
8.05,8.00
1.10,2.20
6.65,8.00'''
    X_list = []
    Y_list = []
    lines = training_data.strip().splitlines()
    for line in lines:
        xy = line.split(',')
        if(float(xy[1]) < 8): #here is the thing, we remove all the Y == 8
            X_list.append(float(xy[0]))
            Y_list.append(float(xy[1]))
        
    numerator = 0
    denominator = 0
    n = len(X_list)
    x_bar = sum(X_list, start = 0)/n
    y_bar = sum(Y_list, start = 0)/n
    for i in range(n): #here we make the somatories needed
        numerator += (X_list[i] - x_bar) * (Y_list[i] - y_bar)
        denominator += (X_list[i] - x_bar) ** 2
        
    slope = numerator/denominator #slope formula
    intercept = y_bar - (x_bar * slope) #intercept formula
    
    timeCharged = float(input().strip())
    output = (timeCharged * slope) + intercept
    if output > 8:
        print(8)
    else:
        print(output)
    