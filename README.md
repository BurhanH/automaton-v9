# Automaton-v9

Automation testing framework (UI, Visual) - an example. Based on Python, OpenCV (Open Source Computer Vision Library), Selenium, and Unittest

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v9/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7cdc286cad594d3ab1cec707c33007bf)](https://app.codacy.com/app/BurhanH/automaton-v9?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v9&utm_campaign=Badge_Grade_Settings)
[![HitCount](http://hits.dwyl.com/BurhanH/automaton-v9.svg)](http://hits.dwyl.com/BurhanH/automaton-v9)


## Requirements
Python 3.7.\*, Selenium 3.141.0, Unittest, Open CV 4.1.* <br>
virtualenv (virtual environment manager), <br> 
Firefox 75.0, geckodriver 0.26.0, <br>
Chrome 81.0.4044.122, chromedriver 81.0.4044.69 <br>

## Project structure
```text
-- automaton-v9
   |-- .gitattributes
   |-- .gitignore
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   |-- utils.py
   |-- bad_template.png
   |-- google_template.png
   |-- buttons_template.png
   |-- search_template.png
   `-- tests
       |-- test.py
   `-- results_example
       |-- home_page.png
       |-- google_template_result.png
       |-- buttons_template_result.png
       |-- search_template_result.png
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/)
2) Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v9` folder, and execute command `pip install -r requirements.txt`
5) Install Firefox
6) Download, extract and move geckodriver into `bin` folder for Mac/Linux, `Scripts` folder for Windows on virtual environment

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment
4) Move to `automaton-v9` folder
5) Execute `python -m unittest discover tests "*.py" -v`

## How to run test/s in Chrome browser
Go to any UI scenario and change the value of the `BROWSER` variable from `firefox` to `chrome`. <br> Note! Before execution read steps 5-6 from [How to prepare environment](https://github.com/BurhanH/automaton-v9#how-to-prepare-environment) section

## Technology stack and helpful info
[Python 3.7](https://docs.python.org/3.7/)<br>
[virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) <br>
[GitHub, cloning repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) <br>
[OpenCV, Open Source Computer Vision Library](https://opencv.org/) <br>
[unittest](https://docs.python.org/3.7/library/unittest.html) <br>
[Selenium](https://www.selenium.dev/documentation/en/) <br>
[Firefox](https://www.mozilla.org/en-US/firefox/) <br>
[geckodriver](https://github.com/mozilla/geckodriver/releases) <br>
[Chrome](https://www.google.com/chrome/) <br>
[ChromeDriver](https://chromedriver.chromium.org/downloads) <br>

### Actual result (taken screenshot)

![alt text](/results_example/home_page.png "Actual result for home page") <br>

### Visual searching result for google template (google logo)

![alt text](/results_example/google_template_result.png "Result for google logo template") <br>

### Visual searching result for buttons template

![alt text](/results_example/buttons_template_result.png "Result for buttons") <br>

### Visual searching result for search template

![alt text](/results_example/search_template_result.png "Result for google search text field") <br>
