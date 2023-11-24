#Imports 
import pandas as pd
import numpy as np

#In this file, five convoy routes are compiled into on csv file. Sink percentages (overall, escort, and straggler) \
# are also calculated, along with the addition of seven new features. 

#After the different routes were compiled, a couple entries had to be manually changed due to unforseen issues with the raw data. 

#DataFrames
sc = pd.read_csv('Excel_Files/Complete_Data/SC_Data.csv')
ob = pd.read_csv('Excel_Files/Complete_Data/OB_Data.csv')
hx = pd.read_csv('Excel_Files/Complete_Data/HX_Data.csv')
on = pd.read_csv('Excel_Files/Complete_Data/ON_Data.csv')
ons = pd.read_csv('Excel_Files/Complete_Data/ONS_Data.csv')

#Calculate Sink Rates
def Divide(a,b):
    if b == 0:
        return np.nan
    return a / b

sc['Overall Sink Percentage'] = sc.apply(lambda row: Divide(row['Number of Ships Sunk'], row['Number of Ships'], ), axis=1)
sc['Escort Sink Percentage'] = sc.apply(lambda row: Divide(row['Number of Escorts Sunk'], row['Number of Escort Ships']), axis=1)
sc['Straggler Sink Percentage'] = sc.apply(lambda row: Divide(row['Number of Stragglers Sunk'], row['Number of Stragglers'],), axis=1)
sc['Overall Sink Percentage'] = sc['Overall Sink Percentage'] * 100
sc['Escort Sink Percentage'] = sc['Escort Sink Percentage'] * 100
sc['Straggler Sink Percentage'] = sc['Straggler Sink Percentage'] * 100
sc['Depart_Date'] = pd.to_datetime(sc['Depart_Date'], errors='coerce')
sc['YearMonth'] = sc['Depart_Date'].dt.to_period('M')
sc = sc.fillna(0)

ob['Overall Sink Percentage'] = ob.apply(lambda row: Divide(row['Number of Ships Sunk'], row['Number of Ships'], ), axis=1)
ob['Escort Sink Percentage'] = ob.apply(lambda row: Divide(row['Number of Escorts Sunk'], row['Number of Escort Ships']), axis=1)
ob['Straggler Sink Percentage'] = ob.apply(lambda row: Divide(row['Number of Stragglers Sunk'], row['Number of Stragglers'],), axis=1)
ob['Overall Sink Percentage'] = ob['Overall Sink Percentage'] * 100
ob['Escort Sink Percentage'] = ob['Escort Sink Percentage'] * 100
ob['Straggler Sink Percentage'] = ob['Straggler Sink Percentage'] * 100
ob_clean = ob.dropna(subset=['Dispersed_Date']) #Some OB Convoys Formed OG Convoys soon after departing
ob_clean['Depart_Date'] = pd.to_datetime(ob['Depart_Date'], errors='coerce')
ob_clean['YearMonth'] = ob_clean['Depart_Date'].dt.to_period('M')
ob_clean = ob_clean.fillna(0)

hx['Overall Sink Percentage'] = hx.apply(lambda row: Divide(row['Number of Ships Sunk'], row['Number of Ships'], ), axis=1)
hx['Escort Sink Percentage'] = hx.apply(lambda row: Divide(row['Number of Escorts Sunk'], row['Number of Escort Ships']), axis=1)
hx['Straggler Sink Percentage'] = hx.apply(lambda row: Divide(row['Number of Stragglers Sunk'], row['Number of Stragglers'],), axis=1)
hx['Overall Sink Percentage'] = hx['Overall Sink Percentage'] * 100
hx['Escort Sink Percentage'] = hx['Escort Sink Percentage'] * 100
hx['Straggler Sink Percentage'] = hx['Straggler Sink Percentage'] * 100
hx['Depart_Date'] = pd.to_datetime(hx['Depart_Date'], errors='coerce')
hx['YearMonth'] = hx['Depart_Date'].dt.to_period('M')
hx = hx.fillna(0)

on['Overall Sink Percentage'] = on.apply(lambda row: Divide(row['Number of Ships Sunk'], row['Number of Ships'], ), axis=1)
on['Escort Sink Percentage'] = on.apply(lambda row: Divide(row['Number of Escorts Sunk'], row['Number of Escort Ships']), axis=1)
on['Straggler Sink Percentage'] = on.apply(lambda row: Divide(row['Number of Stragglers Sunk'], row['Number of Stragglers'],), axis=1)
on['Overall Sink Percentage'] = on['Overall Sink Percentage'] * 100
on['Escort Sink Percentage'] = on['Escort Sink Percentage'] * 100
on['Straggler Sink Percentage'] = on['Straggler Sink Percentage'] * 100
on['Depart_Date'] = pd.to_datetime(on['Depart_Date'], errors='coerce')
on['YearMonth'] = on['Depart_Date'].dt.to_period('M')
on = on.fillna(0)

ons['Overall Sink Percentage'] = ons.apply(lambda row: Divide(row['Number of Ships Sunk'], row['Number of Ships'], ), axis=1)
ons['Escort Sink Percentage'] = ons.apply(lambda row: Divide(row['Number of Escorts Sunk'], row['Number of Escort Ships']), axis=1)
ons['Straggler Sink Percentage'] = ons.apply(lambda row: Divide(row['Number of Stragglers Sunk'], row['Number of Stragglers'],), axis=1)
ons['Overall Sink Percentage'] = ons['Overall Sink Percentage'] * 100
ons['Escort Sink Percentage'] = ons['Escort Sink Percentage'] * 100
ons['Straggler Sink Percentage'] = ons['Straggler Sink Percentage'] * 100
ons['Depart_Date'] = pd.to_datetime(ons['Depart_Date'], errors='coerce')
ons['YearMonth'] = ons['Depart_Date'].dt.to_period('M')
ons = ons.fillna(0)

#Combine Data Frames
sc = sc.rename(columns={'SC Convoy Number': 'Convoy Number', 'Arrive_Date': 'Arrival/Dispersal Date'})
ob_clean = ob_clean.rename(columns={'OB Convoy Number': 'Convoy Number', 'Dispersed_Date': 'Arrival/Dispersal Date'})
hx = hx.rename(columns={'HX Convoy Number': 'Convoy Number', 'Arrive_Date': 'Arrival/Dispersal Date'})
on = on.rename(columns={'ON Convoy Number': 'Convoy Number', 'Dispersed/Arrival Date': 'Arrival/Dispersal Date'})
ons = ons.rename(columns={'ONS Convoy Number': 'Convoy Number', 'Dispersed/Arrival Date': 'Arrival/Dispersal Date'})
frames = [sc, ob_clean, hx, on, ons]
df = pd.concat(frames, ignore_index=True)
#print(df.head(-1))
df.loc[df['Depart_Date'].apply(lambda x: isinstance(x, int)), 'Depart_Date'] = pd.NaT
df = df.sort_values(by='Depart_Date')

#Add New Features

#Add average number of U-Boats in Atlantic feature. The data comes from https://www.churchillarchive.com/catalogue-item?docid=CHAR20_238_1 
U_Boats = pd.read_csv('Excel_Files/U-Boat-Data.csv')
U_Boats['Date'] = pd.to_datetime(U_Boats['Date'])
U_Boats['YearMonth'] = U_Boats['Date'].dt.to_period('M')
U_Boats_Dict = U_Boats.set_index('YearMonth')['Average Number in Atlantic Oceane'].to_dict()
df['Avg Number of U-Boats in Atlantic'] = df['YearMonth'].map(U_Boats_Dict)
df.drop('YearMonth', axis=1, inplace=True)

#Add Escort Ratio 
df['Escort Ratio'] = df['Number of Escort Ships'] / df['Number of Ships']

#Add Time at Sea
df['Arrival/Dispersal Date'] = pd.to_datetime(df['Arrival/Dispersal Date'])
df['Depart_Date'] = pd.to_datetime(df['Depart_Date'])
df['Time At Sea (Days)'] = (df['Arrival/Dispersal Date'] - df['Depart_Date']).dt.days

#Add Year and Month
df['Month'] = df['Depart_Date'].dt.month
df['Year'] = df['Depart_Date'].dt.year

#Add Prevoius Month's Sink Percentage 
monthly_avg_sink_percentage = df.groupby(['Year', 'Month'])['Overall Sink Percentage'].mean().reset_index()
monthly_avg_sink_percentage['Previous Month Avg Sink %'] = monthly_avg_sink_percentage['Overall Sink Percentage'].shift(1)
monthly_avg_sink_percentage.iloc[0, monthly_avg_sink_percentage.columns.get_loc('Previous Month Avg Sink %')] = None
df = pd.merge(df, monthly_avg_sink_percentage[['Year', 'Month', 'Previous Month Avg Sink %']], on=['Year', 'Month'], how='left')
df = df.fillna(0)
#df['Historic Sink Percentage'] = df['Overall Sink Percentage'].rolling(window=3, min_periods=1).mean().shift(1)

#Add Spproximate Sighting Range. Equation comes from https://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html 
def Approx_Sighting_Range(convoy_size):
    b = 0.1 # Fraction of the time a ship smokes
    R_1 = 4.0 # Max visual Range of ship, can be changed
    R_2 = 24.0 # Max visual range of smoke, can be changed. Absolute Max = 40
    convoy_range = float((R_2 - (1 - b)**convoy_size * (R_2 - R_1)))
    return convoy_range
df['Approx. Sighting Range'] = df['Number of Ships'].apply(Approx_Sighting_Range)

#print(df.head(-1))
#df.to_csv('Complete_Convoy_Data.csv')