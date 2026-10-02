import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv("house_prices.csv")
print(df.shape); print(df.isnull().sum()); print(df.describe(include="all"))

sns.histplot(df["Price"],kde=True); plt.title("Distribution of House Prices"); plt.show()
X=df[["Area_sqft","Location","Rooms","Age_years"]]; y=df["Price"]
numeric=["Area_sqft","Rooms","Age_years"]; categorical=["Location"]
prep=ColumnTransformer([
("num",SimpleImputer(strategy="median"),numeric),
("cat",Pipeline([("imp",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]),categorical)])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.20,random_state=42)
model=Pipeline([("preprocessor",prep),("regressor",LinearRegression())])
model.fit(Xtr,ytr); pred=model.predict(Xte)
mse=mean_squared_error(yte,pred); rmse=np.sqrt(mse); r2=r2_score(yte,pred)
print(f"MSE: {mse:,.2f}\nRMSE: {rmse:,.2f}\nR2: {r2:.4f}")

mn,mx=min(yte.min(),pred.min()),max(yte.max(),pred.max())
plt.scatter(yte,pred,alpha=.7); plt.plot([mn,mx],[mn,mx],linestyle="--"); plt.xlabel("Actual"); plt.ylabel("Predicted"); plt.title("Actual vs Predicted"); plt.show()
res=yte-pred
plt.scatter(pred,res,alpha=.7); plt.axhline(0,linestyle="--"); plt.xlabel("Predicted"); plt.ylabel("Residual"); plt.title("Residual Plot"); plt.show()

names=model.named_steps["preprocessor"].get_feature_names_out()
coef=pd.DataFrame({"Feature":names,"Coefficient":model.named_steps["regressor"].coef_})
print(coef.sort_values("Coefficient",ascending=False).head(5))
print(coef.sort_values("Coefficient").head(5))

ridge=Pipeline([("preprocessor",prep),("regressor",Ridge(alpha=1.0))])
ridge.fit(Xtr,ytr); print("Ridge R2:",r2_score(yte,ridge.predict(Xte)))
