import pandas as pd
import os.path

class File_Handler:
    def __init__(self, path):
        if isinstance(path, str):
            self.path = [path]
        else:
            self.path = path
        if self.check_consistency():
            self.read_file()
        else:
            raise TypeError("Files have different extension.")

    def read_file(self):
        extension = os.path.splitext(self.path[0])[1]
        li = []
        for filename in self.path:
            if extension == '.csv':
                df = pd.read_csv(filename)
            else:
                try:
                    df = pd.read_csv(filename, sep='\t', header=0, index_col=False)
                except UnicodeDecodeError:
                    df = pd.read_csv(filename, sep='\t', header=0, index_col=False, encoding='utf-16')
            li.append(df)
        self.concat(li)

    def concat(self, li):
        self.data = pd.concat(li, axis=0, ignore_index=True, sort=False)

    def check_consistency(self):
        extension = os.path.splitext(self.path[0])[1]
        for f in self.path:
            if os.path.splitext(f)[1] != extension:
                return False
        return True
    
    def get(self):
        return self.data