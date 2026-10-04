sc.pl.umap(
    adata,
    color="cell_type",
    legend_loc="on data",
    frameon=False
)

comparison = pd.crosstab(
    adata.obs["cell_type"],
    adata_full.obs["celltypist_label"]
)

comparison


common_cells = adata.obs_names.intersection(adata_full.obs_names)

comparison = pd.crosstab(
    adata.obs.loc[common_cells, "cell_type"],
    adata_full.obs.loc[common_cells, "celltypist_label"]
)

comparison

comparison = pd.crosstab(
    adata.obs["cell_type"],
    adata_full.obs["celltypist_label"]
)
comparison.to_csv("celltypist_vs_manual_annotation.csv")
