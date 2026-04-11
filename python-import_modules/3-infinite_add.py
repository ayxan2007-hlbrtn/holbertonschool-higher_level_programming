#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # 1-ci indeksdən sona qədər bütün arqumentləri toplayırıq
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{:d}".format(total))
