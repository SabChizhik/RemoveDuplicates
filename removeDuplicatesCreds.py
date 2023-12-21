import csv

# clears file
def clearFile():
    clear = open("noDuplicates.csv", "w")
    clear.close()

def main():
    count = 0
    # call clear file function to empty file content
    clearFile()
    # opens input file for reading
    with open('Amtrakcreds.csv', errors='ignore') as infile:
    # creates csv reader
        csv_reader = csv.reader(infile, delimiter=',')
    # for each row in file
        for row in csv_reader:
    # pop function removes the last index value of the row
    # done for formatting purposes
            row.pop(-1)
            row.pop(-1)
            row.pop(-1)
            row.pop(-1)
            row.pop(-1)
            row.pop(-1)
    # variable for username
            username = row[1]
    # opens noDuplicates file for appending & reading
            with open("noDuplicates.csv", "a+", newline='') as outfile:
    # if username is in the noDuplicates file
                if username in open("noDuplicates.csv").read():
    # print username was found
                    print("%s found in outfile" % username)
                    count += 1
                else:
    # add row into noDuplicates file
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(row)
    print("End of file reached")
    print("%d duplicates removed" % count)
    return 0

main()