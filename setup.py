from setuptools import setup

APP = ['data_tables_app.py']
DATA_FILES = ['LICENSE', 'README.md']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['streamlit', 'pandas', 'openpyxl'],
}

setup(
    app=APP,
    name='DataAi',
    version='1.0',
    author='Krishna Gupta',
    author_email='your_email@example.com',
    url='https://github.com/iamkrishnagupta10',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
