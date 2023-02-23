# Test templates reconstruction with AST
## Introduction
##### This is an API for using to change test templates format automatically by giving corresponding inputs. It also can proceed with multiple files one by one in one single folder and the user can choose the specific file that needs to be changed. 

## Instructions
### 1. Get Started
##### Follow the command line with `python3 ReconstructTestData.py` to run the code.
### 2. Choose applied folder
##### Once the user runs the code, they can choose the targeted folder with test templates in it. The rule is that we do not change the original test templates. Instead, we create a copy of the target file and save the changes on it. The structure looks like the below:
| Folder | Description |
| ------ | ----------- |
| templates   | The folder contains all the test templates |
| ModifiedTemp | The folder contains all the modified test templates that are proceeded by AST |
| IndentationRes   | The result of getting the indentation level for a specific code block or function|
### 3. Appoint a specific test template
##### After the user enters the folder, the code will automatically check all the files and their name in it and type them on the terminal tab. The user can directly copy the file name that they want to make changes to.
### 4. Operation Menu
##### When we make a change to a test template for the first time, it will generate a new file in the `ModifiedTemp` folder. And the following operation for the same file will also directly overwrite the last version file to update the latest one.
#### 4.1 Variable name change
##### There are two options for variable names. They are global and local variables respectively. For the local variables, just type the function number and the local variable name to change a new one. For the global variables, just directly type the name.
#### 4.2 String constant change
##### Enter a Constant String that needs to be changed.
#### 4.3 Comparison operator change
##### The user needs to type the expression at first, such as a == b, or a > b etc.
#### 4.4 Function declaration and call change
##### Choose a function name as an input.
#### 4.5 Get indentation level
##### Student code is always stored in the function code block, our goal is to get the student code indentation so that we can match and control the code format on the front-end. We also use the function name as input. The result will be shown in the `indentationRes` folder.
#### 4.6 Quit
##### Quit to the current file, and the user can choose the next file that they want to change.