sc.pp.normalize_total(
    adata,
    target_sum=1e4
)

sc.pp.log1p(adata)

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    flavor="seurat"
)

adata.var["highly_variable"].sum()

sc.pl.highly_variable_genes(adata)

adata = adata[
    :,
    adata.var.highly_variable
].copy()
print(adata)

sc.pp.scale(
    adata,
    max_value=10
)

sc.tl.pca(
    adata,
    n_comps=30
)

sc.pl.pca_variance_ratio(
    adata,
    log=True
)

print(adata.uns["pca"]["variance_ratio"][:30])

sc.pp.neighbors(
    adata,
    n_neighbors=10,
    n_pcs=20
)
