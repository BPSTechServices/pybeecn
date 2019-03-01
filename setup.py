from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    liscense = f.read()

# Install dependencies

# install_deps = []
#
# test_deps = install_deps + ['pytest~=3.4', 'pytest-mock', 'pytest-profiling', 'pytest-benchmark']
#
# analysis_deps = install_deps + test_deps + [
#     'matplotlib',
#     'numpy',
#     'pandas'
# ]

setup(
    name='pybeecn',
    description='A package that will provide command line interface tools for analysis',
    long_description=readme,
    author='Gabriel McBtide',
    author_email='gabe.l.mcbride@gmail.com',
    url='https://github.com/glmcbr06/pybeecn',
    setup_requires=['setuptools_scm'],
    tests_require=test_deps,
    use_scm_version=True,
    install_require=install_deps,
    include_package_data=True,
    extra_require={
        'tests': test_deps
    },
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'beecn.subcommands': [
            'view = pybeecn.vis.cli'
        ],
        'console_scripts':[
            'beecn=pybeecn.cli:run'
        ]
    }
)
