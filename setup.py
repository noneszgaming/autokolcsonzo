from setuptools import setup, find_packages

setup(
    name='autokolcsonzo_project',  # Add meg a projekt nevét
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'run_autokolcsonzo=autokolcsonzo.main:main',  # itt állítjuk be, hogy a `main:main` függvény fut
        ],
    },
)