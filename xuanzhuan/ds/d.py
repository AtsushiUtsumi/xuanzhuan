# %%
from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
print("説明変数")
print(f"{len(california.data)}件")
print(california.data[:5])
print("目的変数")
print(f"{len(california.target)}件")
print(california.target[:5])
print("変数名")
print(f"{len(california.feature_names)}件")
print(california.feature_names)


# %%
import pandas as pd

df = pd.DataFrame(california.data, columns=california.feature_names)
df["MEDV"] = california.target
#print(df.head())
print('以下、説明を取得して表示')
print(df.describe())

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 5))
for i, col in enumerate(df.columns):
    plt.subplot(2, 7, i + 1)
    plt.hist(df[col])
    plt.title(col)
plt.tight_layout()
#plt.show()
df_corr = df.corr()
print(df_corr)
import seaborn as sns

plt.figure(figsize=(15, 10))
sns.heatmap(df_corr, annot=True)
plt.title("Corr Heatmap")
#plt.show()
