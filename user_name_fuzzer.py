###############################################################################
# user_name_fuzzer.py
#
# USAGE: 
#   python user_name_fuzzer.py name_file.txt > uesrnames.txt
#
# Creates a fuzzed listed of potential usernames based on a provided list of 
# names. Used in attempts to account spray.
###############################################################################
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} name_file.txt")
        sys.exit(0)


    name_list_file = sys.argv[1]

    with open(name_list_file) as name_list:
        for name in name_list:
            tokens = name.lower().split()

            fname = tokens[0]
            lname = tokens[-1]

            print(fname + lname)            # johndoe
            print(lname + fname)            # doejohn
            print(fname + "." + lname)      # john.doe
            print(lname + "." + fname)      # doe.john
            print(lname + fname[0])         # doej
            print(fname[0] + lname)         # jdoe
            print(lname[0] + fname)         # djoe
            print(fname[0] + "." + lname)   # j.doe
            print(lname[0] + "." + fname)   # d.john
            print(fname)                    # john
            print(lname)                    # joe