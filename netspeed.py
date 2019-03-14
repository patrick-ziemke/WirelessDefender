import csv

filepath = raw_input("Enter file path to file (netspeed_data.csv): ")

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

    print("Total number of materials: %s" % (csvreader.line_num))

print("Field names are: " + ', '.join(field for field in fields))
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

    controlAverage = ((float(control[2]) + float(control[5]) + float(control[8])) / 3)

    # set corresponding variables to integers for each row
    for row in materials[:(csvreader.line_num)]:
        materialName = row[0]

        trial1avg = row[2]
        trial2avg = row[5]
        trial3avg = row[8]

        # find the mean of all trial averages
        avgAverage = ((float(trial1avg) + float(trial2avg) + float(trial3avg)) / 3)

        # calculate percent decrease
        decrease = (controlAverage - avgAverage)
        percentDecrease = (decrease / controlAverage) * -100

        # Percent decrease = Percent slower (ms)
        # Larger decrease = Slower connection
        print("\n " + materialName + "      Percent Decrease: " + str(round(percentDecrease, 2)) + "%\n")
        print("------------------------------------------------------------")

elif(selection == 'n'):
    print(starBullet + "Quitting...")
