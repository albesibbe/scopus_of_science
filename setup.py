from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(name='scopus_of_science',
      version='0.1',
      description='Merge Scopus and WoS databases in Scopus csv format',
      url='https://github.com/albesibbe/scopus_of_science',
      author='Alberto Silvestri',
      author_email='albertosilvestri@me.com',
      long_description=long_description,
      license='MIT',
      packages=['scopus_of_science'],
      zip_safe=False)