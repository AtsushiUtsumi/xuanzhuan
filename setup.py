from setuptools import setup, find_packages

setup(
    name='xuanzhuan',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'jinja2',
    ],
    package_data={'xuanzhuan': ['hoge/hoge.txt','templates/*.j2', 'templates/*.json']},
    include_package_data=True,
)