import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

def train_test(dataset, train_feature, test_feature, away_or_home):
    # one-hot encode the data using pandas get_dummies
    features = pd.get_dummies(dataset)

    # labels are the values we want to predict
    train_labels = np.array(features.query(train_feature)[away_or_home])

    # remove labels from feature, axis 1 refers to the columns
    train_features = features.query(train_feature).drop(away_or_home, axis=1).drop('date', axis=1)
    # convert to numpy array
    train_features = np.array(train_features)

    # creating labels and features
    test_labels = np.array(features.query(test_feature)[away_or_home])
    test_features = features.query(test_feature).drop(away_or_home).drop('date', axis=1)
    test_features = np.array(test_features)

    # checking labels and features
    print('Training Features Shape:', train_features.shape)
    print('Training Labels Shape:', train_labels.shape)
    print('Testing Features Shape:', test_features.shape)
    print('Testing Labels Shape:', test_labels.shape)

    # instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)

    # train the model on training data
    rf.fit(train_features, train_labels)

    # use the forest's predict method on the test data
    predictions = rf.predict(test_features)

    # calculate the absolute errors
    errors = abs(predictions - test_labels)

    # print out the mean absolute error (mae)
    print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

    # checking how many gor right
    # merging test data and predicts data
    df_predict_test = pd.merge(pd.DataFrame(predictions.round(0)), pd.DataFrame(test_labels), left_index=True, right_index=True).rename(columns={'0_x' : 'predicts', '0_y' : 'reality'})
    df_predict_test['is_correct'] = df_predict_test['predicts'] - df_predict_test['reality']
    predict_right = ((df_predict_test['reality'].count() - df_predict_test.query('is_correct != 0')['is_correct'].count()) / df_predict_test['reality'].count() * 100).round(2)

    print(f"The algorithm predicted right: {predict_right}% of the values")