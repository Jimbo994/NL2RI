import numpy as np
import joblib
import catboost as cb
import pandas as pd

threshold_descript_to_ri =  0.13148925126827915
threshold_nl_to_ri = 1

def predict_ri_from_descriptor(data, model, leverage_matrix, features=None):
    """
    Predicts retention indices and leverage values based on descriptors data.
    Prints a warning if at least one of the leverage values exceeds the leverage threshold
    of the model.

    :param data: Indexable, length n_samples. Must fulfill the input assumptions of the model.
    :param model: Regression model
    :param leverage_matrix: pd.DataFrame of shape (n_features, n_features)
    :param features: Feature names of model, ndarray of shape (n_features,). Must fulfill the feature
    assumptions of model.

    :return:
    ri : ndarray of shape (n_samples,)
    leverages : ndarray of shape (n_samples,)

    """
    leverages = []
    if features == None:
        features = leverage_matrix.columns
    ri = model.predict(data[features])

    # compute leverage for each datapoint
    leverages = np.diag(data[features].values @ leverage_matrix.values @ data[features].values.T)
    if leverages.any() < threshold_descript_to_ri:
        print("Warning, some compounds have a high leverage value and predictions might be unreliable. Please check!")
    return ri, np.array(leverages)

def predict_ri_from_nl(data, model, leverage_matrix, features=None):
    """
    Predicts retention indices and leverage values based on neutral losses data.
    Prints a warning if at least one of the leverage values exceeds the leverage threshold
    of the model.

    :param data: Indexable, length n_samples. Must fulfill the input assumptions of the model.
    :param model: Regression model
    :param leverage_matrix: pd.DataFrame of shape (n_features, n_features)
    :param features: Feature names of model, ndarray of shape (n_features,). Must fulfill the feature
    assumptions of model.

    :return:
    ri : ndarray of shape (n_samples,)
    leverages : ndarray of shape (n_samples,)
    """
    if features == None:
        features = leverage_matrix.columns
    print(features)
    ri = model.predict(data[features])
    leverages = np.diag(data[features].values @ leverage_matrix.values @ data[features].values.T)
    if leverages.any() < threshold_nl_to_ri:
        print("Warning, some compounds have a high leverage value and predictions might be unreliable. Please check!")
    return ri, leverages