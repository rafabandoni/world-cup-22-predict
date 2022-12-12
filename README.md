# World Cup 2022 Prediction: Random Forest Approach
This is a personal project that tries to predict the results of the FIFA World Cup games with a random forest approach.  

## Data Used
For this project |  3 datasets were used:  
- Historical games (which includes world cups and other championships);
- Historical outcomes ratio (win |  loose and draw);
- Historical rank on FIFA and rank points.

## Approach
A random forest approach was applied |  below we have the log for the tunning on the approach:

## Group Stage: n_estimators = 1000 |  random_seed = 42:
On this approach |  we got:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-11-21 | Qatar | 2.0 | 1.0 | Ecuador |
2022-11-21 | Senegal | 1.0 | 1.0 | Netherlands |
2022-11-21 | England | 3.0 | 1.0 | Iran |
2022-11-21 | USA | 1.0 | 1.0 | Wales |
2022-11-22 | France | 2.0 | 1.0 | Australia |
2022-11-22 | Denmark | 2.0 | 1.0 | Tunisia |
2022-11-22 | Mexico | 1.0 | 1.0 | Poland |
2022-11-22 | Argentina | 1.0 | 1.0 | Saudi Arabia |
2022-11-23 | Belgium | 3.0 | 1.0 | Canada |
2022-11-23 | Spain | 2.0 | 1.0 | Costa Rica |
2022-11-23 | Germany | 2.0 | 1.0 | Japan |
2022-11-23 | Morocco | 1.0 | 1.0 | Croatia |
2022-11-24 | Switzerland | 2.0 | 0.0 | Cameroon |
2022-11-24 | Uruguay | 3.0 | 1.0 | South Korea |
2022-11-24 | Portugal | 2.0 | 1.0 | Ghana |
2022-11-24 | Brazil | 2.0 | 1.0 | Serbia |
2022-11-25 | Wales | 2.0 | 1.0 | Iran |
2022-11-25 | Qatar | 0.0 | 1.0 | Senegal |
2022-11-25 | Netherlands | 2.0 | 1.0 | Ecuador |
2022-11-25 | England | 1.0 | 0.0 | USA |
2022-11-26 | Tunisia | 1.0 | 1.0 | Australia |
2022-11-26 | Poland | 2.0 | 1.0 | Saudi Arabia |
2022-11-26 | France | 2.0 | 1.0 | Denmark |
2022-11-26 | Argentina | 2.0 | 1.0 | Mexico |
2022-11-27 | Japan | 1.0 | 1.0 | Costa Rica |
2022-11-27 | Belgium | 2.0 | 1.0 | Morocco |
2022-11-27 | Croatia | 2.0 | 0.0 | Canada |
2022-11-27 | Spain | 1.0 | 3.0 | Germany |
2022-11-28 | Cameroon | 1.0 | 2.0 | Serbia |
2022-11-28 | South Korea | 1.0 | 1.0 | Ghana |
2022-11-28 | Brazil | 1.0 | 1.0 | Switzerland |
2022-11-28 | Portugal | 1.0 | 1.0 | Uruguay |
2022-11-29 | Wales | 1.0 | 2.0 | England |
2022-11-29 | Iran | 1.0 | 2.0 | USA |
2022-11-29 | Ecuador | 1.0 | 1.0 | Senegal |
2022-11-29 | Netherlands | 3.0 | 0.0 | Qatar |
2022-11-30 | Australia | 1.0 | 1.0 | Denmark |
2022-11-30 | Tunisia | 1.0 | 1.0 | France |
2022-11-30 | Poland | 1.0 | 1.0 | Argentina |
2022-11-30 | Saudi Arabia | 1.0 | 1.0 | Mexico |
2022-12-01 | Croatia | 1.0 | 1.0 | Belgium |
2022-12-01 | Canada | 1.0 | 1.0 | Morocco |
2022-12-01 | Japan | 1.0 | 2.0 | Spain |
2022-12-01 | Costa Rica | 1.0 | 3.0 | Germany |
2022-12-02 | Ghana | 1.0 | 1.0 | Uruguay |
2022-12-02 | South Korea | 2.0 | 1.0 | Portugal |
2022-12-02 | Serbia | 1.0 | 1.0 | Switzerland |
2022-12-02 | Cameroon | 1.0 | 2.0 | Brazil |

## Playoffs Stage: n_estimators = 1000 |  random_seed = 42:
The playoffs predictions were developed after each bracket was decided. Important note: real results from any stage weren't added to the training set.

### Phase of 16



### Phase of 8



### Semifinals



### Final