import pandas as pd
import os

Header = ["GSTIN of supplier","Invoice number","Invoice type","Invoice Date","Invoice Value (₹)","Place of supply","Supply Attract Reverse Charge","Rate (%)","Taxable Value","Integrated Tax","Central Tax","State/UT tax","Cess","GSTR-1/5 Filing Status","GSTR-3B Filing Status","Amendment made if any","Tax Period in which Amended","Effective date of cancellation","Source","IRN","IRN Date"]
dataframes = []
for files in os.listdir('Excel Files/'):

        dfs = pd.read_excel('Excel Files/'+files,sheet_name = "MyReport_Taxable_inward_supplie")
        temp = pd.DataFrame(dfs[3:])
        dataframes.append(temp)
data = pd.concat(dataframes)
data.columns = Header
data.to_csv('Final_Data.csv',index=False)