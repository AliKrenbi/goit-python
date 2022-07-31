from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    author='Ali Krenbi',
    entry_points = {
                'console_scripts': ['clean=clean_folder.main:main']},
    scripts=['clean_folder/clean.py', 'clean_folder/transformer.py'],
    packages=find_packages(),
    description="Clean folder script"
)