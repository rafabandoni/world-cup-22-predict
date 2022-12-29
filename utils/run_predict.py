import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

def run_predict_home(df_to_predict, historical_results_world_cup):
# one-hot encode the data using pandas get_dummies
    features = pd.get_dummies(
        pd.concat([historical_results_world_cup,df_to_predict]).reset_index(drop=True)
        [['date', 'home_team', 'away_team', 'home_score', 'away_score',
           'games', 'home_wins', 'home_looses', 'draws', 'home_rank',
           'home_ranking_points', 'away_rank', 'away_ranking_points']]
        )

    # labels are the values we want to predict
    train_labels = np.array(features.query('date < "2022-12-01"')['home_score'])

    # remove the labels from the features
    # axis 1 refers to the columns
    train_features = features.query('date < "2022-12-01"').drop('home_score', axis = 1).drop('date', axis = 1)
    # convert to numpy array
    train_features = np.array(train_features)

    test_labels = np.array(features.query('date >= "2022-12-01"')['home_score'])
    test_features = features.query('date >= "2022-12-01"').drop('home_score', axis = 1).drop('date', axis = 1)
    test_features = np.array(test_features)

    # instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

    # train the model on training data
    rf.fit(train_features, train_labels)

    # use the forest's predict method on the test data
    predictions = rf.predict(test_features)

    #adding predicts to df
    dataset = pd.merge(pd.DataFrame(predictions.round(0)), df_to_predict, left_index=True, right_index=True)
    dataset.rename(columns={0 : "home_score_predicted"}, inplace=True)
    dataset = dataset[['date', 'home_team', 'home_score_predicted', 'away_score', 'away_team']]
    return dataset

def run_predict_away(df_to_predict, df_created, historical_df):
# one-hot encode the data using pandas get_dummies
    features = pd.get_dummies(
        pd.concat([historical_df,df_to_predict]).reset_index(drop=True)
        [['date', 'home_team', 'away_team', 'home_score', 'away_score',
           'games', 'home_wins', 'home_looses', 'draws', 'home_rank',
           'home_ranking_points', 'away_rank', 'away_ranking_points']]
        )

    # labels are the values we want to predict
    train_labels = np.array(features.query('date < "2022-12-01"')['away_score'])

    # remove the labels from the features
    # axis 1 refers to the columns
    train_features = features.query('date < "2022-12-01"').drop('away_score', axis = 1).drop('date', axis = 1)
    # convert to numpy array
    train_features = np.array(train_features)

    test_labels = np.array(features.query('date >= "2022-12-01"')['away_score'])
    test_features = features.query('date >= "2022-12-01"').drop('away_score', axis = 1).drop('date', axis = 1)
    test_features = np.array(test_features)

    # instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

    # train the model on training data
    rf.fit(train_features, train_labels)

    # use the forest's predict method on the test data
    predictions = rf.predict(test_features)

    #adding predicts to df
    df_created = pd.merge(pd.DataFrame(predictions.round(0)), df_created, left_index=True, right_index=True)
    df_created.rename(columns={0 : "away_score_predicted"}, inplace=True)
    df_created = df_created[['date', 'home_team', 'home_score_predicted', 'away_score_predicted', 'away_team']]
    return df_created