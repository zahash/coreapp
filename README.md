## Core Application Structure

This repository has the function of serving as a main skeleton from which
an application project can be initiated. It contains features that are
specific to this author's approach to development but can be adapted for anyone else's needs 
 with some basic tweaking:
 - A config.yml template file for CD/CI with CircleCI
 - PyTest with coverage and strict options for TDD
 - A template for setup.py to facilitate builds
 - Use of \_\_main__.py along with argparser for CLI

#### How to use
The use of this repository consists of cloning its contents into a local
directory, making the necessary modifications, committing and then pushing it
 upstream with the new project into its specific repository.