import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

def run_predict(teams_to_query, features_df, labels_df):
    teams_to_query = labels_df[f'{teams_to_query}']

    # one-hot encode the data using pandas get_dummies
    features = pd.get_dummies(
        features_df.query('home_team in @teams_to_query & away_team in @teams_to_query'
        )[['date', 'home_team', 'away_team', 'home_score', 'away_score',
           'games', 'home_wins', 'home_looses', 'draws', 'home_rank',
           'home_ranking_points', 'away_rank', 'away_ranking_points']]
    )

    features_to_predict = pd.get_dummies(
        labels_df[['date', 'home_team', 'away_team', 'home_score', 'away_score',
                   'games', 'home_wins', 'home_looses', 'draws', 'home_rank',
                   'home_ranking_points', 'away_rank', 'away_ranking_points']]
    )

    # labels are the values we want to predict
    train_labels = np.array(features['away_score'])

    # remove the labels from the features, axis 1 refers to the columns
    train_features = features.drop('away_score', axis = 1).drop('date', axis = 1)
    # convert to numpy array
    train_features = np.array(train_features)

    test_labels = np.array(features_to_predict['away_score'])
    test_features = features_to_predict.drop('away_score', axis = 1).drop('date', axis = 1)
    test_features = np.array(test_features)

    # instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

    # train the model on training data
    rf.fit(train_features, train_labels)

    # use the forest's predict method on the test data
    predictions = rf.predict(test_features)