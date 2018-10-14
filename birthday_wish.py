#!/usr/bin/env python3

import time

def counter(n):
    """
    Show Happy Birthday message after n sec 
    """
    while n>0:
        print(n)
        n -= 1
        time.sleep(1)
    else:
        print('Happy Birthday!')

if __name__ == "__main__":
    num = int(input("Enter counter num:"))
    counter(num)
