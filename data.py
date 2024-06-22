import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
 


class SalesData():

    def __init__(self):
        self._dfProduct = None
        self._dfTransaction = None
        self._dfData = None
        self._dfRFM = None
        
        #self.load()
        
#-------------------------------------------------------------------------------------
    @property
    def Product(self):
        return self._dfProduct

    @property
    def Transaction(self):
        return self._dfTransaction
    
    @property
    def Data(self):
        return self._dfData
    
    @property
    def RFM(self):
        return self._dfRFM
        
#-------------------------------------------------------------------------------------
    def load(self):
        self._dfProduct = pd.read_csv("input_data/Products_with_Prices.csv")
        self._dfTransaction = pd.read_csv("output_data/transactions.csv")
        self._dfData = pd.read_csv("output_data/data.csv")
        self._dfRFM = pd.read_csv("output_data/customer_rfm.csv")
        
        self._dfTransaction["order_date"] = pd.to_datetime(self._dfTransaction["order_date"], format="%Y-%m-%d")
        self._dfData["order_date"] = pd.to_datetime(self._dfData["order_date"], format="%Y-%m-%d")
        

#-------------------------------------------------------------------------------------
    def pre_proccess(self):
        dfProduct = pd.read_csv("input_data/Products_with_Prices.csv")
        dfTransaction = pd.read_csv("input_data/Transactions.csv")
        
        dfTransaction["date"] = dfTransaction["date"].apply(lambda x: x.replace("/", "-"))
        dfTransaction["order_date"] = pd.to_datetime(dfTransaction["date"], format="%d-%m-%Y")
        
        encoder = LabelEncoder()
        encoded_data = encoder.fit_transform(dfTransaction["member_number"].astype(str) + " " + dfTransaction["order_date"].astype(str))
        dfTransaction["orderId"] = encoded_data
        dfTransaction = dfTransaction[["member_number", "productId", "items", "order_date", "orderId"]]
        
        dfData = pd.merge(dfProduct, dfTransaction, on="productId")
        dfData["total"] = dfData["items"] * dfData["price"]
        dfData = dfData[["member_number", "orderId", "order_date", "total", "productName", "items"]]
 
        dfRFM = self.calculate_RFM(dfData)
        dfRFM = dfRFM.rename(columns={"Days": "Recency", "orderId": "Frequency", "total": "Monetary"})
        
        # luu lai du lieu
        dfTransaction.to_csv("output_data/transactions.csv", index=False)
        dfData.to_csv("output_data/data.csv", index=False)
        dfRFM.to_csv("output_data/rfm.csv", index=False)

#-------------------------------------------------------------------------------------
    def calculate_RFM(self, dfData):
        Frequency = lambda x : len(x.unique())
        Monetary = lambda x : round(sum(x), 2)
        
        dfFM = dfData.groupby("member_number").agg({"orderId": Frequency, "total": Monetary }).reset_index()
        
        #
        dfTemp = dfData
        for m in dfTemp["member_number"].unique():
            max_date = datetime(2015, 12, 30)
            for i, r in dfTemp[dfTemp["member_number"] == m].sort_values("order_date", ascending=False).iterrows():
                d = (max_date - r["order_date"]).days
                max_date = r["order_date"]
                dfTemp.loc[i, "Days"] = d
        
        dfTemp = dfTemp[dfTemp["Days"] > 0]
        Recency = lambda x : x.mean()
        dfR = dfTemp.groupby("member_number").agg({"Days": Recency}).reset_index()
        
        return pd.merge(dfR, dfFM, on="member_number")
    
#-------------------------------------------------------------------------------------
    def product_R(self, dfData):
                
        dfTemp = dfData
        for m in dfTemp["productName"].unique():
            max_date = datetime(2015, 12, 30)
            for i, r in dfTemp[dfTemp["productName"] == m].sort_values("order_date", ascending=False).iterrows():
                d = (max_date - r["order_date"]).days
                max_date = r["order_date"]
                dfTemp.loc[i, "Days"] = d
        
        dfTemp = dfTemp[dfTemp["Days"] > 0]
        Recency = lambda x : x.mean()
        dfR = dfTemp.groupby("productName").agg({"Days": Recency}).reset_index()
        dfR = dfR.rename(columns={"Days": "Recency"})
        dfR.to_csv("output_data/product_r.csv", index=False)

#-------------------------------------------------------------------------------------
    def rfm_level(self, df):    
        if df["R"] > 3 and df["F"] > 1:
            return "ACTIVE"
        elif df["R"] == 1 and df["F"] == 1 and df["M"] == 1:
            return "NEW"
        else:
            return "REGULARS"   

#-------------------------------------------------------------------------------------
    def customer_RFM(self):
        
        df = pd.read_csv("output_data/rfm.csv")
        
        r_labels = range(4, 0, -1)
        f_labels = range(1, 5)
        m_labels = range(1, 5)

        r_groups = pd.qcut(df["Recency"].rank(method="first"), q=4, labels=r_labels)
        f_groups = pd.qcut(df["Frequency"].rank(method="first"), q=4, labels=f_labels)
        m_groups = pd.qcut(df["Monetary"].rank(method="first"), q=4, labels=m_labels)

        df = df.assign(R = r_groups.values, F = f_groups.values, M = m_groups.values)
        
        df["RFM_Level"] = df.apply(self.rfm_level, axis=1)
        df.to_csv("output_data/customer_rfm.csv", index=False)