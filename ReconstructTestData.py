import ast
from _ast import FunctionDef
from typing import Any
from colorama import Style
import json

file_path = 'templates/TEST7040.py'
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
            new_node.ops[0] = opreator_dict[new_operator]
            
            # new_node = ast.Compare()
           
           
        # print(expression_list)
        # print(node._fields)
        return new_node

with open(file_path, 'r') as inputFile:
    source = inputFile.read()

    # print(ast_result)
# question_dataList = ast_result.body[0].value.values[4].elts[0]
root = ast.parse(source)
# print(ast.dump(root,indent=4))
body_list = root.body
#filter FunctionDef
function_filter = filter(lambda item: type(item)== ast.FunctionDef, body_list)
function_list = list(function_filter)

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
            function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
            function_index_number = int(function_index_str)
            variable_Name = input(Style.BRIGHT + "Enter Variable Name want to be changed: " + Style.RESET_ALL)
            new_Variable_Name = input(Style.BRIGHT + "Enter new Variable Name: " + Style.RESET_ALL)
            modified = visitor1.visit(function_list[function_index_number-1])
            #make sure replace the origin function in the root
            for item in body_list:
                if(item.end_col_offset == modified.end_col_offset):
                    item = modified
                
            try:
                with open(file_path, 'w') as new_savedFile:
                    new_savedFile.write(ast.unparse(root))
                    print('file changed successfully!')
                # fill data into spec format
                changing_operations = {
                    'origin_var':variable_Name,
                    'current_var': new_Variable_Name
            }
                SPEC_FILE_FORMAT['name_variables'].append(changing_operations)
                
                print(SPEC_FILE_FORMAT)
            except:
                print('save failed')
                            
    elif OPTION == "2":
            try: 
                function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
                function_index_number = int(function_index_str)
                constant_string = input(Style.BRIGHT + "Enter Constant String want to be changed: " + Style.RESET_ALL)
                new_constant_string = input(Style.BRIGHT + "Enter new Constant String: " + Style.RESET_ALL)
                modified = visitor2.visit(function_list[function_index_number-1])
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
                except:
                    print('save failed')
            except Exception as e:
                print(e)
    elif OPTION =="3":
            try: 
                function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
                function_index_number = int(function_index_str)
                expression = input(Style.BRIGHT + "Enter expression whose operator that you want to change: " + Style.RESET_ALL)
                new_operator = input(Style.BRIGHT + "Enter New Comparison Operator: " + Style.RESET_ALL)
                modified = visitor3.visit(function_list[function_index_number-1])
                for item in body_list:
                    if(item.end_col_offset == modified.end_col_offset):
                        item = modified
                    
                try:
                    with open(file_path, 'w') as new_savedFile:
                        new_savedFile.write(ast.unparse(root))
                    changing_operations = { 
                        'origin_var': expression.split(' ')[1],
                        'current_var': new_operator
                        }
                    SPEC_FILE_FORMAT['comparison_operators'].append(changing_operations)
                except:
                    print('save failed')
            except Exception as e:
                print(e)

    elif OPTION == "4": 
        output_file = open("config.json", 'a')
        json.dump(SPEC_FILE_FORMAT, output_file, indent=4)
        flag = False
        #write json data into specfic parameters' value
        
    else: print('Wrong option input, please try again!')

# print(ast.dump(new_root,indent=4))
# print(x.body[0].value.right.value)