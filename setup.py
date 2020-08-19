import setuptools

with open("DESCRIPTION.md", "r") as fh:
    long_description = fh.read()

# Taken largely from https://packaging.python.org/tutorials/packaging-projects/
setuptools.setup(
    name="transfer-message",
    version="0.0.1",
    author="Michael Edwards",
    author_email="medwards@walledcity.ca",
    description="A command line tool for transferring messages between different messaging systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medwards/cli-demo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # see https://python-packaging.readthedocs.io/en/latest/testing.html
    test_suite='nose.collector',
    tests_require=['nose'],
    # see https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
    entry_points = {
        'console_scripts': ['transfermessage=transfer_message.__main__:main'],
    }
)
