import pandas as pd
import scopus_of_science as sos

p = sos.Sos("datasets/scopus.csv", "datasets/wos_small.tsv")
df = p.merge()
print(df)
df.to_csv("test.csv")