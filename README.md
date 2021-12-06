# CS 410 - Project: Causal Topic Modeling

## Overview

This project is to perform causal topic modeling on MLB (Major League Baseball) articles to analyze the identified hidden trend topics. The performance of the model can be tested by referring the section: [The Software Usage and Testing the Software](#the-software-usage-and-testing-the-software) without installing anything on your machine, which I suspect most people prefer. Additionally, I introduce [The Software Development and Installation](#the-software-development-and-installation) in case you would like to setup the same development environment of this project to run the code.

## Author

### Team: MP

| Name                | NetId                 |
| ------------------- | --------------------- |
| Masami Peak         | masamip2@illinois.edu |

## Table of Contents

- [Introduction](#introduction)
- [LDA Algorithm](#lda-algorithm)
- [The Software Usage and Testing the Software](#the-software-usage-and-testing-the-software)
- [The Software Implementation](#the-software-implementation)
- [The Software Usage Tutorial Presentation](#the-software-usage-tutorial-presentation)
- [The Software Development and Installation](#the-software-development-and-installation)
  - [Prerequisites](#prerequisites)
  - [Python Modules and Tools Used on Windows](#python-modules-and-tools-used-on-windows)
  - [Project File Structure](#project-file-structure)
  - [Project Steps](#project-steps)
    - [1 Downloading the Project Source Code](#1-downloading-the-project-source-code)
    - [2 Setting Up the Local Environment](#2-setting-up-the-local-environment)
      - [2_1 Python and Pip Installation](#2_1-python-and-pip-installation)
      - [2_2 Finding Out Available Python and Pip Versions](#2_2-finding-out-available-python-and-pip-versions)
      - [2_3 Jupyter Notebook Installation](#2_3-jupyter-notebook-installation)
      - [2_4 Setting Up Virtual Environment](#2_4-setting-up-virtual-environment)
    - [3 Web Crawling to Obtain MLB Related Articles](#3-web-crawling-to-obtain-mlb-related-articles)
      - [3_1 ChromeDriver Installation](#3_1-chromedriver-installation)
      - [3_2 Start Web Crawling](#3_2-start-web-crawling)
    - [4 Data Preprocessing and Topic Modeling Analysis](#4-data-preprocessing-and-topic-modeling-analysis)
      - [4_1 Start Jupyter Notebook](#4_1-start-jupyter-notebook)
      - [4_2 Run the mlb notebook](#4_2-run-mlb-notebook)

## Introduction

Each annual MVP (Most Valuable Player) in the 2 leagues is determined by the voters in [the Baseball Writers’ Association of America](https://bbwaa.com/voting-faq). Because of this, topic modeling on the MLB related articles published before the MVP announcement can be used to discover the key topics correlated to the MVP for the year.

## LDA Algorithm

LDA: Latent Dirichlet Allocation is the most popular topic model and extracts the topics discussed in the documents. In LDA model, each document has a vector of topics as a topic distribution, and each topic has a vector of words as a word distribution. The topic distribution is forced to be drawn from its Dirichlet distribution with the vector of α parameters, and the word distribution is forced to be drawn from its Dirichlet distribution with the vector of β parameters.

__<u>k Topics Probability Distribution (from Dirichlet Distribution) on d-th Document πd</u>__

p(πd)

= (p(πd,1), p(πd,2), ..., p(πd,k))

= (Dirichlet(α1), Dirichlet(α2), ..., Dirichlet(αk))

= p(θ)

= (p(θ1), p(θ2), ..., p(θk))

__<u>m Words Distribution on i-th Topic θi</u>__

p(W|θi)

= (p(w1|θi), p(w2|θi), ..., p(wm|θi))

= (Dirichlet(β1), Dirichlet(β2), ..., Dirichlet(βm))

## The Software Usage and Testing the Software

Please go to [Online Jupyter Notebook](https://mybinder.org/v2/gh/masamip2/CourseProject/HEAD) of this project and see the section 'How to Use/Test the Software' in the [ProjectReport.pdf](/ProjectReport.pdf) for the details of the software usage and testing the software.

## The Software Implementation

Please see the section 'How the Software Implemented' in the [ProjectReport.pdf](/ProjectReport.pdf) for the details of the software  implementation.

## The Software Usage Tutorial Presentation

Please watch the [Project Presentaion](https://mediaspace.illinois.edu/media/t/1_7h9807wh) for the software usage tutorial.

## The Software Development and Installation

The rest of the entire section below is extra detailed documentation for how to develop and install the software on Windows 10 Pro (21H1), Mac (Catalina 10.15.7) or Linux (Ubuntu 20.04). The information will be useful if you would like to setup the development environment of the software.

### Prerequisites

Python 3.9, Jupyter Notebook 6.4.5, ChromeDriver (Optional) 

### Python Modules and Tools Used on Windows

   | Module / Tool           | Version      | Usage                    | Reference
   | ----------------------- | ------------ | ------------------------ | ---------------------------------------------------------------------------------------- |
   | Python                  | 3.9.4        | Programming Language     | <https://www.python.org/>                                                                |
   | Python Built-in Modules | 3.9.4        | Commonly Used Functions  | calendar, csv, datetime, os, string, re, importlib.util, subprocess, sys, warnings       |
   | Jupyter Notebook        | 6.4.5        | Simulating Code          | <https://www.python.org/>                                                                |
   | bs4 for BeautifulSoup   | 0.0.1        | Web Scraping             | <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>                                 |
   | selenium for webdriver  | 4.0.0        | Controlloring Browser    | <https://selenium-python.readthedocs.io/getting-started.html>                            |
   | pandas                  | 1.3.4        | DataFrame                | <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>                     |
   | nltk                    | 3.6.5        | Stemming & Lemmatization | <https://www.nltk.org/howto/stem.html> <https://www.nltk.org/api/nltk.stem.wordnet.html> |
   | gensim                  | 4.1.2        | Topic Modeling           | <https://radimrehurek.com/gensim/models/phrases.html>                                    |
   | matplotlib for pyplot   | 3.4.3        | Graphical Plotting       | <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html>                       |
   | pyLDAvis                | 3.3.1        | LDA model visualization  | <https://pypi.org/project/pyLDAvis/>                                                     |
   | Chrome                  | 94.0.4606.71 | Google Browser           | <https://www.google.com/chrome/>                                                         |
   | ChromeDriver            | 94.0.4606.61 | Executing Webapps        | <https://chromedriver.chromium.org/downloads>                                            |

### Project File Structure

```
masamip2/CourseProject (CourseProject-main.zip)
|   mlb.ipynb - for topic modeling and analyzing the outcome
|   ProjectProgress.pdf
|   ProjectProposal.pdf
|   ProjectReport.pdf
|   README.md
|   scraper.py - for web crawling
└───Data/
|   |   articles.csv (the dataset for reproducing the report)
|   |   (the datasets for producing the articles.csv)
|   |   espn.csv - from espn.com
|   |   mlb.csv - from mlb.com
|   |   mvps.csv - a list of the annual MVP in 2 leagues from 2011 to 2021
|   |   nyt.csv - from nytimes.com
|   |   reuters.csv - from reuters.com
|   |   wsj.csv - from wsj.com
└───Model/ (this directory will be created only if to_save=True is configured in the mlb notebook)
|   |   topic_model_{year}.pkl (the LDA model can be saved per {year})

```

### Project Steps

This project has 4 different steps:

1. Downloading the Project Source Code
2. Setting Up the Local Environment
3. Web Crawling to Obtain MLB Related Articles
4. Data Preprocessing and Topic Model Analysis

#### 1 Downloading the Project Source Code

Please follow the steps below to download the project zip file.

1. Go to https://github.com/masamip2/CourseProject .
2. Click 'Code' button.
3. Choose 'Download ZIP'.

NOTE: Alternatively, you can clone the project repository, if you prefer to use GIT.

```bash
git clone https://github.com/masamip2/CourseProject.git
```

#### 2 Setting Up the Local Environment

#### 2_1 Python and Pip Installation

This project has a working condition on:

- Windows 10 Pro (21H1): Python 3.9.4
- Mac (Catalina 10.15.7): Python 3.9.7
- Linux (Ubuntu 20.04): Python 3.9.7

If your Python version is different from any of the versions above, please see the section __Python and Pip Installation__ [Windows](#python-and-pip-installation-on-windows),  [Mac](#python-and-pip-installation-on-mac) and [Linux](#python-and-pip-installation-on-linux) to consider installing the supported version of Python for this project. Pip is already installed with Python 3.4+.

#### 2_2 Finding Out Available Python and Pip Versions

If Python and Pip versions are not up to date, please see the section __Finding Out Available Python and Pip Versions__ [Windows](#finding-out-available-python-and-pip-versions-on-windows), [Mac](#finding-out-available-python-and-pip-versions-on-mac), [Linux](#finding-out-available-python-and-pip-versions-on-linux) to upgrade the versions.

#### 2_3 Jupyter Notebook Installation

If Jupyter Notebook is not installed or the version is not up to date, please see the section __Jupyter Notebook Installation__ [Windows](#jupyter-notebook-installation-on-windows), [Mac](#jupyter-notebook-installation-on-mac), [Linux](#jupyter-notebook-installation-on-linux).

#### 2_4 Setting Up Virtual Environment

Please see the section __Setting Up Virtual Environment__ [Windows](#setting-up-virtual-environment-on-windows), [Mac](#setting-up-virtual-environment-on-mac), [Linux](#setting-up-virtual-environment-on-linux) to setup the virtual environment 'mlb' for this project. Venv is already installed with Python 3.3+.

#### 3 Web Crawling to Obtain MLB Related Articles

This step is __OPTIONAL__, because it will take about 1 hour 40 minutes to complete web crawling. Also, due to the available articles being updated on the corresponding sites, the fetched articles will be slightly different from the datasets already provided in this project. Moreover, there is a chance that the scraper.py has to run multiple times on some of those article sites where the advertisements and the pop-ups maybe cause some kind of issue.

#### 3_1 ChromeDriver Installation

1. Check your Chrome version: Click right-top corner on the browser for settings.

2. 'Help' -> 'About Google Chrome' -> Version (the examples below):

- Windows 10 Pro (21H1): Version 94.0.4606.81 (Official Build) (64-bit)
- Mac (Catalina 10.15.7): Version 95.0.4638.69 (Official Build) (x86_64)
- Linux (Ubuntu 20.04): Version 95.0.4638.54 (Official Build) (64-bit)

3. Go to https://chromedriver.chromium.org/downloads , click a link for the downloading page, download the appropriate chromedriver zip file, unzip the file and place the executable driver file at 1 level above the scraper.py:

- Windows 10 Pro (21H1): ChromeDriver 94.0.4606.61 -> chromedriver_win32.zip -> chromedriver.exe
- Mac (Catalina 10.15.7): ChromeDriver 95.0.4638.54 -> chromedriver_mac64.zip -> chromedriver
- Linux (Ubuntu 20.04): ChromeDriver 95.0.4638.17 -> chromedriver_linux64.zip -> chromedriver

4. Alternatively, place the driver file at any applicable place and modify a constant 'CHROME_DRIVER_PATH' in the scraper.py for the file path.

5. __NOT ON__ the virtual environment 'mlb', run the chromedriver:

- Windows 10 Pro (21H1): Double-click the chromedriver.exe
- Mac (Catalina 10.15.7): Right-click the chromedriver -> Open -> Open
- Linux (Ubuntu 20.04): Type \~/Documents/CS410/chromedriver in terminal and hit enter key

#### 3_2 Start Web Crawling

__ON__ the virtual environment 'mlb', run the command like below where an argument of site_name has to be replaced by Reuters, MLB, WSJ, NYTimes or ESPN.

#### Windows 10 Pro (21H1) Environment

```bash
py -3.9 scraper.py ESPN # example: web crawling on ESPN.com
```

#### Mac (Catalina 10.15.7) Environment

```bash
python3 scraper.py ESPN # example: web crawling on ESPN.com
```

_NOTE1_: For the first time, a popup will show up asking "'Google Chrome' would like to access files in your Documents folder."

#### Linux (Ubuntu 20.04) Environment

```bash
python3.9 scraper.py ESPN # example: web crawling on ESPN.com
```

_NOTE2_: If the script stops very quickly or gets stuck, please run scraper.py multiple times for the particular article site where the advertisements and the pop-ups maybe cause some kind of issue.

_NOTE3_: Once web crawling is done, you can stop the chromedriver by 'Ctrl' + 'c'.

#### 4 Data Preprocessing and Topic Model Analysis

#### 4_1 Start Jupyter Notebook

__NOT ON__ the virtual environment 'mlb', run the command like below to start Jupyter Notebook.

```bash
cd ~/Documents/CS410/CourseProject-main # go to a suitable directory for the root of Jupyter Notebook tree
jupyter notebook
```

_NOTE1_: In case a browser for Jupyter Notebook does not open up on Mac, copy and paste the url for the host like `http://127.0.0.1:8888/?token={48_Alphanumeric_Characters}` on a browser url bar.

#### 4_2 Run mlb notebook

1. On the automatically opened Jupyter Notebook in a browser, navigate to the file 'mlb.ipynb' and click it.

2. Make sure that the virtual environment 'mlb' has already been created in the step [Setting Up Virtual Environment](#setting_up_virtual_environment), click 'Kernel' -> 'Change kernel' -> select 'mlb'.

3. Click 'Kernel' -> 'Restart & Clear Output' -> click 'Restart and Clear All Outputs' to clear cache.

4. Click 'Cell' -> 'Run All' (alternatively, click 'Run' for each cell one by one).

_NOTE1_: Once all the tasks in Jupyter Notebook are done, you can stop the Jupyter Notebook by 'Ctrl' + 'c'.

_NOTE2_: In 'mlb.ipynb', please ignore one type of DeprecationWarning which is unable to be suppressed when the function gensimvis.prepare() is called for the first time in Python 3.9.7.

# Appendix

## Windows 10 Pro (21H1) Environment

### Python and Pip Installation on Windows

Please follow the steps below as example, only if you do not have Python version 3.9.4. Pip is already installed with Python 3.4+.

1. Go to https://www.python.org/downloads/windows .
2. Look for the section 'Python 3.9.4 - April 4, 2021'.
3. Click 'Download Windows installer (64-bit)'.
4. Double-click the downloaded 'python-3.9.4-amd64.exe' and click 'Install Now'.

_NOTE1_: The Python (python.exe) is, for example, installed at C:\Users\Masami\AppData\Local\Programs\Python\Python39\python.exe .

_NOTE2_: Please follow the steps below in case Pip does not exist in your machine.

1. Downloaded get-pip.py from https://bootstrap.pypa.io/get-pip.py .
2. Alternatively, run the follwoing command.

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

3. Install Pip for the Python on your PATH as User variable.

```bash
python get-pip.py
```

### Finding Out Available Python and Pip Versions on Windows

Please follow the steps below to check your environment.

1. Find out the Python versions in your machine and see the output like below.

```bash
py -0
Installed Pythons found by py Launcher for Windows
 -3.10-64 *
 -3.9-64
 -3.7-64
```

2. Find out the Pip version for the specific Python version.

```bash
py -3.9 -m pip -V
```

3. Upgrade the Pip version for the specific Python version and check to see the latest version like below.

```bash
py -3.9 -m pip install pip --upgrade

py -3.9 -m pip -V
pip 21.3.1 from C:\Users\Masami\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)
```

### Jupyter Notebook Installation on Windows

1. Install Jupyter Notebook for the specific Python version.

```bash
py -3.9 -m pip install notebook --upgrade
```

2. Check to see the latest version like below.

```bash
jupyter notebook -V
6.4.5
```

### Setting Up Virtual Environment on Windows

Venv is already installed with Python 3.3+.

1. Create a virtual environment 'mlb' at the same location as scraper.py and mlb.ipynb.

```bash
cd C:\Users\Masami\Documents\CS410\CourseProject-main
py -3.9 -m venv mlb
mlb\Scripts\activate
```

2. Install ipykernel for running Jupyter Notebook on a kernel inside the virtual environment.

```bash
py -3.9 -m pip install pip --upgrade
py -3.9 -m pip install --user ipykernel
```

3. Add the kernel to Jupyter Notebook and see the output like below.

```bash
py -3.9 -m ipykernel install --user --name=mlb
Installed kernelspec mlb in C:\Users\Masami\AppData\Roaming\jupyter\kernels\mlb
```

4. To delete the kernel and the virtual environment, run the following commands.

```bash
jupyter kernelspec uninstall mlb
deactivate
rmdir /s /q mlb
```

## Mac (Catalina 10.15.7) Environment

### Python and Pip Installation on Mac

Please follow the steps below only if you do not have Python version 3.9.7. Pip is already installed with Python 3.4+.

1. Install Python 3.9.7 and its Pip 21.3.1, and see the output like below.

```bash
brew update && brew upgrade
brew install python3 && brew upgrade python3

python3 -V
Python 3.9.7

pip3 -V
pip 21.2.4 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
```

_NOTE1_: Refer the following steps, in case you want to clean up your python3 environment.

1. Remove all the symbolic links to python and pip.

```bash
sudo rm /usr/local/bin/python*
sudo rm /usr/local/bin/pip*
```

2. Remove versions of Python in the Python.framework.

```bash
sudo rm -rf /Library/Frameworks/Python.framework/Versions/*
```

3. Check your PATH environment variables in \~/.bash_profile.

```bash
export PATH=/usr/local/bin:/usr/local/sbin:${PATH}
```

4. Uninstalling python3 first could make reinstalling python3 easier depending on your situation. 

```bash
brew uninstall --ignore-dependencies python3
```

_NOTE2_: The Python is installed at /usr/local/Cellar/python@3.9/3.9.7_1/bin/python3 .


### Finding Out Available Python and Pip Versions on Mac

Please follow the steps below to check your environment.

1. Find out the detail of Python3 version on your PATH and see the output like below.

```bash
python3 -V
Python 3.9.7
```

2. Find out the Pip version for the specific Python version.

```bash
python3 -m pip -V
```

3. Upgrade the Pip version for the specific Python version and check to see the output like below.

```bash
python3.9 -m pip install pip --upgrade

python3 -m pip -V
pip 21.3.1 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
```

### Jupyter Notebook Installation on Mac

1. Install Jupyter Notebook for the specific Python version.

```bash
python3 -m pip install notebook --upgrade
```

2. Check to see the latest version like below.

```bash
jupyter notebook -V
6.4.5
```

### Setting Up Virtual Environment on Mac

Venv is already installed with Python 3.3+.

1. Create a virtual environment 'mlb' at the same location as scraper.py and mlb.ipynb.

```bash
cd ~/Documents/CS410/CourseProject-main
python3 -m venv mlb
source mlb/bin/activate
```

2. Install ipykernel for running Jupyter Notebook on a kernel inside the virtual environment.

```bash
python3 -m pip install pip --upgrade
python3 -m pip install ipykernel
```

3. Add the kernel to Jupyter Notebook and see the output like below.

```bash
python3 -m ipykernel install --user --name=mlb
Installed kernelspec mlb in /home/masami/.local/share/jupyter/kernels/mlb
```

4. To delete the kernel and the virtual environment, run the following commands.

```bash
jupyter kernelspec uninstall mlb
deactivate
rm -r
```

## Linux (Ubuntu 20.04) Environment

### Python and Pip Installation on Linux

Please follow the steps below only if you do not have Python version 3.9.7.

1. Install Python 3.9.7 and its Pip 21.3.1, and see the output like below. Pip is already installed with Python 3.4+.

```bash
sudo apt update && sudo apt upgrade
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.9
python3.9 -V
python3.9.7

python3.9 -m pip install pip --upgrade
python3.9 -m pip -V
pip 21.3.1 from /home/masami/.local/lib/python3.9/site-packages/pip (python 3.9)
```

_NOTE1_: The Python is installed at /usr/bin/python3.9 .

_NOTE2_: In case you see the warning below, the command like below makes the Pip to be on your PATH.

WARNING: The scripts pip, pip3 and pip3.9 are installed in '/home/masami/.local/bin' which is not on PATH.

```bash
echo "export PATH=\"/home/masami/.local/bin:\$PATH\"" >> ~/.bashrc && source ~/.bashrc
```

### Finding Out Available Python and Pip Versions on Linux

Please follow the steps below to check your environment.

1. Find out the detail of Python3.9 version at /usr/bin on your machine and see the output like below.

```bash
python3.9 -V
Python 3.9.7
```

2. Find out the Pip version for the specific Python version.

```bash
python3.9 -m pip -V
```

3. Upgrade the Pip version for the specific Python version and check to see the output like below.

```bash
python3.9 -m pip install pip --upgrade

python3.9 -m pip -V
pip 21.3.1 from /home/masami/.local/lib/python3.9/site-packages/pip (python 3.9)
```

### Jupyter Notebook Installation on Linux

1. Install Jupyter Notebook for the specific Python version.

```bash
python3.9 -m pip install notebook --upgrade
```

2. Check to see the latest version like below.

```bash
jupyter notebook -V
6.4.5
```

### Setting Up Virtual Environment on Linux

0. Install Venv.

```bash
sudo apt-get install python3.9-venv
```

1. Create a virtual environment 'mlb' at the same location as scraper.py and mlb.ipynb.

```bash
cd ~/Documents/CS410/CourseProject-main
python3.9 -m venv mlb
source mlb/bin/activate
```

2. Install ipykernel for running Jupyter Notebook on a kernel inside the virtual environment.

```bash
python3.9 -m pip install pip --upgrade
python3.9 -m pip install ipykernel
```

3. Add the kernel to Jupyter Notebook and see the output like below.

```bash
python3.9 -m ipykernel install --user --name=mlb
Installed kernelspec mlb in /home/masami/.local/share/jupyter/kernels/mlb
```

4. To delete the kernel and the virtual environment, run the following commands.

```bash
jupyter kernelspec uninstall mlb
deactivate
rm -rf mlb
```
