#Imports
import pandas as pd
import numpy as np
from datetime import datetime

SC_data = pd.read_excel('Excel_Files/Transformed/SC_Transformed_Data.xlsx')
SC_dates = pd.read_excel('Excel_Files/Dates/SC_Convoy_Dates.xlsx')
HX_data = pd.read_excel('Excel_Files/Transformed/HX_Transformed_Data.xlsx')
HX_dates = pd.read_excel('Excel_Files/Dates/HX_Convoy_Dates.xlsx')
OB_data = pd.read_excel('Excel_Files/Transformed/OB_Transformed_Data.xlsx')
OB_dates = pd.read_excel('Excel_Files/Dates/OB_Convoy_Dates.xlsx')
ON_data = pd.read_excel('Excel_Files/Transformed/ON_Transformed_Data.xlsx')
ON_dates = pd.read_excel('Excel_Files/Dates/ON_Convoy_Dates.xlsx')
ONS_data = pd.read_excel('Excel_Files/Transformed/ONS_Transformed_Data.xlsx')
ONS_dates = pd.read_excel('Excel_Files/Dates/ONS_Convoy_Dates.xlsx')

#print(SC_dates.head())
def SC_csv():
    df = pd.concat([SC_data, SC_dates], axis=1)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.set_index('SC Convoy Number')
    df['Depart_Date'] = pd.to_datetime(df['Depart_Date'].str.replace('.', ''), format="%d %B %Y")
    df['Arrive_Date'] = pd.to_datetime(df['Arrive_Date'].str.replace('.', ''), format="%d %B %Y")
    df.to_csv('SC_Data.csv')
    return df
#print(SC_csv().head())

def HX_csv():
    df = pd.concat([HX_data, HX_dates], axis=1)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.set_index('HX Convoy Number')
    df['Depart_Date'] = pd.to_datetime(df['Depart_Date'].str.replace('.', ''), format="%d %B %Y")
    df['Arrive_Date'] = pd.to_datetime(df['Arrive_Date'].str.replace('.', ''), format="%d %B %Y")
    df.to_csv('HX_Data.csv')
    return df
#print(HX_csv().head())

def OB_csv():
    df = pd.concat([OB_data, OB_dates], axis=1)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.set_index('OB Convoy Number')
    df['Depart_Date'] = pd.to_datetime(df['Depart_Date'].str.replace('.', ''), format="%d %B %Y")
    df['Dispersed_Date'] = pd.to_datetime(df['Dispersed_Date'].str.replace('.', ''), format="%d %B %Y")
    df.to_csv('OB_Data.csv')
    return df
#print(OB_csv().head())

def ON_csv():
    df = pd.concat([ON_data, ON_dates], axis=1)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.set_index('ON Convoy Number')
    df['Depart_Date'] = pd.to_datetime(df['Depart_Date'].str.replace('.', '').str.strip(), format='%d %B %Y', errors='coerce')
    df['Dispersed/Arrival Date'] = pd.to_datetime(df['Dispersed/Arrival Date'].str.replace('.', '').str.strip(), format='%d %B %Y', errors='coerce')
    #Weird issue with one of the Dispersed/Arrival Dates. Date was manually entred and does follow the same format as the others. 
    # Was fixed manually in the excel and csv files.
    df.to_csv('ON_Data.csv')
    return df
print(ON_csv().head())

def ONS_csv():
    df = pd.concat([ONS_data, ONS_dates], axis=1)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df = df.set_index('ONS Convoy Number')
    df['Depart_Date'] = pd.to_datetime(df['Depart_Date'].str.replace('.', ''), format="%d %B %Y")
    df['Dispersed/Arrival Date'] = pd.to_datetime(df['Dispersed/Arrival Date'].str.replace('.', ''), format="%d %B %Y")
    df.to_csv('ONS_Data.csv')
    return df
#print(ONS_csv().head())


#Add average number of U-Boats operating in the Atlantic Ocean 
U_Boat = {'1939-09': (6, 2), '1939-10': (3, 4), '1939-11': (4, 2), '1939-12': (2, 1), '1940-01': (7, 2), 
               '1940-02': (8, 5), '1940-03': (3, 2), '1940-04': (24, 7), '1940-05': (5, 1), '1940-06': (12, 11), 
               '1940-07': (5, 4), '1940-08': (9, 2), '1940-09': (7, 6), '1940-10': (7, 5), '1940-11': (8, 5), 
               '1940-12': (12, 3), '1941-01': (12, 3), '1941-02': (11, 0), '1941-03': (15, 9), '1941-04': (16, 3),
               '1941-05': (16, 1), '1941-06': (25, 6), '1941-07': (20, 2), '1941-08': (35, 5), '1941-09': (36, 7),
               '1941-10': (30, 2), '1941-11': (32, 4), '1941-12': (24, 13), '1942-01': (35, 5), '1942-02': (44, 33),
               '1942-03': (45, 7), '1942-04': (42, 2), '1942-05': (49, 5), '1942-06': (61, 8), '1942-07': (73, 12),
               '1942-08': (82, 16), '1942-09': (91, 9), '1942-10': (110, 13), '1942-11': (98, 18), '1942-12': (98, 6),
               '1943-01': (105, 8), '1943-02': (106, 20), '1943-03': (114, 13), '1943-04': (110, 14), '1943-05': (116, 37),
               '1943-06': (89, 13), '1943-07': (89, 40), '1943-08': (50, 22), '1943-09': (56, 8), '1943-10': (68, 28),
               '1943-11': (66, 16), '1943-12': (58, 6), '1944-01': (57, 15), '1944-02': (54, 18), '1944-03': (52, 20),
               '1944-04': (43, 14), '1944-05': (32, 19), '1944-06': (43, 24), '1944-07': (26, 16), '1944-08': (35, 22),
               '1944-09': (47, 11), '1944-10': (21, 6), '1944-11': (23, 4), '1944-12': (30, 8), '1945-01': (30, 4),
               '1945-02': (39, 13), '1945-03': (50, 10), '1945-04': (53, 21), '1945-05': (np.nan, np.nan)}
#This data comes from https://www.churchillarchive.com/catalogue-item?docid=CHAR20_238_2 

#Convert to Data Frame
U_Boat_df = pd.DataFrame(list(U_Boat.items()), columns=['Date', 'Data'])
U_Boat_df[['Average Number in Atlantic Ocean', 'U-Boats Sunk']] = pd.DataFrame(U_Boat_df['Data'].tolist(), index=U_Boat_df.index)
U_Boat_df = U_Boat_df.drop(columns=['Data'])
#U_Boat_df.to_csv('U-Boat-Data.csv')