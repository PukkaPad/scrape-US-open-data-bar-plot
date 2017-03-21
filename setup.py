try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Analysis of Cancer data from US gov',
    'author': 'Mariana Souza',
    'url': 'https://statecancerprofiles.cancer.gov/',
    'download_url': 'https://statecancerprofiles.cancer.gov/',
    'author_email': 'xxx@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['Get_data.py', 'view_data.py'],
    'name': 'scrape-US-open-data-bar-plot'
}

setup(**config)