import scopus_of_science.wos_tag as wt
import pandas as pd
from .file_handler import File_Handler

class WOS(File_Handler):
    def __init__(self, path):
        super().__init__(path)
        print("WoS database has " + str(self.data.shape[0]) + " publications")
        
    def scopus_author_format(self, aut_string):
        aut_string = aut_string.replace(",","")
        aut_list = aut_string.split("; ")
        aut_corrected = []
        for aut in aut_list:
            name = aut.split()[1]
            name_initial = name[0]
            aut_corrected.append(aut.replace(name, name_initial + '.'))
        return "; ".join(aut_corrected)

    def convert(self):
        self.data.rename(columns=wt.diz, inplace=True)
        self.data['Authors'] = self.data['Authors'].apply(self.scopus_author_format)
        self.data.drop([col for col in self.data.columns if len(col) <= 2], axis=1, inplace=True)
        headers = pd.DataFrame(columns=wt.vals)
        self.data = pd.concat([headers, self.data], axis=0, ignore_index=True, sort=False)
        return self.data