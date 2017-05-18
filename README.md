# Pluralsight Scraper
 [![GitHub issues](https://img.shields.io/github/issues/Stormiix/pluralsight_scraper.svg?style=flat-square)](https://github.com/Stormiix/pluralsight_scraper/issues)
[![GitHub forks](https://img.shields.io/github/forks/Stormiix/pluralsight_scraper.svg?style=flat-square)](https://github.com/Stormiix/pluralsight_scraper/network)
[![GitHub stars](https://img.shields.io/github/stars/Stormiix/pluralsight_scraper.svg?style=flat-square)](https://github.com/Stormiix/pluralsight_scraper/stargazers)

Allows you to fetch & download the courses on PluralSight - MUST HAVE AN ACCOUNT IN ORDER TO DOWNLOAD
## Setup

1. Clone the repository

```
  git clone https://github.com/Stormiix/pluralsight_scraper.git
```

## Installation

1. Install Python

2. Install pip

3. Install packages from requirements.txt

```
  pip install -r requirements.txt
```

## Configure the tool

1. Create a new file config.py and add the following:
```
    Username = "Your PluralSight Email/Username"
    Password = "Your PluralSight Password"
```
2. Modify pluralsight.py and change both lines 10 & 11:

```
    title = "COURSE TITLE"
    link = "COURSE PLAYER URL"
```
P.S : You can also change the scraper's delay time, by default it's 3sec

## Run the tool

```
  python pluralsight.py
```
