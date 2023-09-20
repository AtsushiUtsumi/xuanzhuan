# %% [markdown]
# # 第8章 分類モデルの評価を行う10本

# %% [markdown]
# ## ノック71:評価対象のモデルを用意しよう

# %%
from sklearn.datasets import load_breast_cancer

load_data = load_breast_cancer()

import pandas as pd

df = pd.DataFrame(load_data.data, columns = load_data.feature_names)
df["y"] = load_data.target

# %%
from sklearn.model_selection import train_test_split

X= df[["mean radius","mean texture"]]
y = df["y"]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=0)

print(len(X_test))

# %%
from sklearn.ensemble import RandomForestClassifier

rf_cls = RandomForestClassifier(max_depth=3,random_state=0).fit(X_train, y_train)

y_train_pred = rf_cls.predict(X_train)
y_test_pred = rf_cls.predict(X_test)

# %% [markdown]
# ## ノック72:正解率を算出しよう

# %%
from sklearn.metrics import accuracy_score

print(f"訓練データ正解率：{accuracy_score(y_train,y_train_pred)}")
print(f"テストデータ正解率：{accuracy_score(y_test,y_test_pred)}")

# %% [markdown]
# ## ノック73:混同行列を見てみよう

# %%
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

matrix = confusion_matrix(y_test,y_test_pred)

sns.heatmap(matrix.T, square=True,annot=True)
plt.xlabel("True Label")
plt.ylabel("Pred Label")
plt.show()

# %% [markdown]
# ## ノック74:	適合率を算出しよう

# %%
from sklearn.metrics import precision_score

print(f"訓練データ適合率：{precision_score(y_train,y_train_pred,pos_label=0)}")
print(f"テストデータ適合率：{precision_score(y_test,y_test_pred,pos_label=0)}")

# %% [markdown]
# ## ノック75:再現率を算出しよう

# %%
from sklearn.metrics import recall_score

print(f"訓練データ再現率：{recall_score(y_train,y_train_pred,pos_label=0)}")
print(f"テストデータ再現率：{recall_score(y_test,y_test_pred,pos_label=0)}")

# %% [markdown]
# ## ノック76:F1値を算出しよう

# %%
from sklearn.metrics import f1_score

print(f"訓練データF1値：{f1_score(y_train,y_train_pred,pos_label=0)}")
print(f"テストデータF1値：{f1_score(y_test,y_test_pred,pos_label=0)}")

# %% [markdown]
# ## ノック77:分類レポートを見てみよう

# %%
from sklearn.metrics import classification_report

print("Train Score Report")
print(classification_report(y_train,y_train_pred))
print("Test Score Report")
print(classification_report(y_test,y_test_pred))

# %% [markdown]
# ## ノック78:予測結果の確信度を算出しよう

# %%
pred_proba_train = rf_cls.predict_proba(X_train)
pred_proba_test = rf_cls.predict_proba(X_test)

print(pred_proba_train[:5])
print(pred_proba_test[:5])

# %%
import numpy as np

x_min, x_max = X["mean radius"].min() - 0.5, X["mean radius"].max() + 0.5
y_min, y_max = X["mean texture"].min() - 0.5, X["mean texture"].max() + 0.5

step = 0.5
x_range = np.arange(x_min, x_max, step)
y_range = np.arange(y_min, y_max, step)
xx, yy = np.meshgrid(x_range, y_range)

Z = rf_cls.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 0]
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10,7))
plt.contourf(xx, yy, Z, alpha=0.8,cmap=plt.cm.coolwarm)
plt.colorbar()
plt.scatter(X_train["mean radius"], X_train["mean texture"], c=y_train,marker="o", edgecolors="k", cmap=plt.cm.coolwarm_r, label="Train")
plt.scatter(X_test["mean radius"], X_test["mean texture"], c=y_test, marker="^",edgecolors="k", cmap=plt.cm.coolwarm_r, label="Test")
plt.xlabel("mean radius")
plt.ylabel("mean texture")
plt.legend()
plt.show()

# %% [markdown]
# ## ノック79:PR曲線を見てみよう

# %%
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc

precision, recall, thresholds = precision_recall_curve(y_test,pred_proba_test[:,0], pos_label=0)

print(precision[:3])
print(recall[:3])
print(thresholds[:3])

# %%
plt.plot(recall, precision,label="PR Curve")

tg_thres = [0.3,0.5,0.8]
for thres in tg_thres:
  tg_index = np.argmin(np.abs(thresholds - thres))
  plt.plot(recall[tg_index], precision[tg_index], marker = "o",markersize=10, label=f"Threshold = {thres}")

plt.plot([0,1], [1,1], linestyle="--", color="red", label="Ideal Line")

plt.legend()
plt.title("PR curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.grid()
plt.show()

# %%
from sklearn.metrics import auc

auc(recall, precision)

# %%
plt.plot(np.append(thresholds, 1), recall, label = "Recall")
plt.plot(np.append(thresholds, 1), precision, label = "Precision")
plt.xlabel("Thresholds")
plt.ylabel("Score")
plt.grid()
plt.legend()
plt.show()

# %%
def plot_pr_curve(y_true,proba):
  precision, recall, thresholds = precision_recall_curve(y_true, proba[:,0], pos_label=0)
  auc_score = auc(recall, precision)

  plt.figure(figsize=(12, 4))
  plt.subplot(1,2,1)

  plt.plot(recall, precision,label=f"PR Curve (AUC = {round(auc_score,3)})")
  plt.plot([0,1], [1,1], linestyle="--", color="red", label="Ideal Line")

  tg_thres = [0.3,0.5,0.8]
  for thres in tg_thres:
    tg_index = np.argmin(np.abs(thresholds - thres))
    plt.plot(recall[tg_index], precision[tg_index], marker = "o",markersize=10, label=f"Threshold = {thres}")

  plt.legend()
  plt.title("PR curve")
  plt.xlabel("Recall")
  plt.ylabel("Precision")
  plt.grid()

  plt.subplot(1,2,2)

  plt.plot(np.append(thresholds, 1), recall, label = "Recall")
  plt.plot(np.append(thresholds, 1), precision, label = "Precision")
  plt.xlabel("Thresholds")
  plt.ylabel("Score")
  plt.grid()
  plt.legend()

  plt.show()

# %% [markdown]
# ## ノック80:各モデルの評価結果を見てみよう

# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

models = {"Logistic Regression":LogisticRegression(), 
          "Linear SVM":SVC(kernel="linear",probability=True,random_state=0),
          "Kernel SVM":SVC(kernel="rbf",probability=True,random_state=0),
          "K Neighbors":KNeighborsClassifier(),
          "Decision Tree":DecisionTreeClassifier(max_depth=3,random_state=0),
          "Random Forest":RandomForestClassifier(max_depth=3,random_state=0)}

# %%
data_set = {"Train":[X_train_scaled,y_train],"Test":[X_test_scaled,y_test]}

# %%
for model_name in models.keys():

  print(f"{model_name} Score Report")
  model = models[model_name].fit(X_train_scaled,y_train)

  for data_set_name in data_set.keys():

    X_data = data_set[data_set_name][0]
    y_true = data_set[data_set_name][1]

    y_pred = model.predict(X_data)

    score_df = pd.DataFrame(classification_report(y_true,y_pred,output_dict=True))
    score_df["model"] = model_name
    score_df["type"] = data_set_name
    print(score_df)

    if data_set_name == "Test":
      proba = model.predict_proba(X_data)
      plot_pr_curve(y_true,proba)

def show():
	print('8章importしました')
	return