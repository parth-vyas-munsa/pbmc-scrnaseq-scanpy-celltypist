Complete Workflow

The complete workflow can be summarized as:

PBMC scRNA-seq Data
        │
        ▼
Quality Control
        │
        ▼
Filtering
        │
        ▼
Normalization
        │
        ▼
Highly Variable Genes
        │
        ▼
Scaling
        │
        ▼
PCA
        │
        ▼
Nearest Neighbors
        │
        ▼
UMAP
        │
        ▼
Leiden Clustering
        │
        ▼
Marker Gene Identification
        │
        ▼
Manual Cell-Type Annotation
        │
        ├───────────────┐
        ▼               ▼
   Marker-based     CellTypist
   annotation       annotation
        │               │
        └───────┬───────┘
                ▼
        Annotation Comparison
                │
                ▼
       Biological Interpretation

Technologies Used
Python
Scanpy
AnnData
CellTypist
Pandas
NumPy
Matplotlib
Seaborn
Jupyter / Google Colab

pbmc-scRNAseq-celltypist/
│
├── README.md
│
├── notebooks/
│   └── PBMC_Scanpy_CellTypist.ipynb
│
├── scripts/
│   ├── 01_qc.py
│   ├── 02_preprocessing.py
│   ├── 03_clustering.py
│   ├── 04_marker_analysis.py
│   ├── 05_celltypist.py
│   └── 06_compare_annotations.py
│
├── results/
│   ├── figures/
│   │   ├── qc_metrics.png
│   │   ├── umap.png
│   │   ├── leiden_umap.png
│   │   ├── manual_annotation_umap.png
│   │   ├── celltypist_umap.png
│   │   └── marker_dotplot.png
│   │
│   └── tables/
│       └── celltypist_vs_manual_annotation.csv
│
├── data/
│   └── README.md
│
├── requirements.txt
│
└── .gitignore


Key Learning Outcomes

Through this project, I developed practical experience in:

Processing single-cell RNA-seq data
Quality control of individual cells
Normalization and HVG selection
PCA-based dimensionality reduction
UMAP visualization
Leiden clustering
Marker gene identification
Manual cell-type annotation
Automated cell-type annotation using CellTypist
Comparing independent annotation approaches
Working with AnnData objects
Generating reproducible analysis results
Presenting scRNA-seq results using publication-style visualizations


