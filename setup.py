import os
from codecs import open

from setuptools import find_packages, setup

INSTALL_REQUIRES = ("click<8.1", "elex-solver<2", "pandas<1.5.0", "boto3<2", "python-dotenv==0.19.2")

THIS_FILE_DIR = os.path.dirname(__file__)

LONG_DESCRIPTION = ""
# Get the long description from the README file
with open(os.path.join(THIS_FILE_DIR, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# The full version, including alpha/beta/rc tags
RELEASE = "1.0.9"
# The short X.Y version
VERSION = ".".join(RELEASE.split(".")[:2])

PROJECT = "elex-model"
AUTHOR = "The Wapo Newsroom Engineering Team"
COPYRIGHT = "2022, {}".format(AUTHOR)


setup(
    name=PROJECT,
    version=RELEASE,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    description="A package for the Washington Post's live election night model",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages("src", exclude=["docs", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    command_options={
        "build_sphinx": {
            "project": ("setup.py", PROJECT),
            "version": ("setup.py", VERSION),
            "release": ("setup.py", RELEASE),
        }
    },
    py_modules=["elexmodel"],
    entry_points="""
        [console_scripts]
        elexmodel=elexmodel.cli:cli
    """,
)
