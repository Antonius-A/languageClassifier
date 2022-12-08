def convert_file_to_lower_case(file1,file2):
    file_write = open(file2,"w")
    with open(file1) as fp:
        line = ''
        count = 0

        while True:
            count += 1

            # Get next line from file
            line = fp.readline()
            line = line.lower()
            print(line)
            # if line is empty
            # end of file is reached
            file_write.write(line)
            if not line:
                break
    fp.close()
    file_write.close()
    print(count)



convert_file_to_lower_case("francais.txt","francais.txt")