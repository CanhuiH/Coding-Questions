#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'groupTransactions' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY transactions as parameter.
#

def groupTransactions(transactions):
    # Write your code here
    transactions_dict = dict()
    counter_dict = Counter(transactions)
    for key in counter_dict:
        amount = str(counter_dict[key])
        item = key + " " + amount
        if amount in transactions_dict:
            transactions_dict[amount].append(item)
        else:
            transactions_dict[amount] = [item]
    
    myKeys = list(transactions_dict.keys())
    myKeys.sort(key=int)
    sorted_dict = {i: transactions_dict[i] for i in myKeys}
    
    result = []
    for key in transactions_dict:
        item = transactions_dict[key].sort(key=str.lower)
        result += transactions_dict[key]
        
    return result
    

    #
    # WARNING: Please do not use GitHub Copilot, ChatGPT, or other AI assistants
    #          when solving this problem!
    #
    # We use these tools in our coding too, but in our interviews, we also don't
    # allow using these, and want to see how we do without them.
    #

if __name__ == '__main__':
    fptr = sys.stdout

    transactions_count = int(input().strip())

    transactions = []

    for _ in range(transactions_count):
        transactions_item = input()
        transactions.append(transactions_item)

    result = groupTransactions(transactions)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
