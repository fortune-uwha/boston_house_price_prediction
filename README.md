# Boston House Price Prediction App
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![](https://github.com/fortune-uwha/boston_house_price_prediction/blob/main/assets/boston_welcome_page.jpg)

## Table of Contents
* [General Information](#general-information)
* [Usage](#usage)
* [Features](#features)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
The web app is intended for predicting hiouse prices in Boston, United States. Model was trained on the  predefined and cleaned [dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston) and can predict price by given parameters. Trained model is saved to model.pkl file.

## Usage
The API endpoint is a Flask app hosted on heroku https://boston-predictions.herokuapp.com which you can access with any REST API client, such as Postman. There is only one main route:

/predict - takes POST requests, predicts price by parameters provided.

##### Input json format example:
```python
{"inputs": [[6.28807, 0.0, 18.1, 0.0, 0.74, 6.341, 96.4, 2.072, 24.0, 666.0, 20.2, 318.01, 17.79],
            [14.4208, 0.0, 18.1, 0.0, 0.74, 6.461, 93.3, 2.0026, 24.0, 666.0, 20.2, 27.49, 18.05]]}
```
##### Postman usage example:
![](https://github.com/fortune-uwha/boston_house_price_prediction/blob/main/assets/postman_demo.jpg)

* Using Jupyter Notebook
You can also use requests module and use the API in a Jupyter notebook like this:
```python
import json
import requests

predict_url = 'https://boston-predictions.herokuapp.com/predict'
json_input = {"inputs": [[14.4208, 0.0, 18.1, 0.0, 0.74, 6.461,
             93.3, 2.0026, 24.0, 666.0, 20.2, 27.49,
             18.05]]}

response = requests.post(predict_url, data=json.dumps(json_input))
print (f"response: {json.loads(response.content)}")
```
## Project Status
Project is: in progress

## Acknowledgements
This project was based on [Turing College](https://www.turingcollege.com) learning on deploying machine learning models.

## Contact
Created by [@fortune_uwha](https://fortune-uwha.github.io/Fortune_Portfolio/) - feel free to contact me!

## License
This project is open source and available under the terms of the [MIT](https://opensource.org/licenses/MIT) license.


