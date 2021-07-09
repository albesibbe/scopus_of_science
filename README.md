# scopus_of_science
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/albesibbe/scopus_of_science.svg?branch=master)](https://travis-ci.com/albesibbe/scopus_of_science)

## Description
This package merges databases downloaded from Scopus (.csv) and Web of Science (plain text with the extension .txt). 
It returns a pandas DataFrame which can be saved as a Scopus .csv file compatible with 
softwares for bibliographic analysis (such as [**VOSviewer**][VOSviewer]) 

[VOSviewer]: https://www.vosviewer.com/

## Installation
```python
pip install scopus_of_science
```

## Usage

```python
from scopus_of_science import SOS

s = SOS(sco="datasets/scopus.csv", wos=["datasets/wos1.txt", "datasets/wos2.txt"])

data = s.get()

print(data)

data.to_csv("csv_filename.csv", index=False)

```
## Dependencies
- [pandas](https://pandas.pydata.org/)

## Contributing
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome
