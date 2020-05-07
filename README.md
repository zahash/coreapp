# Python 3 Core Application Structure

This repository has the function of serving as a main skeleton from which
an application project can be initiated. It contains features that are
specific to this author's approach to development but can be adapted for anyone else's needs 
 with some basic tweaking:
 - A config.yml template file for CD/CI with CircleCI
 - PyTest with coverage and strict options for TDD
 - A template for setup.py to facilitate builds
 - Use of \_\_main__.py along with argparse for CLI

## Usage
The use of this repository consists of simple steps:
1. Forking it to your remote repository on GitHub.
2. Cloning its contents into a local directory on your system.
3. **Making the necessary modifications** as outlined below.
4. Committing and then pushing the new project upstream to your own remote
 repository.
 
 This project is organized in a way that anyone can tailor it to their needs by
 simply "trimming" the excesses (or deleting whatever is deemed unnecessary
 ). Following Step 3 is as simple as adapting the file structure to fit your
  specific needs by evaluating your own use cases. That being said...
 
### "... If you don't use Continuous Integration or CircleCI's service, then..."
 *Delete the directory named ".circleci":*

```user@host:~/coreapp$ rm -rf .circleci```

### "... If you don't do Test-Driven Development or use PyTest, then..." 
*Delete the directory named "tests" and/or the file "conftest.py":*

```
user@host:~/coreapp$ rm -rf tests
user@host:~/coreapp$ rm conftest.py
```

### "... If you don't need to build your scripts into a package, then..."
*Delete the files requirements.txt and setup.py:*

```user@host:~/coreapp$ rm requirements.txt setup.py```

### "... If your script doesn't need a CLI or do you use argparse, then..."
*Either delete the contents of the __main__.py file and leave it blank or get
rid of the entire file itself:*

```user@host:~/coreapp$ rm core/__main__.py```

### "... If your scripts don't produce any kind of data files, then..."
*Delete the data directory:*

```user@host:~/coreapp$ rm -rf data```
