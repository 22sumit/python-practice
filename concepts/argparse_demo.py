import argparse

# Initialize parser
parser=argparse.ArgumentParser(description="Adding description")

# Adding optional argument
parser.add_argument("-o", "--Output", help="show output")

# Read arguments from command line
args=parser.parse_args()

if args.Output:
    print("Displaying output as: %s" %args.Output)