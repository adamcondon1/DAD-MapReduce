REM Locally test topNameByCount mapper and reducer

mkdir output

REM Run mapper 
type input\dogNames.csv
type input\dogNames.csv | topNameByCountMapper.py
type input\dogNames.csv | topNameByCountMapper.py > output\topNameByCountMapper_output.txt

REM Run mapper 
type input\dogNames.csv | topNameByCountMapper.py >> output\topNameByCountMapper_output.txt

REM View the mappers (sorted)
type output\topNameByCountMapper_output.txt | sort

REM Run the reducer
type output\topNameByCountMapper_output.txt | sort | topNameByCountReducer.py

REM Run the reducer, output to file
type output\topNameByCountMapper_output.txt | sort | topNameByCountReducer.py > output\topNameByCountReducer_output.txt

REM Wait for user to press a key
PAUSE