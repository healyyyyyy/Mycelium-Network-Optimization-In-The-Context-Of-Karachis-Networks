import csv
import more_itertools

def readfile(file,experiment):
    runs = open (file + ".txt","r+")
    temp = runs.readlines()
    for i in range(len(temp)):
        temp[i]= temp[i].split()
    
    if experiment:
        fd = [(temp[i][0], float(temp[i][1][1:len(temp[i][1])-1]), temp[i][3]) for i in range(len(temp))]
    else:
        fd = [(int(temp[i][0]), float(temp[i][1][1:len(temp[i][1])-1])) for i in range(len(temp))]
    return fd

def getbest(file,water,write):

    simulationfd = readfile(file,False)
    experimentfd = readfile("final_petri_dishes",True)

    waterfd = []
    nutrientfd = []
    for i in experimentfd:
        if i[2]== "water":
            waterfd.append(i)
        else:
            nutrientfd.append(i)

    absdiff = dict()
    for i in simulationfd:
        if water == True:
            absdiff[i]= sum([abs(i[1]- j[1]) for j in waterfd])
        else:
            absdiff[i] = sum([abs(i[1]- j[1]) for j in nutrientfd])

    key_min = min(absdiff.keys(), key=(lambda k: absdiff[k]))
    if write == "first10":
        first_n = more_itertools.take(10, absdiff.items())
        data = [[key[0],key[1],value] for key,value in first_n]
        header = ['name', 'Fractal Dimension', 'Sum of Absolute differences from experiment']
        with open(file + '.csv', 'w', encoding='UTF8', newline='') as f: 
            writer = csv.writer(f)
            
            # write the header
            writer.writerow(header)
            # write multiple rows
            writer.writerows(data)
    return(key_min, absdiff[key_min])


print(getbest("no_food_scaled",False,"None"))