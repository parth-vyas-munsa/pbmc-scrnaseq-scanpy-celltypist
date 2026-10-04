sc.tl.umap(adata)
sc.pl.umap(adata) 

!pip install -q leidenalg

sc.tl.leiden(
    adata,
    resolution=0.5
)

sc.pl.umap(
    adata,
    color="leiden"
)

sc.tl.rank_genes_groups(
    adata,
    groupby="leiden",
    method="wilcoxon"
)

sc.pl.rank_genes_groups(
    adata,
    n_genes=10,
    sharey=False
)

adata
adata.obs["leiden"].value_counts()
sc.pl.umap(
    adata,
    color="leiden"
)
sc.pl.rank_genes_groups(
    adata,
    n_genes=10,
    sharey=False
)
print(adata)
print(adata.obs["leiden"].value_counts())
