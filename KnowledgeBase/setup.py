from setuptools import setup, find_packages

setup(
    name='KnowledgeBase',
    version='0.1.0',
    author='Mark Sheretov',
    author_email='mark.sheretov@gmail.com',
    description='Небольшая библиотека для представления базы знаний',
    long_description=open('README.md').read(),
    url='https://github.com/lolomarka/StructuresAndAlgorithmsOfDataAndKnowledgesProcessing_PNRPU/tree/main/KnowledgeFrames',
    packages=find_packages(),
    python_requires='>=3.6',
)