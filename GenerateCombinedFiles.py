import pandas as pd
import os

Header = ["GSTIN of supplier","Trade/Legal name of the Supplier","Invoice number","Invoice type","Invoice Date","Invoice Value (₹)","Place of supply","Supply Attract Reverse Charge","Rate (%)","Taxable Value (₹)","Integrated Tax  (₹)","Central Tax (₹)","State/UT tax (₹)","Cess  (₹)","Counter Party Return status"]
dataframes = []
for files in os.listdir('Excel Files/'):

        dfs = pd.read_excel('Excel Files/'+files,sheet_name = "B2B")
        temp = pd.DataFrame(dfs[5:])
        dataframes.append(temp)
data = pd.concat(dataframes)
data.columns = Header
data.to_csv('Final_Data.csv',index=False)