#!/usr/bin/env python3

import duckdb
import timeit
from os import remove

try:
    remove("my-db.duckdb")
except:
    pass
con = duckdb.connect(database="my-db.duckdb", read_only=False)


# enable the progress bar
con.execute('PRAGMA enable_progress_bar')
con.execute('PRAGMA enable_print_progress_bar;')
# enable parallel CSV loading
con.execute("SET experimental_parallel_csv=true")
# disable preservation of insertion order
con.execute("SET preserve_insertion_order=false")

# Don't perform the actual load since that is done by benchmark.sh using SQLite

# print("Will load the data")
# start = timeit.default_timer()

# con.execute(open("create.sql").read())
# con.execute("COPY hits FROM 'small_hits.csv'")
# end = timeit.default_timer()
# print(end - start)

# Register the SQLite DB tables as views in DuckDB
con.execute("INSTALL sqlite_scanner;")
con.execute("LOAD sqlite_scanner;")
con.execute("CALL sqlite_attach('mydb');")