import pandas as pd

def Average(data, field):
    sum = 0.0
    vector = data[field]
    for i in range(0, len(vector)):
        sum += vector[i]
    average = sum / len(vector)
    return average

iris = pd.read_csv("iris.csv")
print(iris.head())
print()
avg = Average(iris, "sepalLength")
print(f"The average of Sepal Length = {avg:.3f}\n")

