#import openpyxl
#openpyxl.__version__

import sqlite3
import pandas as pd
from sqlalchemy import create_engine

file = 'SampleData.xlsx'
output = 'output.xlsx'

engine = create_engine('sqlite://', echo=False)   # not to store into database
df = pd.read_excel(file, sheet_name='SalesOrders')
#print(df)
df.to_sql('salesorders', engine, if_exists='replace', index=False)

# results = engine.execute("SELECT * FROM salesorders")
# results = engine.execute("SELECT * FROM salesorders WHERE Region='East' \
#                                             AND Units>50")
results = engine.execute("SELECT * FROM salesorders WHERE Region in('East', 'West') \
                                            AND Units>50")
final = pd.DataFrame(results, columns=df.columns)
# final.to_excel(output, index=False)

print(final)
