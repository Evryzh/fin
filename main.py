import pandas as pd

pay_day = pd.read_csv('test.csv', sep=";", encoding="mbcs")
pay_day = pay_day.dropna(subset=['Счет зачисления'])
print(pay_day)
