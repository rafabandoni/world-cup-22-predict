def enrich_data(dataset, historical_df, ranking_df):
    dataset['date'] = dataset['date'].astype('datetime64')

    # adding outcome ratio
    dataset = dataset.merge(historical_df, left_on=['home_team', 'away_team'], right_on=['country1', 'country2'], how='left').rename(columns={
        'wins' : 'home_wins',
        'looses' : 'home_looses'
    })[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'phase', 'games', 'home_wins', 'home_looses', 'draws']]

    # adding home rank
    dataset = dataset.merge(ranking_df.query('rank_date.astype("datetime64") > 2021').groupby('country_full').mean().round(0),
                                              left_on='home_team',
                                              right_on='country_full',
                                              how='left').rename(columns={
                                                                          'rank' : 'home_rank',
                                                                          'total_points' : 'home_ranking_points'
    })[['date', 'home_team', 'away_team', 'home_score', 'away_score',
        'phase', 'games', 'home_wins', 'home_looses', 'draws', 'home_rank', 'home_ranking_points']]

    # adding away rank
    dataset = dataset.merge(ranking_df.query('rank_date.astype("datetime64") > 2021').groupby('country_full').mean().round(0),
                                              left_on='away_team',
                                              right_on='country_full',
                                              how='left').rename(columns={
                                                                          'rank' : 'away_rank',
                                                                          'total_points' : 'away_ranking_points'
    })[['date', 'home_team', 'away_team', 'home_score', 'away_score',
        'phase', 'games', 'home_wins', 'home_looses', 'draws', 'home_rank',
        'home_ranking_points', 'away_rank', 'away_ranking_points']]

    dataset = dataset.fillna(0)
    return dataset