# ESS569_AI_data
Repository for ESS 569's final project data.
## Data Sources

Metagenome-assembled genomes (MAG) stored as FASTQ files. Data was retrieved from https://opendata.lifebit.ai/table/sgb
### MAGs and Identified Genera
1. Constructed MAGs in Pasolli et al.
   16S rRNA DNA sequences stored as FASTQ files.
Metagenome Assembled Genome (MAGs) stored as FA files. 
### DNA Sequences
1. Microbial DNA sequencing database
2. Identified genera in Zackular et al.
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
2. Custome HMM profiles 
3. Sulfide-producing genera and correlation with CRC in Wolf et al.
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
Apply Random Forest algorithms to MAGs constructed from human fecal samples in order to correlate sulfide-producing bacteria with patients diagnosed with Adenoma or Carcinoma.  

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
1. METabolic And BiogOchemistry anaLyses In miCrobes (METABOLIC) is a software that predicts metabolic and biogeochemical functional trait profiles to any given genome datasets (Zhou et al.) https://github.com/AnantharamanLab/METABOLIC
```
@article{Zhou2022,
  author = {Z. Zhou, P. Q. Tran, A. M. Breister, Y. Liu, K. Kieft, E. S. Cowley, U. Karaoz, and K. Anantharaman},
  title = {METABOLIC: high-throughput profiling of microbial genomes for functional traits, metabolism, biogeochemistry. and community-scale functional networks},
  journal = {Microbiome},
  volume = {10},
  number = {33},
  year = {2022},
  doi = {10.1186/s40168-021-01213-8}
}
```

