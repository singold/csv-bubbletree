# csvbt.py
# This file is the main script that processes the csv file and outputs a .js
# file with the json object as a variable called 'data'


#en esta funcion falta ver donde se guarda todo (json_dict) y como
def get_childs(csv_object, json_dict):
#gets childs recursevly 

    current_line = csv.read()

    initial_label = current_line[0]
    initial_value = current_line[1]

    previous_line = current_line

    csv_sub_object = None

    #json_dict.add(label & value)

    while previous_line = current_line:
        csv_sub_object.add(current_line)

    #json_dict.add(childs = get_childs(csv_sub_object)

