#!/bin/bash

# Install

# Launch on AWS with: sudo nohup sh benchmark.sh &
sudo apt-get update
sudo apt-get install -y python3-pip
pip install duckdb psutil

sudo apt-get install -y sqlite3

# sudo rm ./mydb
# sqlite3 mydb < create.sql

# wget --continue 'https://datasets.clickhouse.com/hits_compatible/hits.csv.gz'
# gzip -d hits.csv.gz

# time sqlite3 mydb ".mode csv" ".import hits.csv hits"

wc -c mydb

sudo python3 ./duckdb_setup.py

# Run the queries
sudo bash ./run.sh 2>&1 | tee log.txt

wc -c my-db.duckdb

cat log.txt | grep -P '^\d|Killed|Segmentation' | sed -r -e 's/^.*(Killed|Segmentation).*$/null\nnull\nnull/' |
    awk '{ if (i % 3 == 0) { printf "[" }; printf $1; if (i % 3 != 2) { printf "," } else { print "]," }; ++i; }'

cat log.txt | grep -P '^\d|Killed|Segmentation' | sed -r -e 's/^.*(Killed|Segmentation).*$/null\nnull\nnull/' |
    awk '{ if (i % 3 == 0) { printf "" }; printf $1; if (i % 3 != 2) { printf "," } else { print "" }; ++i; }' > ./results/results.csv