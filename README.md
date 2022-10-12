
![contributors](https://img.shields.io/badge/all_contributors-3-green.svg?style=flat)
![milestones](https://img.shields.io/github/milestones/all/pwerden/ds-ml-flight-delay-prediction)
![contributors](https://img.shields.io/badge/python-3.9.8-blue.svg?style=flat)
![language](https://img.shields.io/github/languages/top/pwerden/ds-ml-flight-delay-prediction)
![license](https://img.shields.io/github/license/pwerden/ds-ml-flight-delay-prediction)
![repo-size](https://img.shields.io/github/repo-size/pwerden/ds-ml-flight-delay-prediction)
![repo-size](https://img.shields.io/github/last-commit/pwerden/ds-ml-flight-delay-prediction)

# ML Project: Flight Delay Prediction Challenge

**Second project at the _neuefische Data Science_ bootcamp 2022.**

---

![](https://media.cntraveler.com/photos/57b1ddf87443947d28477866/master/pass/GettyImages-93466101.jpg­)

---

## Description

This group project aims to predict the delay of aircrafts flying (mostly) from or to the Tunis-Carthage International Airport (TUN) using **regression** models. The data base for this task is from the __zindi__ website which organised the "AI Tunisia Hack 2019" and covers the years 2016 to 2018 with a total of about 100,000 samples in 10 columns (9 features + 1 label).

The data can be found at: 

[https://zindi.africa/competitions/ai-tunisia-hack-5-predictive-analytics-challenge-2](https://zindi.africa/competitions/ai-tunisia-hack-5-predictive-analytics-challenge-2).

Supplementary data for the airports are provided at:

[https://pypi.org/project/airportsdata/](https://pypi.org/project/airportsdata/) 


---
The exploratory data analysis (EDA) can be found in **1_EDA.ipynb**. The notebooks for the different models are in the *model* folder.


---
## Requirements and Environment

Requirements:
- pyenv with Python: 3.9.8

Environment: 

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands: 

```Bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

