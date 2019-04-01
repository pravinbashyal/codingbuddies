# Write a csv parser that parses the csv and returns corresponding dictionary for it.

for eg
```python
Name,Age,Gender
Ash, 11, M
Misty, 10, F

# above text will be turned to
[
    {"Name": "Ash", "Age": 11, "Gender": "M"},
    {"Name": "Misty", "Age": 10, "Gender": "F"},
]

def csv_to_json(csv_string, delimitter): # above delimiter is ','. In some cases it could be tab or ';'
    json = {}
    # your code here
    return json
```
# use the code written above to parse the data from provided url

```python
from urllib.request import urlopen

# data for deutschbahn
data_url = "http://download-data.deutschebahn.com/static/datasets/stationsdaten/DBSuS-Uebersicht_Bahnhoefe-Stand2016-07.csv"

# imports and prints data by each line
dataResponse = urlopen(data_url)

data = ""

for line in dataResponse:
    data = data + line.decode("utf-8")
    print(line)

stations = csv_to_json(data)
```

# Above is data for stations in Germany
# Now find the City with least and most number of stations respectively.

