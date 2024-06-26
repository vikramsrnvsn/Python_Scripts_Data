import sqlite3
import pandas as pd

db_path = '/Users/vikramsrinivasan/Documents/Optilogic/2023_DDM_DG_Template/2023_DDM_Training_Template.dgproj'    # Connect to the SQLite database
   conn = sqlite3.connect(db_path)

# List of tables in the database
tables = ['ProjectData','ConnectionData', 'MacroActionData', 'ConfiguredActionData', 'DesignerNoteData', 'ReplaceableParameterData', 'PropertyBagData', 'DatastoreContextData']
# Loop through each table and export to CSV
for table in tables:
    query = f"SELECT * FROM {table};"
    df = pd.read_sql_query(query, conn)
    df.to_csv(f'{table}.csv', index=False)

# Combine CSV files into one spreadsheet
combined_df = pd.concat([pd.read_csv(f'{table}.csv') for table in tables], ignore_index=True)
combined_df.to_excel('combined_tables.xlsx', index=False)

# Close the connection
conn.close()
