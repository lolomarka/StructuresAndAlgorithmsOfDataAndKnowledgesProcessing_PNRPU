from setuptools import setup, find_packages

setup(
    name='KnowledgeFrames',
    version='0.1.0',
    author='Mark Sheretov',
    author_email='mark.sheretov@gmail.com',
    description='Небольшая библиотека для представления KnowledgeFrame',
    long_description=open('README.md').read(),
    url='https://github.com/lolomarka/StructuresAndAlgorithmsOfDataAndKnowledgesProcessing_PNRPU/tree/main/KnowledgeFrames',
    packages=find_packages(where='KnowledgeFrames'),
    python_requires='>=3.6',
)