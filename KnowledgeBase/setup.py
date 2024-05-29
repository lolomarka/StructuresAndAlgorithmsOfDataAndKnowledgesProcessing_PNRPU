from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='KnowledgeBase',
    version='0.1.0',
    author='Mark Sheretov',
    author_email='mark.sheretov@gmail.com',
    description='Небольшая библиотека для представления базы знаний',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/lolomarka/StructuresAndAlgorithmsOfDataAndKnowledgesProcessing_PNRPU/tree/main/KnowledgeBase',
    packages=find_packages(),
    python_requires='>=3.6',
)