from setuptools import setup, find_packages

setup(
    name='surf_scrap',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'scrape-surf-data = scraper:scrap_surf_data',  # Allowing command-line use of the function
        ]
    },
    description='A simple library to scrape meteo surf data from the website "https://www.surf-report.com/meteo-surf/" and export it to a CSV file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gabriele, Bianca, Bastien',
    author_email='your.email@example.com',
    url='https://github.com/Gabriele3vi/DashboardIsNotFunny/blob/main/',  # GitHub link to modify
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
