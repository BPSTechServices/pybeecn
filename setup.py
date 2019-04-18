from setuptools import setup, find_packages
import logging
logging.basicConfig(level=logging.INFO)


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# Install dependencies
install_deps = []

test_deps = install_deps + ['pytest~=3.4', 'pytest-mock', 'pytest-profiling', 'pytest-benchmark']

analysis_deps = install_deps + test_deps + [
    'matplotlib',
    'numpy',
    'pandas',
    'folium'
]

setup(
    name='pybeecn',
    long_description=readme,
    author='Gabriel McBride',
    author_email='gabe.l.mcbride@gmail.com',
    url='https://github.com/glmcbr06/pybeecn',
    setup_requires=['setuptools_scm'],
    tests_require=test_deps,
    use_scm_version=True,
    install_requires=install_deps,
    include_package_data=True,
    extras_require={
        'tests': test_deps
    },
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'pybeecn.subcommands': [
            'vis = pybeecn.vis.cli'
        ],
        'console_scripts': [
            'pybeecn=pybeecn.cli:run'
        ]
    }
)
