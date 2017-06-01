#!/usr/bin/python

import sys, getopt, json, csv

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if len(inputfile) > 0:
        with open(inputfile) as inputdata:
            items = json.load(inputdata)
        if len(outputfile) > 0:
            f = csv.writer(open(outputfile, 'wb+'))
            f.writerow(['No', 'Product Name', 'Price (SGD)'])
            for idx, item in enumerate(items):
                f.writerow([idx, unicode(item['product_name']).encode("utf-8").strip(), item['price']])
           
if __name__ == "__main__":
   main(sys.argv[1:])