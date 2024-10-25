# ESS569_AI_data
Repository for ESS 569's final project data.
## Data Sources
16S rRNA DNA sequences stored as FASTQ files.
Metagenome Assembled Genome (MAGs) stored as FA files. 
### DNA Sequences
1. Microbial DNA sequencing database
2. Identified genera in Zuckular et al.
```
@article{Zackular2014,
  author = {J. P. Zackular and M. A. M. Rogers and M. T. Ruffin and P. D. Schloss},
  title = {The Human Gut Microbiome as a Screening Tool for Colorectal Cancer},
  journal = {Cancer Prevention Research (Philadelphia, Pa.)},
  volume = {7},
  number = {11},
  pages = {1112--1121},
  year = {2014},
  doi = {10.1158/1940-6207.CAPR-14-0129}
}
```
4. Sulfide-producing general in Wolf et al.
```
@article{Wolf2022,
  author = {P. G. Wolf and E. S. Cowley and A. Breister and S. Matatov and L. Lucio and P. Polak and J. M. Ridlon and H. R. Gaskins and K. Anantharaman},
  title = {Diversity and distribution of sulfur metabolic genes in the human gut microbiome and their association with colorectal cancer},
  journal = {Microbiome},
  volume = {10},
  number = {1},
  pages = {64},
  year = {2022},
  doi = {10.1186/s40168-022-01242-x}
}
```

## Project Objectives
Apply Random Forest algorithms to microbial OTUs found in fecal samples in order to correlate sulfide-producing bacteria with patients diagnosed with Adenoma or Carcinoma.  

## Environment Packages
```
# For random forest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# For RDP classifier
import subprocess
# Import QIIME2 library for 16S analysis
import qiime2
from qiime2.plugins import demux, dada2, feature_table, taxa, phylogeny, diversity
```
## Script Descriptions
Not yet available as of 10/24/24.
