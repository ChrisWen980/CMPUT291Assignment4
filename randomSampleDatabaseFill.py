import pandas
import sqlite3
import random
import copy

def main():
    dfCountry = pandas.read_csv(R"C:\Users\ahmad\OneDrive\Desktop\291\CMPUT291Assignment4\data_csv.csv")
    dfUPC = pandas.read_csv(R"C:\Users\ahmad\OneDrive\Desktop\291\CMPUT291Assignment4\upc_corpus.csv", low_memory = False)

    conn = sqlite3.connect('A4v1M.db')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Parts (partNumber integer PRIMARY KEY, partPrice integer, needsPart integer, madeIn text);")


    aList = copy.deepcopy(dfUPC["ean"])
    random.shuffle(aList)

    total = 1000000
    count = 0
    seen = set()
    while count != total:
        if aList[count] in seen:
            count += 1
            total += 1
            continue
        try:
            partNumber = int(aList[count])
            if partNumber > 2**63 - 1:
                count += 1
                total += 1
                continue
            seen.add(aList[count])
            count += 1
        except:
            count += 1
            total += 1
            continue
        partPrice = random.randint(1,101)
        gottem = False
        while not gottem:
            try:
                needsPart = int(random.choice(dfUPC["ean"]))
                if needsPart > 2**63 - 1:
                    continue
                gottem = True
            except:
                continue
        madeIn = random.choice(dfCountry["Code"])
        c.execute("INSERT INTO Parts VALUES (?, ?, ?, ?);", (partNumber, partPrice, needsPart, madeIn))

    c.execute("select COUNT(DISTINCT partNumber) FROM Parts;")
    
    print(c.fetchall())

    conn.commit()
    conn.close()

if __name__ == "__main__":
   main()
