from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Clean folder script',
    author='Ali Krenbi',

    #packages=find_packages(),
    entry_points = {
            'console_scripts': ['clean=clean_folder.cleaner:main']},
)