# fanxu_template
Data engineering individual project #1

[![Install](https://github.com/nogibjj/fanxu_template/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/fanxu_template/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/fanxu_template/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/fanxu_template/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/fanxu_template/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/fanxu_template/actions/workflows/test.yml)

[![Format](https://github.com/nogibjj/fanxu_template/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/fanxu_template/actions/workflows/format.yml)


Requirements

The project structure must include the following files:
- Jupyter Notebook with: 
    - Cells that perform descriptive statistics using Polars or Panda.
    - Tested by using nbval plugin for pytest
- Makefile with the following:
    - Run all tests (must test notebook and script and lib)
    - Formats code with Python black
    - Lints code with Ruff
    - Installs code via:  pip install -r requirements.txt
- test_script.py to test script
- test_lib.py to test library
- Pinned requirements.txt
- Gitlab Actions performs all four Makefile commands with badges for each one in the README.md

Dataset
- Basketball Referemce 2023-2024 NBA Player Stats: Per Game
    - https://www.basketball-reference.com/leagues/NBA_2024_per_game.html#per_game_stats

Required Files

- requirements.txt
    - required dependencies to run this file
    - provides required versions of devops and web components
- Makefile
    - instructions to install, format, lint, and test python files
- devcontainer
    - devcontainer.json
        - contains docker container for python 3 dependencies
- script.py
    - contains code to use pandas to read dataset, generate summary statistics, visualization, and a report
- lib.py
    - contains shared code between script.py and notebook
- test_script.py
    - contains code to test main.py file
- test_lib.py
    - tests lib.py file
- worflows
    - install.yml
        - installs required python packages and dependencies
    - lint.yml
        - lints python code
    - test.yml
        - performs tests on required python files
    - format.yml
        - properly formats code
- .gitignore
    - ignores unecessary files and programs to prevent installation conflicts

Steps
- set up github repository files such as requirements.txt, Makefile, devcontainer, hello.yml, etc.
- create script.py file containing python script to load in CSV file, create summary statistics, plot visualization, and generate a summary report
- test script.py file by making a test_script.py file
- perform a CI/CD run verifying that the code has passed all the linters and tests

Video Walkthrough:

https://youtu.be/hxRWFt41aqw