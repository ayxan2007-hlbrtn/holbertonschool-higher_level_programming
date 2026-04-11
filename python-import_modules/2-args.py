#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Proqramın adını çıxırıq, yalnız arqumentləri saxlayırıq
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    for i in range(count):
        print("{:d}: {:s}".format(i + 1, argv[i]))
