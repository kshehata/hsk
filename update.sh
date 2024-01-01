#! /bin/bash

cp ~/Downloads/HSK\ Word\ Lists\ -\ hsk_out.csv hsk_all.csv
python convert.py
sed -i "" -e 's/\r//g' *.csv
