REM ==================================================================================
REM Windows batch script to locally test the mapper and reducer
REM ==================================================================================

REM type vgsales.csv

REM Run mapper and print output to STDOUT
type vgsales.csv | python wordCountCleanMapper.py
REM Run mapper and write output to text file
type vgsales.csv | python wordCountCleanMapper.py > wordCountCleanMapper_output.txt

REM Run mapper, sort and reducer and print output to STDOUT
type vgsales.csv | python wordCountCleanMapper.py | sort | python wordCountCleanReducer.py
REM Run mapper, sort and reducer and write output to text file
type vgsales.csv | python wordCountCleanMapper.py | sort | python wordCountCleanReducer.py > wordCountCleanReducer_output.txt

REM Wait for user to press a key
PAUSE