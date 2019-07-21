#Must be run under sudo mode
#cd into ball_tracking file before executing
import keyboard
import json

#Create three different file for different collision possibilities
#first file
address_one = "./collision_set/collision_ensured.txt"
address_two = "./collision_set/miss_ensured.txt"
address_three = "./collision_set/unsure.txt"

#Define the function to collect all the data
file_one = open(address_one,"w+")
file_two = open(address_two,"w+")
file_three = open(address_three,"w+")

def written_process(dict, file_type):
    #Write the data to the file
    file_type.write(json.dumps(dict))
    file_type.write('\n')
    #One space key pressed means one data set
    if keyboard.is_pressed(' '):
        print('Event ending')
        #Formatter
        file_type.write('-----------------------------------------------\n\n')
            
    #file_one.close()
file_choice = None
def collection(dX,dY,x,y,moving_time):
    global file_choice
    dict = {}
    #Construct a library
    dict['dX']=dX
    dict['dY']=dY
    dict['x']=x
    dict['y']=y
    dict['moving_time']=moving_time
    
    #Convert the dictionary to string
    dict={'dict':dict}
    #Key input to decide which file it's gonna written to
    if keyboard.is_pressed(2):
        print('written to file 1')
        file_choice = file_one
    elif keyboard.is_pressed(3):
        print('written to file 2')
        file_choice = file_two
    elif keyboard.is_pressed(4):
        print('written to file 3')
        file_choice = file_three
    #Written specific data to specific files
    if file_choice is not None:
        written_process(dict, file_choice)