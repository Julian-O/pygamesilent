"""  pygamesilent setup module.
Cribbed from: https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygamesilent',
    version='0.1.2',
    description='Shim around PyGame to hide "Hello" message on import.',
    long_description=long_description,
    url='https://github.com/Julian-O/pygamesilent',
    author='Julian-O',
    author_email='pygamesilent@somethinkodd.com',
    classifiers=[
        'Development Status:: 3 - Alpha',
        'Programming Language:: Python',
        'Intended Audience:: Developers',
        'License:: OSI Approved:: MIT License',
        'Operating System:: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic:: Software',
        'Development:: Libraries:: pygame'
    ],
    keywords='pygame shim',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=['pygame'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['pytest', 'pytest-cov'],
    },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'PyGame Info': 'https://pygame.org',
        'Source': 'https://github.com/Julian-O/pygamesilent/',
    },
)
