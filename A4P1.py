'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris

Query 1: ____________________________________________________________
Query 2: ____________________________________________________________
'''

import sqlite3
from averager import avgEachDb
    
if __name__ == "__main__":
    #example
    Query1 = "select COUNT(*) from Parts"
    print(avgEachDb(Query1, 100,100,100,100,100))