def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
            
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
