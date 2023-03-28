import sys
                                                                                                                                              
for line in sys.stdin:
        line = line.strip("\n\r")
        quantity = int(line)
        quantity = quantity * 10
        print(str(quantity))
