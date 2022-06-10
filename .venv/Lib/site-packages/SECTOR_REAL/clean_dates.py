import pandas as pd

l = pd.Series([1,2,3,4]).apply(lambda x: x**2).tolist()
print(l)