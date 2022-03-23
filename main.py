import pandas as pd

pay_day = pd.read_csv('test.csv', sep=";", encoding="mbcs")
print(pay_day)
