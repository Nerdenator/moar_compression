# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import getopt
import sys


def compressor(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = ''
    output_file = ''
    compression_cycles = 0
    try:
        opts, args = getopt.getopt("hi:o:c:",["ifile=","ofile","compressioncycles"])
    except getopt.GetoptError as ex:
        print(str(ex))
        print('moar_compression.py -i <inputfile> -o <outputfile> -c <compressioncycles>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('moar_compression.py -i <inputfile> -o <outputfile> -c <compressioncycles>')
        elif opt in("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-c", "--cycles"):
            compression_cycles = arg
    compressor(input_file, output_file, compression_cycles)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
