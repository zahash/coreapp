import pathlib
from setuptools import setup, find_packages

"""Edit the contents of this file as necessary for your specific
application's requirements."""

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

NAME = 'core'
DESCRIPTION = 'Some words about core'
LONG_DESCRIPTION_TYPE = "text/markdown"
URL = 'github_repository_url_here'
AUTHOR = 'my_alias'
AUTHOR_EMAIL = 'my_email_address'
REQUIRES_PYTHON = '>=X.Y.Z'
VERSION = 'X.Y.Z'
LICENSE = "MIT"
REQUIRED = ["pytest",
            "setuptools"]
ENTRY_POINTS = {
    "console_scripts": [
        "core=core.__main__:my_cli",
    ]
}
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type=LONG_DESCRIPTION_TYPE,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=("tests",
                                    "venv",
                                    ".pytest_cache")),
    include_package_data=True,
    install_requires=REQUIRED,
    entry_points=ENTRY_POINTS,
)
