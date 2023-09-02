# 第3章　代表的な次元削減を行う10本ノック
# 意味はよくわからないがこれでパフォーマンスが上がるならみておくといいかも

# ノック21:PCAを実施してみよう

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df.loc[df["target"]==0, "target_name"] = "setosa"
df.loc[df["target"]==1, "target_name"] = "versicolor"
df.loc[df["target"]==2, "target_name"] = "virginica"
df.head()

# %%
import seaborn as sns
sns.pairplot(df, vars=df.columns[:4], hue="target_name")

# %%
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1, projection="3d")
for c in df["target_name"].unique():
    ax.scatter(df.iloc[:, 0][df["target_name"]==c], df.iloc[:, 1][df["target_name"]==c] , df.iloc[:, 2][df["target_name"]==c], label=c)
ax.set_title("iris 3D") 
ax.set_xlabel("sepal_length") 
ax.set_ylabel("sepal_width")  
ax.set_zlabel("petal_length") 
ax.legend(loc=2, title="legend", shadow=True)  
plt.show()

# %%
from sklearn.decomposition import PCA
import numpy as np
pca = PCA(random_state=0)
X_pc = pca.fit_transform(df.iloc[:, 0:4])
df_pca = pd.DataFrame(X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])
print("主成分の数: ", pca.n_components_) 
print("保たれている情報: ", np.sum(pca.explained_variance_ratio_))
print(df_pca.head())

# %%
sns.scatterplot(x="PC1", y="PC2", data=df_pca, hue=df["target_name"])

# %% [markdown]
# ## ノック22:主成分を解釈してみよう

# %%
import seaborn as sns
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
sns.heatmap(pca.components_,
           cmap="Blues",
           annot=True,
           annot_kws={"size": 14},
           fmt=".2f",
           xticklabels=["SepalLength", "SepalWidth", "PetalLength", "PetalLength"],
           yticklabels=["PC1", "PC2", "PC3", "PC4"],
           ax=ax)
plt.show()

# %% [markdown]
# ## ノック23:スクリープロットで次元削減数を探索してみよう

# %%
df_wine=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df_wine.columns = ["class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash","Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols","Proanthocyanins", "Color intensity", "Hue","OD280/OD315 of diluted wines", "Proline"]
print(df_wine.shape)
print(df_wine.head())

# %%
from pandas import plotting
plotting.scatter_matrix(df_wine.iloc[:, 1:], figsize=(8, 8), c=list(df_wine.iloc[:, 0]), alpha=0.5)
plt.show()

# %%
from sklearn.decomposition import PCA
from sklearn import preprocessing
import numpy as np
sc=preprocessing.StandardScaler()
X = df_wine.iloc[:, 1:]
X_norm=sc.fit_transform(X)
 
pca = PCA(random_state=0)
X_pc = pca.fit_transform(X_norm)
df_pca = pd.DataFrame(X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])
print("主成分の数: ", pca.n_components_)
print("保たれている情報: ", round(np.sum(pca.explained_variance_ratio_),2))
print(df_pca.head())

# %%
pd.DataFrame(np.round(pca.explained_variance_, 2), index=["PC{}".format(x + 1) for x in range(len(df_pca.columns))], columns=["固有値"])

# %%
line = np.ones(14)
plt.plot(np.append(np.nan, pca.explained_variance_), "s-")
plt.plot(line, "s-")
plt.xlabel("PC")
plt.ylabel("explained_variance")
plt.xticks( np.arange(1, 14, 1))
plt.grid()
plt.show()

# %% [markdown]
# ## ノック24:寄与率で次元削減数を探索してみよう

# %%
pd.DataFrame(np.round(pca.explained_variance_ratio_,2), index=["PC{}".format(x + 1) for x in range(len(df_pca.columns))], columns=["寄与率"])

# %%
import matplotlib.ticker as ticker
line = np.full(14, 0.9)
plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
plt.plot([0] + list( np.cumsum(pca.explained_variance_ratio_)), "-o")
plt.xlabel("PC")
plt.ylabel("cumulative contribution rate")
plt.yticks( np.arange(0, 1.1, 0.1))
plt.plot(line, "s-") 
plt.grid()
plt.show()

# %%
sc=preprocessing.StandardScaler()
X = df_wine.iloc[:, 1:]
X_norm=sc.fit_transform(X)
 
pca = PCA(n_components=0.9, random_state=0)
X_pc = pca.fit_transform(X_norm)
df_pca = pd.DataFrame(X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])
print("主成分の数: ", pca.n_components_) 
print("保たれている情報: ", round(np.sum(pca.explained_variance_ratio_),2))
print(df_pca.head())

# %% [markdown]
# ## ノック25:Isomapで次元削減を実施してみよう

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, decomposition, manifold 
from sklearn import datasets
from sklearn.decomposition import PCA
X,Y = datasets.make_moons(n_samples=200, noise=0.05, random_state=0)
sc=preprocessing.StandardScaler()
sc.fit(X)
X_norm=sc.transform(X)
plt.figure(figsize=(10,3))
plt.scatter(X[:,0],X[:,1], c=Y)
plt.xlabel("x")
plt.ylabel("y")

# %%
pca = PCA(n_components=2)
X_reduced=pca.fit_transform(X_norm)
 
isomap_5 = manifold.Isomap(n_neighbors=5, n_components=2)
X_isomap_5 = isomap_5.fit_transform(X_norm)
 
isomap_10 = manifold.Isomap(n_neighbors=10, n_components=2)
X_isomap_10 = isomap_10.fit_transform(X_norm)

# %%
plt.figure(figsize=(10,6))
plt.subplot(3, 1, 1)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=Y)
plt.xlabel("pca-1")
plt.ylabel("pca-2")
 
plt.subplot(3, 1, 2)
plt.scatter(X_isomap_5[:,0],X_isomap_5[:,1], c=Y)
plt.xlabel("isomap_n5-1")
plt.ylabel("isomap_n5-2")
 
plt.subplot(3, 1, 3)
plt.scatter(X_isomap_10[:,0],X_isomap_10[:,1], c=Y)
plt.xlabel("isomap_n10-1")
plt.ylabel("isomap_n10-2")
plt.show

# %% [markdown]
# ## ノック26:t-SNEで次元削減を実施してみよう

# %%
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)
print(digits.data)

# %%
import matplotlib.pyplot as plt 
fig, axes = plt.subplots(10, 10, figsize=(8, 8),subplot_kw={"xticks":[], "yticks":[]})
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="binary", interpolation="nearest")
    ax.text(0, 0, str(digits.target[i]))

# %%
from sklearn.decomposition import PCA
X_reduced = PCA(n_components=2).fit_transform(digits.data)
for each_label in digits.target_names:
    c_plot_bool = digits.target == each_label
    plt.scatter(X_reduced[c_plot_bool, 0], X_reduced[c_plot_bool, 1], label="{}".format(each_label))
    plt.legend()
plt.show()

# %%
from sklearn.manifold import TSNE
X_reduced = TSNE(n_components=2, random_state=0).fit_transform(digits.data)
for each_label in digits.target_names:
    c_plot_bool = digits.target == each_label
    plt.scatter(X_reduced[c_plot_bool, 0], X_reduced[c_plot_bool, 1], label="{}".format(each_label))
    plt.legend()
plt.show()

# %% [markdown]
# ## ノック27:t-SNEで最適なPerplexityを探索してみよう

# %%
import time
def create_2d_tsne(target_X, y, y_labels, perplexity_list= [2, 5, 30, 50, 100]):
    fig, axes = plt.subplots(nrows=1, ncols=len(perplexity_list),figsize=(5*len(perplexity_list), 4))
    for i, (ax, perplexity) in enumerate(zip(axes.flatten(), perplexity_list)):
        start_time = time.time()
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
        Y = tsne.fit_transform(target_X)
        for each_label in y_labels:
            c_plot_bool = y == each_label
            ax.scatter(Y[c_plot_bool, 0], Y[c_plot_bool, 1], label="{}".format(each_label))
        end_time = time.time()
        ax.legend()
        ax.set_title("perplexity: {}".format(perplexity))
        print("perplexity {} is {:.2f} seconds.".format(perplexity, end_time - start_time))
    plt.show()

# %%
create_2d_tsne(digits.data, digits.target, digits.target_names)

# %%
def create_3d_tsne(target_X, y, y_labels, perplexity_list= [2, 5, 30, 50, 100]):
    fig = plt.figure(figsize=(5*len(perplexity_list),4))
    for i, perplexity in enumerate(perplexity_list):
        ax = fig.add_subplot(1, len(perplexity_list), i+1, projection="3d")
        start_time = time.time()
        tsne = TSNE(n_components=3, random_state=0, perplexity=perplexity)
        Y = tsne.fit_transform(target_X)
        for each_label in y_labels:
            c_plot_bool = y == each_label
            ax.scatter(Y[c_plot_bool, 0], Y[c_plot_bool, 1], label="{}".format(each_label))
        end_time = time.time()
        ax.legend()
        ax.set_title("Perplexity: {}".format(perplexity))
        print("perplexity {} is {:.2f} seconds.".format(perplexity, end_time - start_time))
    plt.show()

# %%
create_3d_tsne(digits.data, digits.target, digits.target_names)

# %% [markdown]
# ## ノック28:UMAPで次元削減を実施してみよう


# %%
import umap
 
start_time_tsne = time.time()
X_reduced = TSNE(n_components=2, random_state=0).fit_transform(digits.data)
interval_tsne = time.time() - start_time_tsne
 
start_time_umap = time.time()
embedding = umap.UMAP(n_components=2, random_state=0).fit_transform(digits.data)
interval_umap = time.time() - start_time_umap
 
print("tsne : {}s".format(np.round(interval_tsne,2)))
print("umap : {}s".format(np.round(interval_umap,2)))

# %%
plt.figure(figsize=(10,8))
plt.subplot(2, 1, 1)
for each_label in digits.target_names:
    c_plot_bool = digits.target == each_label
    plt.scatter(X_reduced[c_plot_bool, 0], X_reduced[c_plot_bool, 1], label="{}".format(each_label))
plt.legend(loc="upper right")
plt.xlabel("tsne-1")
plt.ylabel("tsne-2")
 
plt.subplot(2, 1, 2)
for each_label in digits.target_names:
    c_plot_bool = digits.target == each_label
    plt.scatter(embedding[c_plot_bool, 0], embedding[c_plot_bool, 1], label="{}".format(each_label))
plt.legend(loc="upper right")
plt.xlabel("umap-1")
plt.ylabel("umap-2")
plt.show()

# %% [markdown]
# ## ノック29:UMAPで最適なn_neighborsを探索してみよう

# %%
def create_2d_umap(target_X, y, y_labels, n_neighbors_list= [2, 15, 30, 50, 100]):
    fig, axes = plt.subplots(nrows=1, ncols=len(n_neighbors_list),figsize=(5*len(n_neighbors_list), 4))
    for i, (ax, n_neighbors) in enumerate(zip(axes.flatten(), n_neighbors_list)):
        start_time = time.time()
        mapper = umap.UMAP(n_components=2, random_state=0, n_neighbors=n_neighbors)
        Y = mapper.fit_transform(target_X)
        for each_label in y_labels:
            c_plot_bool = y == each_label
            ax.scatter(Y[c_plot_bool, 0], Y[c_plot_bool, 1], label="{}".format(each_label))
        end_time = time.time()
        ax.legend(loc="upper right")
        ax.set_title("n_neighbors: {}".format(n_neighbors))
        print("n_neighbors {} is {:.2f} seconds.".format(n_neighbors, end_time - start_time))
    plt.show()

# %%
create_2d_umap(digits.data, digits.target, digits.target_names)

# %%
def create_3d_umap(target_X, y, y_labels, n_neighbors_list= [2, 15, 30, 50, 100]):
    fig = plt.figure(figsize=(5*len(n_neighbors_list),4))
    for i, n_neighbors in enumerate(n_neighbors_list):
        ax = fig.add_subplot(1, len(n_neighbors_list), i+1, projection="3d")
        start_time = time.time()
        mapper = umap.UMAP(n_components=3, random_state=0, n_neighbors=n_neighbors)
        Y = mapper.fit_transform(target_X)
        for each_label in y_labels:
            c_plot_bool = y == each_label
            ax.scatter(Y[c_plot_bool, 0], Y[c_plot_bool, 1], label="{}".format(each_label))
        end_time = time.time()
        ax.legend(loc="upper right")
        ax.set_title("n_neighbors_list: {}".format(n_neighbors))
        print("n_neighbors_list {} is {:.2f} seconds.".format(n_neighbors, end_time - start_time))
    plt.show()

# %%
create_3d_umap(digits.data, digits.target, digits.target_names)

# %%
create_3d_umap(digits.data, digits.target, digits.target_names, [10 , 15, 20, 25, 30])

# %% [markdown]
# ## ノック30:PCAとUMAPを組み合わせて次元削減を実施してみよう

# %%
pca = PCA(n_components=0.99, random_state=0)
X_pc = pca.fit_transform(digits.data)
df_pca = pd.DataFrame(X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])
print("主成分の数: ", pca.n_components_) 
print("保たれている情報: ", np.sum(pca.explained_variance_ratio_))
print(df_pca.head())

# %%
create_2d_umap(digits.data, digits.target, digits.target_names, [5,10,15])
create_2d_umap(df_pca, digits.target, digits.target_names, [5,10,15])


