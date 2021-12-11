import sqlite3
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import os

def sqliteto_csv(sqldb): #eg r"E:\Breached Databases\toindex2\americanmafia.org\session.sqlite"
    db = sqlite3.connect(sqldb)
    bpath = Path(sqldb).parent
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tqdm(tables):
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(os.path.join(bpath,table_name + '.csv'), index_label='index')
    cursor.close()
    db.close()
