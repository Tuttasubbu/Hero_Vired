import pandas as pd
inputs_list = []
squares_list = []
inputs = int(input("Enter Range : "))
for i in range(inputs):
    n = int(input())
    inputs_list.append(n)
    squares_list.append(n*n)
result = pd.Series(squares_list,index=[inputs_list])    
print(f"Squares Of All The Numbers In The List :\n{result}")
    