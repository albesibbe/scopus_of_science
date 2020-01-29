import pandas as pd
from scopus_of_science import wos, file_handler

w = wos.WOS(["datasets/wos_small.tsv", "datasets/wos_small2.tsv", "datasets/wos_small2.tsv"])
# w = file_handler.File_Handler(["datasets/scopus.csv", "datasets/scopus2.csv"])

print(w.convert())