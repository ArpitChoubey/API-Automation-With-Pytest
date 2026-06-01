import csv
import pandas
import pandas as pd

# pip install pandas
class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open('.venv/APi Intregation/UserData.csv') as csvfile:
            reader= csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('.venv/APi Intregation/UserData.csv')
        print(df)