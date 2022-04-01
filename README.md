# NL2RI
Predicting RP-LC retention indices of structurally unknown chemicals from mass spectrometry data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VyBBgJAV9K8taOBNxEUL5l-LeU7_1lj9?usp=sharing)
[![DOI](g/badge/DOI/10.5281/zenodo.3605363.svg)](TODO)


(Placeholder image)
<img src="/images/descripts_to_RI-correlation_plots_with_dist_train.pdf" width="425"/> <img src="/images/descripts_to_RI-correlation_plots_with_dist_test.pdf" width="425"/> 


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

```python

import joblib
import pandas as pd
from predict import *

# Load model
model_desc_to_RI = joblib.load('models/nl_to_ri_4220_model.sav')
leverage_matrix = pd.read_csv('models/leverage_mat_train_NL_100k_4220feats.csv', index_col=0)

# Load data
data_nl = pd.read_csv('dataset/small_amide_nls.csv', index_col=0)

# Predict retention indices and leverages
ri, leverages = predict_ri_from_descriptor(data_nl, model_desc_to_RI, leverage_matrix)
```
In order to get going and start predicting retention indices from mass spectrometry data yourself, all that is left to do is to convert your mass spectra into neutral losses. 

```python

# Example parent mass and fragment masses
# Note: all masses should be rounded to two digits
parent_mass = 456.75
fragments = np.array([151.21, 18.83, 25.80, 441.75, parent_mass])

# Borrow columns from other dataset
cols = data_nl.columns[6:]
neutral_loss = parent_mass - fragments

# initiate vector with zeroes
nl_vec = np.zeros(len(cols))

parent_mass_indice = parent_mass * 100
neutral_loss_indices = neutral_loss * 100

# everything higher than isomass, should be set to -1
nl_vec[int(parent_mass_indice):] = -1

# where there is a fragment, place 1.
nl_vec[neutral_loss_indices.astype(int)] = 1

# Add some more info (MONOISOMASS is required)
df_test['NAME'] = 'example_molecule'
df_test['RI'] = 42
df_test['MONOISOMASS'] = parent_mass

# Write to DataFrama
df_test = pd.DataFrame(nl_vec, index=cols).T

```



## Citing
TODO
[![DOI](Not there yet)


