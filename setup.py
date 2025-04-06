# setup.py
from setuptools import setup, find_packages

setup(
    name="kynium",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kyn = bin.kyn:main',  # Указываем на основной скрипт
        ],
    },
)
