adata.var["mt"] = adata.var_names.str.startswith("MT-")

sc.pp.calculate_qc_metrics(
    adata,
    qc_vars=["mt"],
    inplace=True
)

adata.obs[
    ["n_genes_by_counts",
     "total_counts",
     "pct_counts_mt"]
].head()

sc.pl.violin(
    adata,
    ["n_genes_by_counts",
     "total_counts",
     "pct_counts_mt"],
    jitter=0.4,
    multi_panel=True
)

adata = adata[
    adata.obs.n_genes_by_counts > 200,
    :
].copy()

adata = adata[
    adata.obs.pct_counts_mt < 10,
    :
].copy()

print(adata)

sc.pl.scatter(
    adata,
    x="n_genes_by_counts",
    y="pct_counts_mt"
)
