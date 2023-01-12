import ast
from _ast import FunctionDef
from typing import Any
from colorama import Style
import json
import os

folder = 'templatesResultFromSever'
file_list = os.listdir(folder)
#   if(a<b):
#       print('A')
#   else: print('B')

class reWriteCode1(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    # def visit_FunctionDef(self, node):
    #       return ast.FunctionDef()
    def visit_Name(self, node):
        new_node = node
        if node.id == variable_Name:
            new_node = ast.Name(id = new_Variable_Name, ctx = node.ctx)
        return new_node
class reWriteCode2(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Str(self, node):
        new_node = node
        if node.value == constant_string:
            new_node = ast.Constant(value = new_constant_string, kind = node.kind)
        return new_node

opreator_dict = {">":ast.Gt(), "<":ast.Lt(), "==":ast.Eq(), "!=": ast.NotEq(), ">=":ast.GtE() ,"<=":ast.LtE()}
class reWriteCode3(ast.NodeVisitor):
    
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Compare(self, node):
        new_node = node
        expression_list = []
        expression_list = expression.split(' ')
        # print(expression_list)
        # print(node.ops[0].__class__)
        # print(opreator_dict[expression_list[1]].__class__)
        if node.left.id == expression_list[0] and node.ops[0].__class__ == opreator_dict[expression_list[1]].__class__ and node.comparators[0].id == expression_list[2]:
            # new_node.ops.remove(new_node.ops[0])
            with open('config.json','r+') as config_file:
                data = config_file.read()
                json_to_dict = json.loads(data)
                print(json_to_dict)
                print(node)
                new_node.ops[0] = opreator_dict[json_to_dict['comparison_operators'][len(json_to_dict['comparison_operators'])-1]['current_var']] 
                # new_node.ops[0] = opreator_dict[new_operator]
            
            # new_node = ast.Compare()
           
           
        # print(expression_list)
        # print(node._fields)
        return new_node

for file in file_list:
    file_path = folder + "/" + file
    #TODO get original data from server
    # we use templates_json file as example right now
    with open(file_path, 'r+') as template_response_data:
        download_data = template_response_data.read()
        json_to_dict = json.loads(download_data)
        #    root = ast.parse(json_to_dict['data'][0])
        #    print(json_to_dict['data'][0])
        # print(json_to_dict['data'][0])
        # print(json_to_dict['expected_answer'])
        # print(json_to_dict['data'][1])
        original_python_file = json_to_dict['data'][0] + json_to_dict['expected_answer']+ json_to_dict['data'][1]
        
        # destructed_code_list = original_python_file.split('\n    # Student Code')
        # print(destructed_code_list)
        

        # print(input_code[0])
        # print(original_python_file)
        # format_data = json_to_dict['expected_answer'].lstrip().replace('    ','  ')
    # for code_item in destructed_code_list:
        root = ast.parse(original_python_file)
        print(ast.dump(root,indent=4))
        # print(ast_result)
    # question_dataList = ast_result.body[0].value.values[4].elts[0]
    # root = ast.parse(source)
    # print(ast.dump(root,indent=4))
        body_list = root.body
        # print(body_list)
        # print(body_list)
    #filter FunctionDef
    try_filter = filter(lambda item: type(item)== ast.Try, body_list)
    try_list = list(try_filter)
# print(try_list[0].body)
    visitor1 = reWriteCode1()
    visitor2 = reWriteCode2()
    visitor3 = reWriteCode3()



    SPEC_FILE_FORMAT = {
        'name_variables':[],
        'string_constant':[],
        'comparison_operators':[]
    }

    flag = True
    while(flag == True):
        print('type in the number for the operation')
        print('1 for Variable Name change')
        print('2 for String Constant change')
        print('3 for Comparison Operator change')
        print('4 for save and quit')
        OPTION = input(Style.BRIGHT + Style.RESET_ALL)
        if OPTION == "1":
                # function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
                # function_index_number = int(function_index_str)
                variable_Name = input(Style.BRIGHT + "Enter Variable Name want to be changed: " + Style.RESET_ALL)
                new_Variable_Name = input(Style.BRIGHT + "Enter new Variable Name: " + Style.RESET_ALL)
                changing_operations = {
                        'origin_var':variable_Name,
                        'current_var': new_Variable_Name
                }
                SPEC_FILE_FORMAT['name_variables'].append(changing_operations)
                modified = visitor1.visit(try_list[0])
                # print(modified)
                #make sure replace the origin function in the root
                for item in body_list:
                    if(item.end_col_offset == modified.end_col_offset):
                        item = modified
                    
                # try:
                #     with open(file_path, 'w') as new_savedFile:
                #         new_savedFile.write(ast.unparse(root))
                #         print('file changed successfully!')
                #     # fill data into spec format
                    
                # except:
                #     print('save failed')
                                
        elif OPTION == "2":
                try: 
                    constant_string = input(Style.BRIGHT + "Enter Constant String want to be changed: " + Style.RESET_ALL)
                    new_constant_string = input(Style.BRIGHT + "Enter new Constant String: " + Style.RESET_ALL)
                    modified = visitor2.visit(try_list[0])
                    for item in body_list:
                        if(item.end_col_offset == modified.end_col_offset):
                            item = modified
                        
                    try:
                        with open(file_path, 'w') as new_savedFile:
                            new_savedFile.write(ast.unparse(root))
                        changing_operations = {
                            "origin_var":constant_string,
                            "current_var": new_constant_string
                        }
                        SPEC_FILE_FORMAT['string_constant'].append(changing_operations)
                        output_file = open("config.json", 'a')
                        json.dump(SPEC_FILE_FORMAT, output_file, indent=4)
                    except:
                        print('save failed')
                except Exception as e:
                    print(e)
        elif OPTION =="3":
                try: 
                    expression = input(Style.BRIGHT + "Enter expression whose operator that you want to change: " + Style.RESET_ALL)
                    new_operator = input(Style.BRIGHT + "Enter New Comparison Operator: " + Style.RESET_ALL)
                    changing_operations = { 
                            'origin_var': expression.split(' ')[1],
                            'current_var': new_operator
                            }
                    SPEC_FILE_FORMAT['comparison_operators'].append(changing_operations)
                    output_file = open("config.json", 'r+')
                    json.dump(SPEC_FILE_FORMAT, output_file, indent=4)
                    output_file.close()
                    modified = visitor3.visit(try_list[0])
                    
                    
                    for item in body_list:
                        if(item.end_col_offset == modified.end_col_offset):
                            item = modified           
                    try:
                        with open('new_root_file.txt', 'w') as new_savedFile:
                            new_root = ast.unparse(root)
                            
                            #TODO need to add #Student Code annotation into the parsed file
                            # so that it can be splited to create new json data.
                            # import CreateRequestBodyForCodeInputExercises as CreateResponseData
                            # CreateResponseData.CreateResponseBody(new_root)
                            new_savedFile.write(new_root)
                    except:
                        print('save failed')
                except Exception as e:
                    print(e)

        elif OPTION == "4":
            #TODO GET original data from server // post(url...)
               
               
               
            #TODO Read config file and modified the original data
            #TODO reupload modified data to server
            flag = False
            #write json data into specfic parameters' value
            
        else: print('Wrong option input, please try again!')

# print(ast.dump(new_root,indent=4))
# print(x.body[0].value.right.value)