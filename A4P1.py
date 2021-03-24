'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris
'''
from averager import *

def makeIndex(aBool):
    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    for db in dbList:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        if aBool:
            c.execute("CREATE INDEX idxNeedsPart ON Parts (needsPart)")
            print(f"{db}: Index has been created.")
        else:
            c.execute("DROP INDEX IF EXISTS idxNeedsPart")
            print(f"{db}: Index has been dropped, if it existed.")
        conn.close()

Q1 = ["SELECT partPrice FROM Parts WHERE partNumber = :code;", "partNumber", 1]
Q2 = ["SELECT partPrice FROM Parts WHERE needsPart = :code;", "needsPart", 2]

if __name__ == "__main__":
    makeIndex(False)
    avgEachDb(Q1[0],100,100,100,100,100,Q1[1], Q1[2])
    avgEachDb(Q2[0],100,100,100,100,100,Q2[1], Q2[2])
    makeIndex(True)
    avgEachDb(Q1[0],100,100,100,100,100,Q1[1], Q1[2])
    avgEachDb(Q2[0],100,100,100,100,100,Q2[1], Q2[2])

