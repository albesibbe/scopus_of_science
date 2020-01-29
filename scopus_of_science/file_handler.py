import pandas as pd
import os.path

class File_Handler:
    def __init__(self, path):
        self.path = path
        if self.check_consistency():
            self.read_file()
        else:
            raise TypeError("No same extension.")
        print(path)

    def read_file(self):
        extension = os.path.splitext(self.path[0])[1]
        li = []
        for filename in self.path:
            if extension == '.csv':
                df = pd.read_csv(filename)
            else:
                df = pd.read_csv(filename, sep='\t', header=0, index_col=False)
            li.append(df)
        self.data = pd.concat(li, axis=0, ignore_index=True, sort=False)

    def check_consistency(self):
        extension = os.path.splitext(self.path[0])[1]
        for f in self.path:
            if os.path.splitext(f)[1] != extension:
                return False
        return True
            