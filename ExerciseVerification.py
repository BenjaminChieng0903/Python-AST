from urllib.error import HTTPError
import requests
import argparse

parser = argparse.ArgumentParser(description='input code exercise id and subquestion id')   
parser.add_argument('exercise_id', type=str, help='input exercise id')
parser.add_argument('subquestion_id', type=str, help='input subquestion id')
args = parser.parse_args()

# now print the exercise id and subquestion id  
print(args.exercise_id)
print(args.subquestion_id)

testMultipleQuestions = args.exercise_id


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
      
    
    
    response_data = response_json["questions"]
    # set response_data to the data of the subquestion with id subquestion_id
    for element in response_data:
        if element["id"] == args.subquestion_id:
            response_data = element["data"]
            
    response_choices = response_json["questions"]
    # set response_choices to the choices of the subquestion with id subquestion_id
    for element in response_choices:
        if element["id"] == args.subquestion_id:
            response_choices = element["choices"]
            
    invalid = False
    
    if response_json["type"] == "multi-choice" or response_json["type"] == "true-false":
        # check if data is within the choices
        for element in response_data:
            for option in response_choices:
                if element == option:
                    print("correct")
                else:
                    print("incorrect")
                    invalid = True
    else:
        print("Data was not checked for validity")
                    
    if invalid == True:
        response_data = ["Error: Invalid answer"]
        # there is an error in the response data so no post request will be made
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
            # if the response code is 201 the save the response data to a JSON file
            if response.status_code == 201:
                # save the response data to a JSON file
                with open("response.json", "w") as outfile:
                    outfile.write(response.text)
            else:
                print("Error: Invalid response code")
                    
    

