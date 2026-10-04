!pip install -q celltypist

import celltypist
print(celltypist.__version__)

celltypist.models.download_models()


celltypist.models.models_description()

adata_full = sc.datasets.pbmc3k()

adata_full.var["mt"] = adata_full.var_names.str.startswith("MT-")

sc.pp.calculate_qc_metrics(
    adata_full,
    qc_vars=["mt"],
    inplace=True
)

adata_full = adata_full[
    (adata_full.obs.n_genes_by_counts > 200) &
    (adata_full.obs.pct_counts_mt < 10),
    :
].copy()

sc.pp.normalize_total(adata_full, target_sum=1e4)
sc.pp.log1p(adata_full)

import celltypist
from celltypist import models

predictions = celltypist.annotate(
    adata_full,
    model="Immune_All_Low.pkl",
    majority_voting=True
)

predictions.predicted_labels.head()

adata_full.obs["celltypist_label"] = predictions.predicted_labels["majority_voting"]

sc.tl.umap(adata_full)

sc.pl.umap(
    adata_full,
    color="celltypist_label",
    legend_loc="on data",
    frameon=False
)

sc.tl.umap(adata)
