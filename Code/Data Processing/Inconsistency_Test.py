#Imports
import pandas as pd

#Here the different convoy routes are cross referenced with another source to find instances where the sinking of a particular ship \
# does not align. 

SC_data = pd.read_excel('Excel_Files/Transformed/SC_Transformed_Data.xlsx')
HX_data = pd.read_excel('Excel_Files/Transformed/HX_Transformed_Data.xlsx')
OB_data = pd.read_excel('Excel_Files/Transformed/OB_Transformed_Data.xlsx')
ON_data = pd.read_excel('Excel_Files/Transformed/ON_Transformed_Data.xlsx')
ONS_data = pd.read_excel('Excel_Files/Transformed/ONS_Transformed_Data.xlsx')
UBoat_data = pd.read_excel('Excel_Files/UBoat.net_Ships_Sunk_Data.xlsx')

def Test_SC():
    SC = UBoat_data['Convoy'].str.contains('SC.', na=False)
    UBoat_data_SC = UBoat_data.loc[SC]
    UBoat_data_SC = UBoat_data_SC.reset_index(drop=True)
    UBoat_data_SC.rename(columns={'Convoy': 'SC Convoy Number'}, inplace=True)
    SC_data['SC Convoy Number'] = SC_data['SC Convoy Number'].str.replace('.', '-', regex=False)
    UBoat_data['Convoy'] = UBoat_data['Convoy'].str.replace('.', '-', regex=False)
    merged_SC = pd.merge(SC_data, UBoat_data, left_on='SC Convoy Number', right_on='Convoy', how='inner')
    SC_Differences = merged_SC[merged_SC['Number of Ships Sunk'] != merged_SC['Ships Sunk']]
    SC_Incosistent_data = SC_Differences[['SC Convoy Number', 'Number of Ships Sunk', 'Ships Sunk']]
    #SC_Incosistent_data.to_excel('SC_Differnces.xlsx') #Used to manually change incorrect entries
    return SC_Incosistent_data
#print(Test_SC().head()) 

def Test_HX():
    HX = UBoat_data['Convoy'].str.contains('HX.', na=False)
    UBoat_data_HX = UBoat_data.loc[HX]
    UBoat_data_HX = UBoat_data_HX.reset_index(drop=True)
    UBoat_data_HX.rename(columns={'Convoy': 'HX Convoy Number'}, inplace=True)
    HX_data['HX Convoy Number'] = HX_data['HX Convoy Number'].str.replace('.', '-', regex=False)
    UBoat_data['Convoy'] = UBoat_data['Convoy'].str.replace('.', '-', regex=False)
    merged_HX = pd.merge(HX_data, UBoat_data, left_on='HX Convoy Number', right_on='Convoy', how='inner')
    HX_Differences = merged_HX[merged_HX['Number of Ships Sunk'] != merged_HX['Ships Sunk']]
    HX_Incosistent_data = HX_Differences[['HX Convoy Number', 'Number of Ships Sunk', 'Ships Sunk']]
    #HX_Incosistent_data.to_excel('HX_Differnces.xlsx') #Used to manually change incorrect entries
    return HX_Incosistent_data
#print(Test_HX().head())

def Test_OB():
    OB = UBoat_data['Convoy'].str.contains('OB.', na=False)
    UBoat_data_OB = UBoat_data.loc[OB]
    UBoat_data_OB = UBoat_data_OB.reset_index(drop=True)
    UBoat_data_OB.rename(columns={'Convoy': 'OB Convoy Number'}, inplace=True)
    OB_data['OB Convoy Number'] = OB_data['OB Convoy Number'].str.replace('.', '-', regex=False)
    UBoat_data['Convoy'] = UBoat_data['Convoy'].str.replace('.', '-', regex=False)
    merged_OB = pd.merge(OB_data, UBoat_data, left_on='OB Convoy Number', right_on='Convoy', how='inner')
    OB_Differences = merged_OB[merged_OB['Number of Ships Sunk'] != merged_OB['Ships Sunk']]
    OB_Incosistent_data = OB_Differences[['OB Convoy Number', 'Number of Ships Sunk', 'Ships Sunk']]
    #OB_Incosistent_data.to_excel('OB_Differnces.xlsx') #Used to manually change incorrect entries
    return OB_Incosistent_data
#print(Test_OB().head())

def Test_ON():
    ON = UBoat_data['Convoy'].str.contains('ONS.', na=False)
    UBoat_data_ON = UBoat_data.loc[ON]
    UBoat_data_ON = UBoat_data_ON.reset_index(drop=True)
    UBoat_data_ON.rename(columns={'Convoy': 'ON Convoy Number'}, inplace=True)
    ON_data['ON Convoy Number'] = ON_data['ON Convoy Number'].str.replace('.', '-', regex=False)
    UBoat_data['Convoy'] = UBoat_data['Convoy'].str.replace('.', '-', regex=False)
    merged_ON = pd.merge(ON_data, UBoat_data, left_on='ON Convoy Number', right_on='Convoy', how='inner')
    ON_Differences = merged_ON[merged_ON['Number of Ships Sunk'] != merged_ON['Ships Sunk']]
    ON_Incosistent_data = ON_Differences[['ON Convoy Number', 'Number of Ships Sunk', 'Ships Sunk']]
    ON_Incosistent_data.to_excel('ON_Differnces.xlsx') #Used to manually change incorrect entries
    return ON_Incosistent_data
#print(Test_ON().head())

def Test_ONS():
    ONS = UBoat_data['Convoy'].str.contains('ONS.', na=False)
    UBoat_data_ONS = UBoat_data.loc[ONS]
    UBoat_data_ONS = UBoat_data_ONS.reset_index(drop=True)
    UBoat_data_ONS.rename(columns={'Convoy': 'ONS Convoy Number'}, inplace=True)
    ONS_data['ONS Convoy Number'] = ONS_data['ONS Convoy Number'].str.replace('.', '-', regex=False)
    UBoat_data['Convoy'] = UBoat_data['Convoy'].str.replace('.', '-', regex=False)
    merged_ONS = pd.merge(ONS_data, UBoat_data, left_on='ONS Convoy Number', right_on='Convoy', how='inner')
    ONS_Differences = merged_ONS[merged_ONS['Number of Ships Sunk'] != merged_ONS['Ships Sunk']]
    ONS_Incosistent_data = ONS_Differences[['ONS Convoy Number', 'Number of Ships Sunk', 'Ships Sunk']]
    ONS_Incosistent_data.to_excel('ONS_Differnces.xlsx') #Used to manually change incorrect entries
    return ONS_Incosistent_data
#print(Test_ONS().head())
