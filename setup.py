from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='mangalib-parser',
    version='1.0.0',
    author='kooflixy',
    description='A library that helps parse site https://mangalib.me',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/kooflixy/mangalib-parser',
    packages=find_packages(),
    install_requires=['requests>=2.32.3'],
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: Unlicense',
    ],
    keywords='parser api mangalib library',
    project_urls={
        'GitHub': 'https://github.com/kooflixy'
    },
    python_requires='>=3.12'
)