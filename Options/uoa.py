import pandas as pd

uo = pd.read_csv('../data/uo.csv')
uoC = uo[uo['Type'] == 'Call']
uoP = uo[uo['Type'] == 'Put']

calls = uoC.Symbol.value_counts().head()
puts = uoP.Symbol.value_counts().head()

# c = 'Calls '
# p = 'Puts '

print('Calls')
print(calls)
print(' ')
print('Puts')
print(puts)
