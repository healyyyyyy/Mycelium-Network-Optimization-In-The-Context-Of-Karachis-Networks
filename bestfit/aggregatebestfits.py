import csv
import more_itertools


def aggregate(file):

    bestfitruns = open(file + ".txt","r+")
    bestfittemp = bestfitruns.readlines()

    for i in range(len(bestfittemp)):
        bestfittemp[i] = bestfittemp[i].split()

    header = ['Name', "Folder",
                    'Fractal Dimension',
                    'Absolute Difference from experiments',
                    'Initial Energy', 
                    'Number of Spores', 
                    'Absorbtion Value', 
                    'ticks per branch', 
                    'At Border Conditions', 
                    'Viewing Angle', 
                    'Vision Distance', 
                    'Wiggle Angle', 
                    'Energy Per Step', 
                    'Energy Per Split', 
                    'Radius Petri', 
                    'Radius Length',
                    'Probability Random Walk',
                    'Water Agar Energy',
                    'Percentage food patch',
                    'Water Agar',
                    'Distribute',
                    'Food input']


    with open(file+'.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(bestfittemp)


aggregate("combinednutrientagar")