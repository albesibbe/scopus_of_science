from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='scopus_of_science',
      version='0.0.1',
      description='Merge Scopus and WoS databases in Scopus csv format',
      url='https://github.com/albesibbe/scopus_of_science',
      author='Alberto Silvestri',
      author_email='albertosilvestri@me.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=[
          'pandas',
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
      ],
      zip_safe=False)