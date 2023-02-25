import ast
from colorama import Style
import json
import os
import subprocess

folder = input(Style.BRIGHT + "type the folder you want to enter: " + Style.RESET_ALL)
file_list = os.listdir(folder)

LANGUAGE_ID = 71
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
        if node.id == local_Name:
            node = ast.Name(id = new_local_Name, ctx = node.ctx)
        return node
    def visit_Name(self, node):
        if node.id == global_Name:
            node = ast.Name(id = new_global_Name, ctx = node.ctx)
        return node
class reWriteCode2(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Constant(self, node):
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
                # new_node.ops[0] = opreator_dict[new_operator]
        return new_node 
            # new_node = ast.Compare()
           
           
        # print(expression_list)
        # print(node._fields)
        return new_node
class reWriteCode4(ast.NodeVisitor):
    
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_FunctionDef(self, node):
        if (node.name == oldFucntionName):
            node.name = newFunctionName
        return node
    def visit_Call(self, node):
        if node.func.id == oldFucntionName:
            node.func.id = newFunctionName
        return node
class reWriteCode5(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Compare(self, node):
        if node.left.func and node.left.func.id == oldFucntionName:
            node.left.func.id = newFunctionName
        return node

class reWriteCode6(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Assign(self, node):
        if node.targets[0].id == global_Name:
            node.targets[0].id = new_global_Name
        return node
        
    def visit_AugAssign(self, node):
        if node.target.id == global_Name:
            node.target.id = new_global_Name
        return node

class reWriteCode7(ast.NodeVisitor):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node
    def visit_Global(self, node):
        if node.names[0] == global_Name:
            node.names[0] = new_global_Name
        return node
while(True):
    print(file_list)
    designated_file =input(Style.BRIGHT + "input the file name you want to change " + Style.RESET_ALL)   
    for file in file_list:
        if file == designated_file:
            file_path = folder + "/" + file
            #TODO get original data from server
            # we use templates_json file as example right now
            # print(Style.BRIGHT + 'current file is '+file_path + Style.RESET_ALL)
            with open(file_path, 'r+') as template_response_data:
                download_data = template_response_data.read()
                root = ast.parse(download_data)
                # print(download_data)
                print(ast.dump(root,indent=4))
                # print(ast_result)
            # question_dataList = ast_result.body[0].value.values[4].elts[0]
            # root = ast.parse(source)
            # print(ast.dump(root,indent=4))
                body_list = root.body
                print(body_list)
            # print(body_list)
        #filter FunctionDef
        # print(body_list)
            function_filter = filter(lambda item: type(item)== ast.FunctionDef, body_list)
            function_list = list(function_filter)
            try_filter = filter(lambda item: type(item)== ast.Try, body_list)
            try_list = list(try_filter)
            class_filter = filter(lambda item: type(item)== ast.ClassDef, body_list)
            class_list = list(class_filter)
            body_list_exclude_try_filter = filter(lambda item: type(item)!= ast.Try and type(item)!= ast.Import, body_list)
            body_list_exclude_try = list(body_list_exclude_try_filter)
            global_variable_filter = filter(lambda item: type(item)== ast.Assign, body_list)
            global_variable_only = list(global_variable_filter)
            function_with_global_var_filter = filter(lambda item: type(item.body[0]) == ast.Global, function_list)
            global_variable_function_only = list(function_with_global_var_filter)
            global_var_filter = filter(lambda item: type(item) == ast.Assign, body_list)
            global_variable_only = list(global_var_filter)
            print(global_variable_only)
        # print(global_variable_function_only)
        # print(body_list_exclude_try)
        # print(try_list[0])
        # print(class_list)
            code_block_indentation_level_dict = {}
            indentation_level = 0
            def get_indentation(node):
                for item in node:
                    if item._fields.__contains__('body'):
                        global indentation_level
                        # print(item.__class__)
                        unparseString = ast.unparse(item)
                        splitList = unparseString.split('\n')
                        for index in range(len(splitList)):
                            splitList[index] ='    '*indentation_level + splitList[index]
                        # print(splitList)
                        modifiedList = "\n".join(splitList).replace("\'","\"")
                        code_block_indentation_level_dict[modifiedList] = indentation_level
                        # print(code_block_indentation_level_dict)
                        indentation_level += 1
                        return get_indentation(item.body)
                    else:
                        if node.index(item) == len(node) - 1:
                            unparseItem = ast.unparse(item)
                            unparseItem = '    '*indentation_level + unparseItem.replace("\'","\"")
                            code_block_indentation_level_dict[unparseItem] = indentation_level
                            return code_block_indentation_level_dict
                        else:
                            unparseItem = ast.unparse(item)
                            unparseItem = '    '*indentation_level + unparseItem.replace("\'","\"")
                            code_block_indentation_level_dict[unparseItem] = indentation_level
                            continue
            # print(indentation_level)
            # print(try_list[0].body[0].value.func.id)
            # print(function_list)
            def store_modified_file():
                # file_parameter = file.split('.')
                path = '/Users/qianjingning/upload-exercises-scripts/ModifiedTemp/'
                folder_exist =  os.path.exists(path)
                if not folder_exist:
                    os.makedirs(path)
                id = input(Style.BRIGHT + 'create a name for modified file' + Style.RESET_ALL)
                generate_file_name = id + '.py'
                if folder == 'ModifiedTemp':
                    try:
                        with open(file_path, 'w') as new_savedFile:
                            new_savedFile.write(ast.unparse(root).replace("\'","\""))
                    except:
                        print('save failed') 
                else:
                    try:
                        with open(path + generate_file_name, 'w') as new_savedFile:
                            new_savedFile.write(ast.unparse(root).replace("\'","\""))
                    except:
                        print('save failed')
            
            def writeBackToFile(modified):
                for i in body_list:
                    if(i.end_col_offset == modified.end_col_offset):
                        i = modified

            visitor1 = reWriteCode1()
            visitor2 = reWriteCode2()
            visitor3 = reWriteCode3()
            visitor4 = reWriteCode4()
            visitor5 = reWriteCode5()
            visitor6 = reWriteCode6()
            visitor7 = reWriteCode7()
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
                print('4 for function delaration and call change')
                print('5 for getting indentation level')
                print('6 for quit current file')
                OPTION = input(Style.BRIGHT + Style.RESET_ALL)
                if OPTION == "1":
                        local_or_global = input(Style.BRIGHT + 'For local variable press 1, for global variable press 2' + Style.RESET_ALL)
                        if local_or_global == "1":
                            function_index_str = input(Style.BRIGHT + 'choose function that you want to modify(following the order from up to down, starting from 1)' + Style.RESET_ALL)
                            function_index_number = int(function_index_str)
                            local_Name = input(Style.BRIGHT + "Enter Variable Name want to be changed: " + Style.RESET_ALL)    
                            new_local_Name = input(Style.BRIGHT + "Enter new Variable Name: " + Style.RESET_ALL)
                            print(function_list[function_index_number-1].body)
                            #this function only can deal with the variable name in a specific funciton
                            
                            for item in function_list[function_index_number-1].body:
                                modified = visitor1.visit(item)
                                # print(modified)
                                #make sure replace the origin function in the root
                            writeBackToFile(modified)
                        
                        if local_or_global == "2":
                            global_Name = input(Style.BRIGHT + "Enter Global Variable Name want to be changed: " + Style.RESET_ALL) 
                            new_global_Name = input(Style.BRIGHT + "Enter New Global Variable Name: " + Style.RESET_ALL)
                            #for global variable assginment variable at the top level
                            modified_top_level = visitor6.visit(global_variable_only[0])
                            writeBackToFile(modified_top_level)
                            #for global variable in inner function 1. global statement 2. global variable assginment
                            for item in global_variable_function_only[0].body:
                                if type(item) == ast.Global:
                                    modified_global = visitor7.visit(item)
                                    writeBackToFile(modified_global)
                                if type(item) == ast.Assign or type(item) == ast.AugAssign:
                                    modified_assignment = visitor6.visit(item)
                                    writeBackToFile(modified_assignment)
                            #for try block for test global variable
                            for expr in try_list[0].body:
                                if expr.value.args[0].__class__ == ast.Compare and expr.value.args[0].left.__class__ == ast.Name:
                                    modified_in_try = visitor1.visit(expr)
                                    writeBackToFile(modified_in_try)
                        store_modified_file()
                        # try:
                        #     with open(file_path, 'w') as new_savedFile:
                        #         new_savedFile.write(ast.unparse(root))
                        #         print('file changed successfully!')
                        #     # fill data into spec format
                            
                        # except:
                        #     print('save failed')
                                        
                elif OPTION == "2":
                    constant_string = input(Style.BRIGHT + "Enter Constant String want to be changed: " + Style.RESET_ALL)
                    new_constant_string = input(Style.BRIGHT + "Enter new Constant String: " + Style.RESET_ALL)
                    for item in body_list:
                        modified = visitor2.visit(item)
                        writeBackToFile(modified)
                        
                    store_modified_file()

                elif OPTION =="3":
                    try: 
                        expression = input(Style.BRIGHT + "Enter expression whose operator that you want to change: " + Style.RESET_ALL)
                        new_operator = input(Style.BRIGHT + "Enter New Comparison Operator: " + Style.RESET_ALL)
                        for item in body_list:
                            modified = visitor3.visit(item)
                            writeBackToFile(modified) 
                        store_modified_file()        
                    except Exception as e:
                        print(e)

                elif OPTION == "4":
                    oldFucntionName = input(Style.BRIGHT + "Enter the function name that you want to change: " + Style.RESET_ALL)
                    newFunctionName = input(Style.BRIGHT + "Enter New function name: " + Style.RESET_ALL)
                    targeted_function = None
                    for item in function_list:
                        if (item.name == oldFucntionName):
                            modified = visitor4.visit(item)
                            targeted_function = item
                            
                            # print(ast.dump(modified,indent=4))
                            writeBackToFile(modified)
                    #function call inside function declaration block
                    for item in targeted_function.body:
                        modified_funcall_inner_block = visitor4.visit(item)
                        writeBackToFile(modified_funcall_inner_block)
                            
                    #function call in try block
                    for expr in try_list[0].body:
                        if expr.value.args[0].__class__ == ast.Compare and expr.value.args[0].left.__class__ == ast.Call:
                            try_calls_modified = visitor5.visit(expr)
                            # print(ast.dump(calls_modified,indent=4))
                            writeBackToFile(try_calls_modified)
                    store_modified_file()
                        
                elif OPTION == "5":
                    # function defination in the class body
                    ClassOrFuncName = input(Style.BRIGHT + "Enter the class name or function name that you want to get the indentation level of innerest body: " + Style.RESET_ALL)
                        # if Class.name == className:
                    ClassOrFuncFilter = filter(lambda item: (item.__class__ == ast.FunctionDef or item.__class__ == ast.ClassDef) 
                                            and item.name == ClassOrFuncName, body_list_exclude_try)
                    only_one_classorDeflist = list(ClassOrFuncFilter)
                    FinalDict = get_indentation(only_one_classorDeflist)
                    print(FinalDict)
                    Indentation_result = {'Indentation_result':[]}
                    for item in FinalDict:
                        print(download_data)
                        # remove_notation = ast.parse(download_data)
                        # remove_notation1 = ast.unparse(remove_notation)
                        # print(remove_notation1)
                        data = download_data.split(item)
                        print(data)
                        each_indentation_level = {
                        "_id": designated_file,
                        "expected_answer": item,
                        "indentation": FinalDict[item],
                        "data":[data[0],data[1]],
                        "language_id": LANGUAGE_ID
                        }
                        whole_code = data[0]+ item + data[1]
                        print(whole_code)
                        p2 = subprocess.run(['python3',f'{folder}/{file}'], capture_output=True, text=True)
                        if p2.returncode == 0:
                            #TODO the output is wrong sometimes
                            print(p2.stdout)
                            each_indentation_level["expected-output"] = p2.stdout
                        else:
                            print(p2.stderr)
                            each_indentation_level["error-msg"] = p2.stderr
                        
                        Indentation_result["Indentation_result"].append(each_indentation_level)
                        # else:
                        #     each_indentation_level = {
                        #     "expected_answer": item,
                        #     "indentation": FinalDict[item],
                        #     }
                        #     Indentation_result["Indentation_result"].append(each_indentation_level)
                    # print(Indentation_result)
                    path = '/Users/qianjingning/upload-exercises-scripts/IndentationRes/'
                    folder_exist =  os.path.exists(path)
                    if not folder_exist:
                        os.makedirs(path)
                    new_generated_file_name = file.split('.')[0]+'-indentaion-result'+'.json'
                    output_file = open(path + new_generated_file_name, 'w+')
                    json.dump(Indentation_result, output_file, indent=4)
                    output_file.close()
                # print(code_block_indentation_level_dict)
                elif OPTION == "6":
                    flag = False
                else: print('Wrong option input, please try again!')

    # print(ast.dump(new_root,indent=4))
    # print(x.body[0].value.right.value)