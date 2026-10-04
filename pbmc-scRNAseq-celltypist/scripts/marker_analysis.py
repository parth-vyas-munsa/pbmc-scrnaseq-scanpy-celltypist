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

print(adata)
print(adata.obs["leiden"].value_counts())

markers = sc.get.rank_genes_groups_df(
    adata,
    group=None
)

markers.head(20)

markers.groupby("group").head(10)

for cluster in adata.obs["leiden"].cat.categories:
    print("\nCLUSTER:", cluster)
    print(
        markers[markers["group"] == cluster][
            ["names", "scores", "logfoldchanges", "pvals_adj"]
        ].head(10)
    )

cell_type_map = {
    "0": "T cells",
    "1": "Classical monocytes",
    "2": "B cells",
    "3": "GZMK+ cytotoxic T cells",
    "4": "FCGR3A+ monocytes",
    "5": "NK cells",
    "6": "Dendritic cells"
}
adata.obs["cell_type"] = adata.obs["leiden"].map(cell_type_map)
adata.obs[["leiden", "cell_type"]].head()

adata.obs["cell_type"].value_counts()

sc.pl.umap(
    adata,
    color="cell_type",
    legend_loc="on data",
    frameon=False
)

print(adata)
print(adata.X.shape)
print(adata.var_names[:10])

adata.obs["cell_type"].value_counts()

adata.obs["cell_type"].value_counts().plot.bar()

import matplotlib.pyplot as plt
plt.ylabel("Number of cells")
plt.xlabel("Cell type")
plt.title("Cell-type composition")
plt.xticks(rotation=90)
plt.show()

markers = [
    "CD3D",
    "CD3E",
    "MS4A1",
    "CD79A",
    "NKG7",
    "GNLY",
    "LYZ",
    "S100A8",
    "S100A9",
    "FCGR3A",
    "FCER1A"
]

available_markers = [
    gene for gene in markers
    if gene in adata.var_names
]

print(available_markers)

sc.pl.umap(
    adata,
    color=available_markers
)

sc.tl.rank_genes_groups(
    adata,
    groupby="cell_type",
    method="wilcoxon"
)

sc.pl.rank_genes_groups(
    adata,
    n_genes=10,
    sharey=False
)

de_results = sc.get.rank_genes_groups_df(
    adata,
    group=None
)

de_results.head()

de_results.to_csv(
    "cell_type_marker_genes.csv",
    index=False
)

for cell_type in adata.obs["cell_type"].unique():

    print("\nCELL TYPE:", cell_type)

    result = de_results[
        de_results["group"] == cell_type
    ]

    print(
        result[
            ["names", "scores", "pvals_adj"]
        ].head(10)
    )



adata.write_h5ad(
    "PBMC3k_annotated.h5ad"
)
