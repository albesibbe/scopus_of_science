import pandas as pd
from .wos_tag import diz

class Sos:
    def __init__(self, scopus_path, wos_path, sep='\t', header=0, index_col=False):
        self.scopus_path = scopus_path
        self.wos_path = wos_path
        self.sep = sep
        self.header = header
        self.index_col = index_col
    
    def read_files(self):
        self.sco = pd.read_csv(self.scopus_path)
        self.wos = pd.read_csv(self.wos_path, sep=self.sep, header=self.header, index_col=self.index_col)
    
    def scopus_author_format(self, aut_string):
        aut_string = aut_string.replace(",","")
        aut_list = aut_string.split("; ")
        aut_corrected = []
        for aut in aut_list:
            name = aut.split()[1]
            name_initial = name[0]
            aut_corrected.append(aut.replace(name, name_initial + '.'))
        return "; ".join(aut_corrected)

    def convert_wos_to_sco(self):
        self.wos.rename(columns=diz, inplace=True)
        self.wos['Authors'] = self.wos['Authors'].apply(self.scopus_author_format)
        self.wos.drop([col for col in self.wos.columns if len(col) <= 2], axis=1, inplace=True)

    def merge(self):
        self.read_files()
        self.convert_wos_to_sco()
        self.merged = pd.concat([self.sco, self.wos], axis=0, ignore_index=True, sort=False)
        self.merged.drop_duplicates(subset=['DOI'], inplace=True)
        return self.merged