# **README: Trophism Classification by Machine Learning and Deep Learning**

This project involves clustering analysis, AutoML for model selection, training engineering, model assessment, and computational time analysis for a classification task.

---

## **Dependencies**
To ensure smooth execution of the project, install the following dependencies:

### **Python Version**
- Python >= 3.12.6

### **Libraries**
- **Data Manipulation and Analysis**:
  - `pandas` >= 1.3
  - `numpy` >= 1.21
- **Visualization**:
  - `matplotlib` >= 3.4
  - `seaborn` >= 0.11
- **Machine Learning**:
  - `scikit-learn` >= 0.24
  - `h2o` >= 3.38
- **Deep Learning**:
  - `torch` >= 1.10
  - `tensorflow` >= 2.6
- **Clustering Analysis**:
  - `scikit-learn` (included above)
- **Bioinformatics**:
  - `biopython` >= 1.79
- **Natural Language Processing**:
  - `transformers` >= 4.12
- **Utilities**:
  - `tqdm` >= 4.62

### **To install these dependencies, you can use the following command**
```bash
pip install -r requirements.txt
```

## **Installation Instructions**
### 1. Set Up Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv myenv
source myenv/bin/activate  # For Linux/Mac
myenv\Scripts\activate     # For Windows
```

## **Repository Structure**
- data/
  - ai_ready/                      # Preprocessed datasets ready for analysis.
- notebooks/
  - Clustering_Analysis.ipynb          # Clustering analysis and visualization.
  - AutoML_Hyperparameter_Tuning.ipynb # AutoML and hyperparameter optimization.
  - Model_Training_Assessment.ipynb    # Training strategies and model performance.
  - Computational_Time_Analysis.ipynb  # Computational time evaluation.
- Research_Relevance.md           # Relevance and context of the research.
- requirements.txt                # List of dependencies for the project.
- README.md                       # This file.

