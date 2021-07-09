import pandas as pd
import os.path
import re


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
                df = pd.read_csv(filename, dtype=str)
            else:
                with open(filename) as f:
                    content = f.read()
                content = content.replace('\n  ', ';')
                documents = content.split("\n\n")
                documents[0] = 'PT' + documents[0].split("PT")[1]
                documents = documents[0:-1]
                data = []
                for document in documents:
                    fields = dict(re.findall("\n?(\w{2,2})\s?(.*)", document))
                    data.append(fields)
                df = pd.DataFrame(data)

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
