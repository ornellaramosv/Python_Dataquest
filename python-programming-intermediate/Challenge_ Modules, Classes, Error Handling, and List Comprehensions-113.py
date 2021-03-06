## 2. Introduction to the Data ##

import csv

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
nfl_suspensions = list(csv.reader(open("nfl_suspensions_data.csv",'r')))
nfl_suspensions = Dataset(nfl_suspensions).data

years = {}

for item in nfl_suspensions:
    row_year = item[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1

print(years)

## 3. Unique Values ##

team = [item[1] for item in nfl_suspensions]
unique_teams = set(team)
print(unique_teams)

game = [item[2] for item in nfl_suspensions]
unique_games = set(game)
print(unique_games)

## 4. Suspension Class ##

class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
        
third_suspension = Suspension(nfl_suspensions[2])
third_suspension

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()