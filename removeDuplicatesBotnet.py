import csv

# clears file
def clearFile():
    clear = open("noDuplicates.csv", "w")
    clear.close()

def main():
    # call clear file function to empty file content
    clearFile()
    # opens input file for reading
    with open('Amtrakbotnet.csv', errors='ignore') as infile:
    # creates csv reader
        csv_reader = csv.reader(infile, delimiter=',')
    # for each row in file
        for row in csv_reader:
    # variable for username
            username = row[1]
    # opens noDuplicates file for appending & reading
            with open("noDuplicates.csv", "a+", newline='') as outfile:
    # if username is in the noDuplicates file
                if username in open("noDuplicates.csv").read():
    # print username was found
                    print("%s found in outfile" % username)
                else:
    # add row into noDuplicates file
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(row)
    return 0

main()