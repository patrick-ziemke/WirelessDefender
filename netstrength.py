import csv

filepath = raw_input("Enter file path to file (netstrength_data.csv): ")

starBullet = "\033[1;36;40m [\033[1;37;40m*\033[1;36;40m] \033[1;37;40m"

# initialize titles and materials
fields = []
materials = []

# reading csv file
with open(filepath, 'r') as csvfile:   
    # create csv reader object
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()

    # extract each data row one by one
    for row in csvreader:
        materials.append(row)

print("Field names are:" + ', '.join(field for field in fields))
print('\n')
print(starBullet + '     Data Output     ' + starBullet + '\n')
for row in materials[:(csvreader.line_num)]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n\n')

selection = raw_input(starBullet + "Do you wish to continue with analysis? (y/n): ")
if(selection == 'y'):

# initializing rows as variable materials
    control = materials[0]
    copper = materials[1]
    aluminum = materials[2]
    steel = materials[3]
    copperRF = materials [4]
    aluminumRF = materials[5]
    steelRF = materials[6]

    # set corresponding variables to strings for each row
    print(starBullet + "        Data Output:        " + starBullet + '\n\n')
    for row in materials[:(csvreader.line_num)]:
        materialName = row[0]

        controlAverage = control[2]
        averageStrength = row[2]
        maxStrength = row[3]

        decrease = (int(controlAverage) - int(averageStrength))
        peak = (int(controlAverage) - int(maxStrength))

        print("-----------------------------------------------------------------------------------------------\n")
        print(row[0] + (": Signal dropped by %s dBm" % decrease) + (" and peaked at %s dBm lower." % peak) + '\n')


elif(selection == 'n'):
    print(starBullet + "Quitting...")
