!python --version
!pip install -q scanpy anndata pandas numpy matplotlib seaborn scikit-learn
import scanpy as sc
import anndata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Scanpy:", sc.__version__)
print("AnnData:", anndata.__version__)

adata = sc.datasets.pbmc3k()
adata

adata.n_obs

print("Cells:", adata.n_obs)
print("Genes:", adata.n_vars)

adata.X.shape

adata.var_names[:20]

adata.obs.columns
adata.obs.head()
