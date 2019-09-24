from struct import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", action="store", type="string", dest="filename", help="input file to parse", default="")
parser.add_option("-o", "--outdir", action="store", type="string", dest="outdir", help="Output directory", default="./extract")
parser.add_option("-l", "--list", action="store_true", dest="list", help="List of partitions")
parser.add_option("-e", "--compress", action="store_true", dest="zip", help="Extract all partitions(without \"-n NAME\")", default = False)
parser.add_option("-n", "--name", action="store", type="string", dest="name", help="Extract partition by name", default = "")
parser.add_option("-d", "--debug", action="store_true", dest="debug", help="Turn on Debug Mode")
parser.add_option("-p", "--partition", action="store", type="string", dest="partition", help="input partition data about PDL file", default="")
(options, args) = parser.parse_args()

if options.filename and options.partition == "":
    if str(args) == "[]":
        print("Use -h to get help")
    else:
        options.filename = args[0]

if options.filename !="":
    f = open("c:/pdl/output.pdl", w)