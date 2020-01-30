import scopus_of_science.constants as cons
import pandas as pd
import re
from .file_handler import File_Handler

class WOS(File_Handler):
    def __init__(self, path, convert=True):
        super().__init__(path)
        if convert:
            self.convert()
        print("WoS database has " + str(self.data.shape[0]) + " publications")

    def scopus_author_format(self, aut_string):
        aut_corrected = []
        try:
            aut_string = aut_string.replace(",","")
            aut_list = aut_string.split("; ")
            for aut in aut_list:
                name = aut.split()[1]
                name_initial = name[0]
                aut_corrected.append(aut.replace(name, name_initial + '.'))
        finally:
            return "; ".join(aut_corrected)

    def convert(self):
        self.data.rename(columns=cons.DIC, inplace=True)
        self.data['Authors'] = self.data['Authors'].apply(self.scopus_author_format)
        self.data.drop([col for col in self.data.columns if len(col) <= 2], axis=1, inplace=True)
        headers = pd.DataFrame(columns=cons.S_TAGS)
        self.data['Source'] = 'WoS'
        self.data = pd.concat([headers, self.data], axis=0, ignore_index=True, sort=False)

class SCO(File_Handler):
    def __init__(self, path):
        super().__init__(path)
        print("Scopus database has " + str(self.data.shape[0]) + " publications")


class SOS(File_Handler):
    def __init__(self, sco=[], wos=[]):
        self.sco_data = SCO(sco).get()
        self.wos_data = WOS(wos).get()
        self.concat([self.sco_data, self.wos_data])
        print("Database has " + str(self.data.shape[0]) + " total publications")
        self.remove_duplicates()

    def remove_duplicates(self):
        data_copied = self.data.copy()
        data_copied['Title'] = data_copied['Title'].apply(lambda x: re.sub(r'\W+', '', x.lower()))
        tit_idx = data_copied.duplicated(subset="Title")
        DOI_idx = data_copied.duplicated(subset="DOI") & data_copied["DOI"].notnull()
        self.data.drop(self.data[tit_idx | DOI_idx].index, inplace=True)
        self.data.reset_index(drop=True, inplace=True)
        print(str(sum(tit_idx | DOI_idx)) + " duplicates removed")
