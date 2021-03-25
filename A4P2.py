'''
Winter 2021 Cmput 291
Assignment 4, Part 2
Ahmad, Chris
'''
from averager import *

def makeIndex(aBool):
    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    for db in dbList:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        if aBool:
            c.execute("CREATE INDEX idxMadeIn ON Parts (madeIn)")
            print(f"{db}: Index has been created.")
        else:
            c.execute("DROP INDEX IF EXISTS idxMadeIn")
            print(f"{db}: Index has been dropped, if it existed.")
        conn.close()

Q3 = ["SELECT AVG(partPrice) FROM Parts GROUP BY madeIn;", 3]

if __name__ == "__main__":
    makeIndex(False)
    avgEachDbSimple(Q3[0],100,100,100,100,100,Q3[1])
    makeIndex(True)
    avgEachDbSimple(Q3[0],100,100,100,100,100,Q3[1])
    makeIndex(False)
