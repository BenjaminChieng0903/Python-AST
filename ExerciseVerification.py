from urllib.error import HTTPError
import requests
import re


testMultipleQuestions = "testMultipleQuestions"


try:
    # return the response and then convert it to a json object
    response = requests.get("academy.aubot.com/api/exercise/" + testMultipleQuestions)
    
    response.raise_for_status()
    
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    response_json = response.json()
    
    # this should allow access to the dictionary of the json object
    # "_id": "testMultipleQuestions-0",
    # "data": ["A", "B"]
    response_data = response_json["data"]
    response_choices = response_json["choices"]
    invalid = False
    
    if response_json["qType"] == "mc" or response_json["qType"] == "tf":
        # check if data is within the choices
        for element in response_data:
            for option in response_choices:
                if element == option:
                    print("correct")
                else:
                    print("incorrect")
                    invalid = True
    if invalid == True:
        response_data = ["Error: Invalid answer"]
    else:
        response_post = {
            "_id": response_json["_id"],
            "data": response_data
        }
try:
    # post request
    requests.post("academy.aubot.com/api/tests/mc", data = response_post)
    
    response.raise_for_status()
    
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    response_data = response.json()
    

