import os
import colorama
from colorama import Fore, Style
import json
import pyperclip
import time

os.system('cls')
colorama.init()

# Set EXERCISE_TEST_FILE_LOCATION to avoid entering Exercise Test File Path only if the exercise test file name is the ID of its corresponding exercise.
EXERCISE_TEST_FILE_LOCATION = "" # Make sure to escape backslashes.

# Change the below constansts if using a language other than Python.
FILE_EXTENSION = ".py"
CODE_DELIMITER = "# Student Code"
LANGUAGE_ID = 71 # Python: 71, Java: 62

while (True):
    try:
        """Read Exercise Test Code File"""
        id = input(Style.BRIGHT + "Enter Exercise Id: " + Style.RESET_ALL)

        if (EXERCISE_TEST_FILE_LOCATION and len(EXERCISE_TEST_FILE_LOCATION) > 1): # If EXERCISE_TEST_FILE_LOCATION exists ...
            exercise_test_file_path = EXERCISE_TEST_FILE_LOCATION + id + FILE_EXTENSION # create exercise_test_file_path automatically.
            print(Fore.LIGHTGREEN_EX + "\nUsed EXERCISE_TEST_FILE_LOCATION and ID to generate the Exercise Test File Path!" + Style.RESET_ALL)
        else:
            exercise_test_file_path = input(Style.BRIGHT + "Enter Exercise Test Code File Path: " + Style.RESET_ALL) # Otherwise, ask for exercise_test_file_path.

        file_split = exercise_test_file_path.split('/')
        file_prefix = file_split[len(file_split)-1].removesuffix(FILE_EXTENSION)
        print(file_prefix)
        exercise_test_file = open(exercise_test_file_path, "r")

        code = exercise_test_file.read()

        """Calculate Code Delimiter Indices"""
        first_code_delimiter_index = code.index(CODE_DELIMITER) + len(CODE_DELIMITER)
        if (code[first_code_delimiter_index:first_code_delimiter_index + 1] == "\n"): # If there is a newline after the first code delimiter ...
            first_code_delimiter_index += 1 # add it to the index.

        second_code_delimiter_index = code.index(CODE_DELIMITER, first_code_delimiter_index)
        if (code[second_code_delimiter_index - 5:second_code_delimiter_index] == "\n    "): # If there is tab and a newline before the second code delimiter ...
            second_code_delimiter_index -= 5 # subtract them from the index.
        elif (code[second_code_delimiter_index - 9:second_code_delimiter_index] == "\n        "): # If there are 2 tabs and newline before the second code delimiter ...
            second_code_delimiter_index -= 9 # subtract them from the index.

        """Create Request Body"""
        expected_answer = code[first_code_delimiter_index:second_code_delimiter_index]
        data = [code[:first_code_delimiter_index], code[second_code_delimiter_index:]]

        request_body = json.dumps({
            "_id": id,
            "language_id": LANGUAGE_ID,
            "expected_output": "Passed",
            "expected_answer": expected_answer,
            "data": data
        }, indent = 4)

        print(Style.BRIGHT + "\nRequest Body:\n" + Style.RESET_ALL, request_body, "\n")

        exercise_test_file.close()

        """Copy Request Body to Clipboard"""
        try:
            pyperclip.copy(request_body)
            print(Fore.LIGHTGREEN_EX + "Copied to clipboard!\n\n\n" + Style.RESET_ALL)

        except:
            print(Fore.LIGHTRED_EX + "NOT copied to clipboard!\n\n\n" + Style.RESET_ALL)
        # savedFile = open(file_prefix+'Result.txt','w')
        # savedFile.write(str(request_body))
        with open(file_prefix+'Result.txt','w') as savedFile:
            savedFile.write(str(request_body))


    except Exception as e:
        print(Fore.LIGHTRED_EX + "\nError: ", e, "\n\n\n" + Style.RESET_ALL)

    time.sleep(3)