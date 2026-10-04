# pbmc-scrnaseq-scanpy-celltypist
End-to-end PBMC single-cell RNA-seq analysis using Scanpy, marker-based cell-type annotation, and CellTypist, with comparison of manual and automated annotations.
# PBMC scRNA-seq Analysis and Cell-Type Annotation

## Overview

This project demonstrates an end-to-end **single-cell RNA-seq (scRNA-seq)** analysis workflow using **Scanpy, AnnData, and CellTypist**.

The main objective is to identify cellular populations from PBMC scRNA-seq data, characterize clusters using marker genes, perform manual cell-type annotation, and compare the results with automated **CellTypist** predictions.

The project covers:

- Quality control
- Normalization
- Highly variable gene selection
- PCA
- Nearest-neighbor graph construction
- UMAP
- Leiden clustering
- Marker gene identification
- Manual cell-type annotation
- CellTypist automated annotation
- Manual vs CellTypist comparison
- Visualization and result export

---

# Analysis Workflow

```text
PBMC scRNA-seq Data
        |
        v
Quality Control
        |
        v
Filtering
        |
        v
Normalization
        |
        v
Highly Variable Genes
        |
        v
Scaling
        |
        v
PCA
        |
        v
Nearest Neighbors
        |
        v
UMAP
        |
        v
Leiden Clustering
        |
        v
Marker Gene Identification
        |
        +----------------------+
        |                      |
        v                      v
Manual Annotation        CellTypist Annotation
        |                      |
        +----------+-----------+
                   |
                   v
       Manual vs CellTypist
             Comparison
                   |
                   v
        Biological Interpretation
