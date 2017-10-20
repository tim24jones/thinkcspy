def sum_of_squares(xs):
    squared_value=0
    for i in range(len(xs)):
        squared_value=xs[i]**2+squared_value
    return(squared_value)
print(sum_of_squares([30,2,8]))
