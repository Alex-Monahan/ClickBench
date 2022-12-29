#!/usr/bin/env python3

import duckdb
import timeit
import sys
import traceback

try: 
    query = sys.stdin.read()
    print(query)

    con = duckdb.connect(database="my-db.duckdb", read_only=False)
    con.execute("LOAD sqlite_scanner;")
    for try_num in range(3):
        start = timeit.default_timer()
        results = con.execute(query).fetchall()
        end = timeit.default_timer()
        print(end - start)
        del results
except:
    traceback.print_exc()