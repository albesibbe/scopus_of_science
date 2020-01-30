# scopus_of_science
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Installation
```python
pip install scopus_of_science
```

## Usage

```python
>>> from scopus_of_science import sos

>>> s = sos.SOS(sco=["datasets/scopus.csv"], wos=["datasets/wos1-500.txt", "datasets/wos501-526.txt"])

>>> data = s.get()

>>> print(data)

>>> data.to_excel("exel_filename.xlsx")

```

## Contributing
PRs are welcome, if you have any questions don't be afraid to open an issue.
