import matplotlib.pyplot as plt
import json

def data_loading(address):
    #Define an empty list
    data_total = list()
    #Load data in file
    file = open(address)
    #Write to a dictionary
    for line in file.readlines():
        print(line)
        #Append each dictionary to a list
        if '------' in line:
            #Jump to the next line
            data_total.append('break')
            continue
            print(line)
        data_total.append(json.loads(line))
        
            
    return data_total

def plot_action(data_number):
    x_number = []
    y_number = []
    if data_number is not None:
        for i in data_number:
            if i is 'break':
                plt.plot(x_number,y_number)
                #Erase the list
                x_number = []
                y_number = []
                #Print multiple graphs
                continue
            
            x_number.append(i['x'])
            y_number.append(i['y'])
        plt.show()

def plot():
    #First read file
    address_one = "./collision_set/collision_ensured.txt"
    address_two = "./collision_set/miss_ensured.txt"
    address_three = "./collision_set/unsure.txt"
    
    #Pass the list containing each dictionary
    data_one = data_loading(address_one)
    data_two = data_loading(address_two)
    data_three = data_loading(address_three)
    
    plot_action(data_one)
    plot_action(data_two)
    plot_action(data_three)
    
    #print(data_one)
    #print(data_two)
    #print(data_three)
        
    #print(collision_ensured)

#plotting()