import sys
import argparse

from bynd import t_server, my_server

"""
1, The  if __name__ == "__main__":  is used to check
   whether this is executed as the top-level file, or if it has been imported
   by someone else (in this case, executing the main() function is not always intended).
2, The main() function must not take any arguments, because that’s how entry_points executes things.
"""

def main(args=None):

    parser = argparse.ArgumentParser()
    #parser.add_argument('-f', '--flag', action='store_true', default=False)  # can 'store_false' for no-xxx flags
    parser.add_argument('-a', '--add', required=True, help='python -m bynd -a [your data message]')
    #parser.add_argument('-o', '--opt', default='fallback')
    #parser.add_argument('arg', nargs='*') # use '+' for 1 or more args (instead of 0 or more)
    parsed = parser.parse_args()
    # NOTE: args with '-' have it replaced with '_'
    print('Result:',  vars(parsed))
    #print('parsed.reqd:', parsed.reqd)

    t_server
    #my_server

    #sys.exit(app.exec_())
    sys.exit()

# executes when your script is called from the command-line
if __name__ == "__main__":
    main(sys.argv)
