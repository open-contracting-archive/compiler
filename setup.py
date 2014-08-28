from setuptools import setup

setup(
    name='ocds-compiler',
    version='0.0.2',
    description='Compile OCDS releases into records.',
    license='MIT',
    long_description=open("README.md").read(),
    author='Alex Morega, Sarah Bird',
    author_email='public-ocds-dev@webfoundation.org',
    url='https://github.com/open-contracting/compiler',
    packages=['ocds_compiler'],
    install_requires=['simplejson==3.6.0'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)

