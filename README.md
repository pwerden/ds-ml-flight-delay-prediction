# ML Project: Flight Delay Prediction Challenge

**Second project at the _neuefische Data Science_ bootcamp 2022.**

## Description

This group project aims to predict the delay of flights from or to the Tunis-Carthage International Airport (TUN) using **regression** models. The data base for this task is from the __zindi__ website which organised the "AI Tunisia Hack 2019" and covers the years 2016 to 2018 with a total of about 100,000 samples in 10 columns (9 features + 1 label).

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

