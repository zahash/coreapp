# Core Application Structure

## Description
This repository has the function of serving as a main skeleton from which
an application project can be initiated. It contains features that are
specific to this author's approach to development but can be adapted for anyone else's needs 
 with some basic tweaking:
 - A config.yml template file for CD/CI with CircleCI
 - PyTest with coverage and strict options for TDD
 - A template for setup.py to facilitate builds
 - Use of \_\_main__.py along with argparse for CLI

## How to use
The use of this repository consists of cloning its contents into a local
directory, **making the necessary modifications**, committing and then
 pushing it upstream with the new project into its specific repository.
 
 This project is structured in a way that anyone can tailor it to their needs by
 simply "trimming" the excesses (or deleting whatever is deemed unnecessary).
 
 #### "I don't use Continuous Integration or CircleCI's service..."
 *Delete the directory named ".circleci":*

```user@host:~/coreapp$ rm -rf .circleci```

#### "I don't do Test-Driven Development or use PyTest..." 
*Delete the directory named "tests" and the file "conftest.py":*

```
user@host:~/coreapp$ rm -rf tests
user@host:~/coreapp$ rm conftest.py
```

#### "I don't need to build my scripts into a package..."
*Delete the files requirements.txt and setup.py:*

```user@host:~/coreapp$ rm requirements.txt setup.py```

#### "My script doesn't need a CLI or do I use argparse..."
*Either delete the contest of the __main__.py file and leave it blank or get
rid of the entire file itself:*

```user@host:~/coreapp$ rm core/__main__.py```
