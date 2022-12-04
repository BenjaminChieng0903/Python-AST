import ast
from _ast import FunctionDef
from typing import Any

from colorama import Style

file_path = 'templates/TEST7040.py'

class reWriteCode(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    # def visit_FunctionDef(self, node):
    #       return ast.FunctionDef()

    def visit_Name(self, node):
        new_node = node
        if node.id == variable_Name:
            new_node = ast.Name(id = new_Variable_Name, ctx = node.ctx)
            print('variable name matched!')
        else: print('cannot match')
        return new_node

    def visit_Num(self, node):
        if node.n == 1:
            node.n = 1000
        return node


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

visitor = reWriteCode()


flag = True
while(flag == True):
    print('type in the number for the operation')
    print('1 for Variable Name change')
    print('2 for Number change')
    print('3 for quit')
    OPTION = input(Style.BRIGHT + Style.RESET_ALL)
    if OPTION == "1":
        function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
        function_index_number = int(function_index_str)
        variable_Name = input(Style.BRIGHT + "Enter Variable Name want to be changed: " + Style.RESET_ALL)
        new_Variable_Name = input(Style.BRIGHT + "Enter new Variable Name: " + Style.RESET_ALL)
        modified = visitor.visit(function_list[function_index_number-1])
        
        #make sure replace the origin function in the root
        for item in body_list:
            if(item.end_col_offset == modified.end_col_offset):
                item = modified
            
        try:
            with open(file_path, 'w') as new_savedFile:
                new_savedFile.write(ast.unparse(root))
                print('file changed successfully!')
        except:
            print('save failed')
    elif OPTION == "2": print()
    elif OPTION == "3": flag = False

# print(ast.dump(new_root,indent=4))


    # print(x.body[0].value.right.value)

