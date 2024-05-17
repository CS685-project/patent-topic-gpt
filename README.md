patent-topic-gpt
==============================

Final project for UMass Amherst CS685.
This Repository contains scripts related to dataset generation and processing of results from TopicGPT.
These files are independent of the topicGPT repository and are specific to the Patent Classification objectives. 
This repository also contains the script for BERTopic. 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── jsondump       <- Folders containing information on 12442 patents
    ├── notebooks          
    │   └── agreement        <- Scripts for computing interannotator agreement 
    │   └── assignment      <- Scripts for evaluating topic assignment 
    │   └── baseline        <- BERTopic baseline script
    │   └── data            <- Scripts for cleaning USPTO data and generating samples
    │   └── patent_analysis        <- Scripts for data analysis of USPTO data
    │   └── refinement        <- Scripts for evaluating topicGPT refinement
    │
    ├── reports            
    │   └── figures        <- Generated graphics and figures to be used in the final report
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── _web_scraping  <- Scripts related to scraping USPTO website for zip files
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

