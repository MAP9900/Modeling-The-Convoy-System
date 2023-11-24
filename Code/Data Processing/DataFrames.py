#Imports
import pandas as pd
import numpy as np
import re

#Cleaning all the Convoy DataFrames  SC, HX, OB, ON All Complete

SC_data = pd.read_excel('Excel_Files/Raw_Data/SC_Convoy_Data_1.xlsx')
def Clean_Data_SC(SC_data):
    SC_data.set_index('SC Convoy Number', inplace=True)
    SC_data['Number of Ships'] = SC_data.groupby('SC Convoy Number')['Vessel'].transform('count')
    SC_data['Number of Ships Sunk'] = SC_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())\
        .groupby(SC_data.index).transform('sum')
    SC_data['Number of Escort Ships'] = SC_data['Notes'].apply(lambda x: 'escort' in str(x).lower())\
        .groupby(SC_data.index).transform('sum')
    SC_data['Tons'] = SC_data['Tons'].replace({',': ''}, regex=True).astype(float)
    sunk_ships = SC_data[SC_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())]
    sunk_ships_tons_grouped = sunk_ships.groupby('SC Convoy Number')['Tons'].sum()
    SC_data['Total Tons of Convoy'] = SC_data['Tons'].groupby(SC_data.index).transform('sum')
    SC_data['Total Tons of Ships Sunk'] = SC_data.index.map(sunk_ships_tons_grouped)
    SC_data['Number of Escorts Sunk'] = SC_data['Notes'].apply(lambda x: 'escort' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(SC_data.index).transform('sum')
    SC_data['Number of Stragglers'] = SC_data['Notes'].apply(lambda x: 'stragg' in str(x).lower())\
        .groupby(SC_data.index).transform('sum')
    SC_data['Number of Stragglers Sunk'] = SC_data['Notes'].apply(lambda x: 'stragg' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(SC_data.index).transform('sum')
    SC = SC_data[['Number of Ships', 'Number of Escort Ships', 'Number of Stragglers', 'Number of Ships Sunk',\
                  'Number of Escorts Sunk', 'Number of Stragglers Sunk', 'Total Tons of Convoy',\
                  'Total Tons of Ships Sunk']].drop_duplicates()
    SC['Total Tons of Ships Sunk'] = SC['Total Tons of Ships Sunk'].fillna(0)
    SC.to_excel('SC_Transformed_Data.xlsx')
    return SC
#print(Clean_Data_SC(SC_data).head())

HX_Data = pd.read_excel('Excel_Files/Raw_Data/HX_Convoy_Data_1.xlsx')
def Clean_Data_HX(HX_data):
    HX_data.set_index('HX Convoy Number', inplace=True)
    HX_data['Number of Ships'] = HX_data.groupby('HX Convoy Number')['Vessel'].transform('count')
    HX_data['Number of Ships Sunk'] = HX_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())\
        .groupby(HX_data.index).transform('sum')
    HX_data['Number of Escort Ships'] = HX_data['Notes'].apply(lambda x: 'escort' in str(x).lower())\
        .groupby(HX_data.index).transform('sum')
    HX_data['Tons'] = HX_data['Tons'].replace({',': ''}, regex=True).astype(float)
    sunk_ships = HX_data[HX_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())]
    sunk_ships_tons_grouped = sunk_ships.groupby('HX Convoy Number')['Tons'].sum()
    HX_data['Total Tons of Convoy'] = HX_data['Tons'].groupby(HX_data.index).transform('sum')
    HX_data['Total Tons of Ships Sunk'] = HX_data.index.map(sunk_ships_tons_grouped)
    HX_data['Number of Escorts Sunk'] = HX_data['Notes'].apply(lambda x: 'escort' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(HX_data.index).transform('sum')
    HX_data['Number of Stragglers'] = HX_data['Notes'].apply(lambda x: 'stragg' in str(x).lower())\
        .groupby(HX_data.index).transform('sum')
    HX_data['Number of Stragglers Sunk'] = HX_data['Notes'].apply(lambda x: 'stragg' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(HX_data.index).transform('sum')
    HX = HX_data[['Number of Ships', 'Number of Escort Ships', 'Number of Stragglers', 'Number of Ships Sunk',\
                  'Number of Escorts Sunk', 'Number of Stragglers Sunk', 'Total Tons of Convoy',\
                  'Total Tons of Ships Sunk']].drop_duplicates()
    HX['Total Tons of Ships Sunk'] = HX['Total Tons of Ships Sunk'].fillna(0)
    HX.to_excel('HX_Transformed_Data.xlsx')
    return HX
#print(Clean_Data_HX(HX_Data).head())

OB_Data = pd.read_excel('Excel_Files/Raw_Data/OB_Convoy_Data_1.xlsx')
def Clean_Data_OB(OB_data):
    OB_data.set_index('OB Convoy Number', inplace=True)
    OB_data['Number of Ships'] = OB_data.groupby('OB Convoy Number')['Vessel'].transform('count')
    OB_data['Number of Ships Sunk'] = OB_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())\
        .groupby(OB_data.index).transform('sum')
    OB_data['Number of Escort Ships'] = OB_data['Notes'].apply(lambda x: 'escort' in str(x).lower())\
        .groupby(OB_data.index).transform('sum')
    OB_data['Tons'] = OB_data['Tons'].replace({',': ''}, regex=True).astype(float)
    sunk_ships = OB_data[OB_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())]
    sunk_ships_tons_grouped = sunk_ships.groupby('OB Convoy Number')['Tons'].sum()
    OB_data['Total Tons of Convoy'] = OB_data['Tons'].groupby(OB_data.index).transform('sum')
    OB_data['Total Tons of Ships Sunk'] = OB_data.index.map(sunk_ships_tons_grouped)
    OB_data['Number of Escorts Sunk'] = OB_data['Notes'].apply(lambda x: 'escort' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(OB_data.index).transform('sum')
    OB_data['Number of Stragglers'] = OB_data['Notes'].apply(lambda x: 'stragg' in str(x).lower())\
        .groupby(OB_data.index).transform('sum')
    OB_data['Number of Stragglers Sunk'] = OB_data['Notes'].apply(lambda x: 'stragg' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(OB_data.index).transform('sum')
    OB = OB_data[['Number of Ships', 'Number of Escort Ships', 'Number of Stragglers', 'Number of Ships Sunk',\
                  'Number of Escorts Sunk', 'Number of Stragglers Sunk', 'Total Tons of Convoy',\
                  'Total Tons of Ships Sunk']].drop_duplicates()
    OB['Total Tons of Ships Sunk'] = OB['Total Tons of Ships Sunk'].fillna(0)
    OB.to_excel('OB_Transformed_Data.xlsx')
    return OB
#print(Clean_Data_OB(OB_Data).head())

ON_Data = pd.read_excel('Excel_Files/Raw_Data/ON_Convoy_Data_1.xlsx')
def Clean_Data_ON(ON_data):
    ON_data.set_index('ON Convoy Number', inplace=True)
    ON_data['Number of Ships'] = ON_data.groupby('ON Convoy Number')['Vessel'].transform('count')
    ON_data['Number of Ships Sunk'] = ON_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())\
        .groupby(ON_data.index).transform('sum')
    ON_data['Number of Escort Ships'] = ON_data['Notes'].apply(lambda x: 'escort' in str(x).lower())\
        .groupby(ON_data.index).transform('sum')
    ON_data['Tons'] = ON_data['Tons'].replace({',': ''}, regex=True).astype(float)
    sunk_ships = ON_data[ON_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())]
    sunk_ships_tons_grouped = sunk_ships.groupby('ON Convoy Number')['Tons'].sum()
    ON_data['Total Tons of Convoy'] = ON_data['Tons'].groupby(ON_data.index).transform('sum')
    ON_data['Total Tons of Ships Sunk'] = ON_data.index.map(sunk_ships_tons_grouped)
    ON_data['Number of Escorts Sunk'] = ON_data['Notes'].apply(lambda x: 'escort' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(ON_data.index).transform('sum')
    ON_data['Number of Stragglers'] = ON_data['Notes'].apply(lambda x: 'stragg' in str(x).lower())\
        .groupby(ON_data.index).transform('sum')
    ON_data['Number of Stragglers Sunk'] = ON_data['Notes'].apply(lambda x: 'stragg' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(ON_data.index).transform('sum')
    ON = ON_data[['Number of Ships', 'Number of Escort Ships', 'Number of Stragglers', 'Number of Ships Sunk',\
                  'Number of Escorts Sunk', 'Number of Stragglers Sunk', 'Total Tons of Convoy',\
                  'Total Tons of Ships Sunk']].drop_duplicates()
    ON['Total Tons of Ships Sunk'] = ON['Total Tons of Ships Sunk'].fillna(0)
    ON.to_excel('ON_Transformed_Data.xlsx')
    return ON
print(Clean_Data_ON(ON_Data).head())

ONS_Data = pd.read_excel('Excel_Files/Raw_Data/ONS_Convoy_Data_1.xlsx')
def Clean_Data_ONS(ONS_data):
    ONS_data.set_index('ONS Convoy Number', inplace=True)
    ONS_data['Number of Ships'] = ONS_data.groupby('ONS Convoy Number')['Vessel'].transform('count')
    ONS_data['Number of Ships Sunk'] = ONS_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())\
        .groupby(ONS_data.index).transform('sum')
    ONS_data['Number of Escort Ships'] = ONS_data['Notes'].apply(lambda x: bool(re.search(r'escort\s*\d+', str(x).lower())))\
        .groupby(ONS_data.index).transform('sum')
    ONS_data['Tons'] = ONS_data['Tons'].replace({',': ''}, regex=True).astype(float)
    sunk_ships = ONS_data[ONS_data['Notes'].apply(lambda x: 'sunk' in str(x).lower())]
    sunk_ships_tons_grouped = sunk_ships.groupby('ONS Convoy Number')['Tons'].sum()
    ONS_data['Total Tons of Convoy'] = ONS_data['Tons'].groupby(ONS_data.index).transform('sum')
    ONS_data['Total Tons of Ships Sunk'] = ONS_data.index.map(sunk_ships_tons_grouped)
    ONS_data['Number of Escorts Sunk'] = ONS_data['Notes'].apply(lambda x: bool(re.search(r'escort\s*\d+', str(x).lower())) and 'sunk' in str(x).lower())\
        .groupby(ONS_data.index).transform('sum')
    ONS_data['Number of Stragglers'] = ONS_data['Notes'].apply(lambda x: 'stragg' in str(x).lower())\
        .groupby(ONS_data.index).transform('sum')
    ONS_data['Number of Stragglers Sunk'] = ONS_data['Notes'].apply(lambda x: 'stragg' in str(x).lower() and 'sunk' in str(x).lower())\
        .groupby(ONS_data.index).transform('sum')
    ONS = ONS_data[['Number of Ships', 'Number of Escort Ships', 'Number of Stragglers', 'Number of Ships Sunk',\
                  'Number of Escorts Sunk', 'Number of Stragglers Sunk', 'Total Tons of Convoy',\
                  'Total Tons of Ships Sunk']].drop_duplicates()
    ONS['Total Tons of Ships Sunk'] = ONS['Total Tons of Ships Sunk'].fillna(0)
    ONS.to_excel('ONS_Transformed_Data.xlsx')
    return ONS
#print(Clean_Data_ONS(ONS_Data).head())