# NL2RI
Predicting RP-LC retention indices of structurally unknown chemicals from mass spectrometry data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kjappelbaum/ml_molsim/blob/2022/molsim_ml.ipynb)
[![DOI](g/badge/DOI/10.5281/zenodo.3605363.svg)](https://doi.org/10.5281/zenodo.3605363)


(Example image)
%![](https://user-images.githubusercontent.com/333780/73550102-425bd180-4444-11ea-8b69-8a4241ffa9c9.gif)

## Installation

Use the package and environment management system  [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to install the conda environment necessary to run the code in this directory from the gpo_environment.yml file.

```bash
conda env create --file environment.yml
```

This will create a conda environment called **retention_indices** with the required packages installed for you.

## Example
```python

import joblib
import pandas as pd
from predict import *

# load model
model_descriptors_to_ri = joblib.load('models/descs_to_RI_40_model.sav')

# load leverage matrix to check for applicability domain
leverage_matrix = pd.read_csv('models/leverage_mat_train40', index_col=0)

# load some example data
data = pd.read_csv('dataset/small_norman.csv')

# predict retention indices and leverages
ri, leverages = predict_ri_from_descriptor(data, model_desc_to_RI, leverage_matrix)
```

Likewise, retention indices can be predicted from mass spectrometry data as follows:



## Installation

## Citing
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3723557.svg)](https://doi.org/10.5281/zenodo.3723557)

```
@software{e3nn_2020_3723557,
  author       = {Mario Geiger and
                  Tess Smidt and
                  Benjamin K. Miller and
                  Wouter Boomsma and
                  Kostiantyn Lapchevskyi and
                  Maurice Weiler and
                  Michał Tyszkiewicz and
                  Jes Frellsen},
  title        = {github.com/e3nn/e3nn},
  month        = mar,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v0.3-alpha},
  doi          = {10.5281/zenodo.3723557},
  url          = {https://doi.org/10.5281/zenodo.3723557}
}
```

