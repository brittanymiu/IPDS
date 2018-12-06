from pandas.io.html import read_html
import pickle

refresh = False

if refresh:
    page = 'html = https://en.wikipedia.org/wiki/Farebox_recovery_ratio'
    wikitables = read_html(page)
    table = wikitables [1]
    pickle.dump(table, open("wiki_table.pkl", "w"))
else:
    table = pickle.load(open("wiki_table.pkl", "r"))

continent = table[0]
country = table[1]
system = table[2]
rates = table[3]

for rate in rates:
    print(rate)
