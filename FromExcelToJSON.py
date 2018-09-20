import re
import os

directory = '.'
files = os.listdir(directory)

rule_list = []


def print_files_on_dir(text):
    n = 0   
    print ('')
    print ('')
    print ('===List of files===')
    print ('')
    print ('')
    while n < len(files):
        name_of_file = files[n]
        result_string = "[" + str(n) + "]" + " - " + name_of_file
        print (result_string)
        n += 1
    print ('')
    print ('')
    print ('===================')
    print ('')
    final_message = "Select " + text + " with tests. Enter the number:"
    print (final_message)

def copy_rules_from_file(file_path):
    f = open(file_path, 'r', encoding='cp1251')
    
    for line in f:
        pattern_for_rules = re.findall(r'^.*',line)

        n = 0
        equal_file = False
        while n < len(rule_list):
            if rule_list[n] == pattern_for_rules:
                equal_file = True
            n += 1
        if equal_file == False:
            rule_list.append(pattern_for_rules)
        else:
            equal_file = False

    f.close()
    n = 0
        
        
def copy_rules_to_json(file_path):
    f = open(file_path, 'a', encoding='utf-8')
    
    n = 0
    while n < len(rule_list):
        #да, я мудак
        formated_string = str(rule_list[n]).replace("['", "")
        formated_string1 = formated_string.replace("']", "")
        rule = "main_user_question;" + formated_string1 + ";call_transfer_to_av\n"
        f.write(rule)
        n += 1
    f.close()
    

print_files_on_dir("EXCEL") #files in dir
file_number = int(input())
copy_rules_from_file(str(files[file_number]))

print_files_on_dir("JSON") #files in dir
file_number = int(input())
copy_rules_to_json(str(files[file_number]))
