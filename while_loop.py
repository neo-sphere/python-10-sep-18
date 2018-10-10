#!/usr/bin/env python3

import time

count = 10

while True:
    print(count)
    if count <= 0:
        print("Happy Birtday")
        break
    time.sleep(1)
    count -= 1
