from urllib.error import HTTPError
from requests.auth import HTTPBasicAuth
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='input code exercise id and subquestion id')   
parser.add_argument('exercise_id', type=str, help='input exercise id')
parser.add_argument('subquestion_id', type=str, help='input subquestion id')
args = parser.parse_args()

print(args.exercise_id)
print(args.subquestion_id)

testMultipleQuestions = args.exercise_id


try:
    # return the response and then convert it to a json object
    response = requests.get("http://academy.aubot.com/api/exercise/" + testMultipleQuestions)
    
    # response = requests.get("http://academy.aubot.com/api/exercise/MultiChoicePostTest")
    # response = requests.get("http://academy.aubot.com/api/exercise/testMultipleQuestions")
    
    response.raise_for_status()
    
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    
    response_json = response.json()
    response_questions = response_json["questions"]
    
    # this should allow access to the dictionary of the json object
    # "_id": "testMultipleQuestions-0",
    # "data": ["A", "B"]
      
    
    
    # response_data = response_json["questions"]
    # # set response_data to the data of the subquestion with id subquestion_id
    # for element in response_json["questions"]:
    #     if element["id"] == int(args.subquestion_id):
    #         response_data = element["textInput"]
    # print(response_data)
            
    # response_choices = response_json["questions"]
    # # set response_choices to the choices of the subquestion with id subquestion_id
    # for element in response_json["questions"]:
    #     if element["id"] == int(args.subquestion_id):
    #         response_choices = element["choices"]
    # print(response_choices)
    
    # question_type = "undefined"
    # for element in response_json["questions"]:
    #     if element["id"] == int(args.subquestion_id):
    #         question_type = element["type"]
    # print(question_type)
    # invalid = False
    
    response_data = response_questions[int(args.subquestion_id)]
    
    question_type = response_data["type"]
    
    response_choices = response_data["choices"]
    
    response_data = response_data["choices"]
    
    # test if it works
    response_data = ["B", "C"]
    
    if question_type == "multi-choice" or question_type == "true-false":
        # check if data is within the choices
        print("Data was checked for validity")
        for element in response_data:
            invalid = True
            for option in response_choices:
                if element == option:
                    # print("correct")
                    invalid = False
            print(invalid)
            if invalid == True:
                print("Error: Invalid answer")
                break
    else:
        print("Data was not checked for validity")
                    
    if invalid == True:
        response_data = ["Error: Invalid answer"]
        # there is an error in the response data so no post request will be made
    else:
        response_post = {
            "_id": response_json["_id"] + "-" + args.subquestion_id ,
            "data": response_data
        }
        try:
            # post request
            url = "https://academy.aubot.com/api/tests/mc"
            payload = json.dumps({
                 "_id": response_json["_id"] + "-" + args.subquestion_id ,
                "data": response_data
            })
            headers = {
                 'Authorization': 'Basic dXBkYXRlcjpjLSssLEUsanAyRzRxYkRjKXprMw==',
                 'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # print(response.text)
            response.raise_for_status()
            
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  
        else:
            # if the response code is 201 the save the response data to a JSON file
            print(response.status_code)
            # print(response.text)
            if response.status_code == 201:
                # save the response data to a JSON file
                with open("saved_responses/" + args.subquestion_id + ".json", "w") as outfile:
                    outfile.write(response.text)
            else:
                print("Error: Invalid response code")
                    
    

