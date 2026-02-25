import sys
import hello_goodbye

if len(sys.argv) ==2:
    hello_goodbye.goodbye(sys.argv[1])