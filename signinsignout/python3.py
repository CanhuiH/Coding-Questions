#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # Write your code here
    result = []
    in_dict = dict()
    out_dict = dict()
    for line in logs:
        log = line.split()
        if log[2] == 'sign-in':
            if log[0] not in in_dict:
                in_dict[log[0]] = [log[1]]
            else:
                in_dict[log[0]].append(log[1])
        elif log[2] == 'sign-out':
            if log[0] not in out_dict:
                out_dict[log[0]] = [log[1]]
            else:
                out_dict[log[0]].append(log[1])
        
    for key in out_dict:
        if key not in in_dict:
            continue
        in_arr = in_dict[key]
        out_arr = out_dict[key]
        for i in range(len(out_arr)):
            if int(out_arr[i]) - int(in_arr[i]) <= maxSpan:
                result.append(key)
                break

    sorted_result = sorted(result, key=int) 
    return sorted_result
    
    #
    # WARNING: Please do not use GitHub Copilot, ChatGPT, or other AI assistants
    #          when solving this problem!
    #
    # We use these tools in our coding too, but in our interviews, we also don't
    # allow using these, and want to see how we do without them.
    #

if __name__ == '__main__':
    fptr = sys.stdout

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()