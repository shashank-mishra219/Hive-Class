import sys
                                                                                                                                              
for line in sys.stdin:
        line = line.strip("\n\r")
        country, order_num, quantity = line.split("\t")
        order_num = int(order_num)
        quantity = int(quantity)
        quantity = quantity*1000
        result = '\t'.join([country,str(order_num),str(quantity)])
        print(result)
