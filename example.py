
import joblib
import pandas as pd
from predict import *


model_desc_to_RI = joblib.load('models/descs_to_RI_40_model.sav')
leverage_matrix = pd.read_csv('models/leverage_mat_train40', index_col=0)

data = pd.read_csv('dataset/small_norman.csv')

ri, leverages = predict_ri_from_descriptor(data, model_desc_to_RI, leverage_matrix)

print(ri)
print(leverages)