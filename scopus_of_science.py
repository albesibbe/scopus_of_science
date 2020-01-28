import pandas as pd

sco = pd.read_csv("datasets/scopus.csv")
print(sco.columns)
wos = pd.read_csv("datasets/wos_small.tsv", sep='\t')
print(wos.columns)

