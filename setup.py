import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name='opunity-bot',
    version='0.1.0',
    description='Бот для маркетплейса Opunity',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=["Programming Language :: Python", "Topic :: Requests"],
    author='rustam781227 & VadimKarmazin',
    keywords='telebot python',
    packages=find_packages(exclude=['tests', 'examples']),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements("requirements.txt")
)
