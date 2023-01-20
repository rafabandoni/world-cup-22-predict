# World Cup 2022 Prediction: Random Forest Approach
This is a personal project that tries to predict the results of the FIFA World Cup games with a random forest approach.  

## Data Used
For this project, 3 datasets were used:  
- Historical games (which includes world cups and other championships);
- Historical outcomes ratio (win, loose and draw);
- Historical rank on FIFA and rank points.  

## Approach
A random forest approach was applied, the number of n_estimators were 1000 and random_seed is 42.

# Predictions based on algorithm itself
On this first item, we will imagine that the first predictions of the algorithm made the following phases, ignoring reality.

## Group Stage:
For group stage predictions, we got:

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

## Playoffs Stage:

### Phase of 16
The phase of 16 predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team | 
--- | --- | --- | --- | --- |
2022-12-03 | Netherlands | 1.0 | 0.0 | USA | 
2022-12-03 | Argentina | 1.0 | 1.0 | Denmark | 
2022-12-04 | France | 2.0 | 1.0 | Poland | 
2022-12-04 | England | 1.0 | 0.0 | Senegal | 
2022-12-05 | Germany | 2.0 | 2.0 | Croatia | 
2022-12-05 | Brazil | 2.0 | 1.0 | Portugal | 
2022-12-06 | Belgium | 1.0 | 1.0 | Spain | 
2022-12-06 | Uruguay | 1.0 | 1.0 | Switzerland | 

On penalties simulation, Denmark, Croatia, Spain and Switzerland won.

### Phase of 8
The phase of 8 predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-09 | Netherlands | 1.0 | 1.0 | Denmark |
2022-12-09 | Brazil | 2.0 | 1.0 | Croatia |
2022-12-10 | Spain | 2.0 | 1.0 | Switzerland |
2022-12-10 | France | 2.0 | 1.0 | England |

On penalties simulation, Netherlands and England won.

### Semifinals
The semifinals predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-13 | Brazil | 1.0 | 2.0 | Netherlands |
2022-12-14 | Spain | 1.0 | 1.0 | England |

On penalties, Spain won.

### Final
The final and third place predictions are:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-17 | Netherlands | 2.0 | 1.0 | Spain |
2022-12-18 | Brazil | 1.0 | 1.0 | England |

On penalties, Brazil gor third place.

# Predictions based on reality
On this item, we predicted, collected the results and compared them with the reality. Here, we are using the reality as definitions, so the predicts won't create new phases.

## Group Stage:
For group stage predictions, we got:

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

As shown above, the stage group predicted right at least one of the features (home goals, away goals or final outcome) in 70.8% of the cases, which:
- 31.25% predicted the home goals;
- 20.83% predicted the away goals;
- 43.75% predicted the final outcome;
- 6.25% was bullseye, predicting both goals and outcome correct.

## Playoffs Stage:
The playoffs predictions were developed after each bracket was decided. Important note: real results from any stage weren't added to the training set.

### Phase of 16
The phase of 16 predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team | 
--- | --- | --- | --- | --- |
2022-12-03 | Netherlands | 1.0 | 0.0 | USA | 
2022-12-03 | Argentina | 2.0 | 1.0 | Australia | 
2022-12-04 | France | 2.0 | 1.0 | Poland | 
2022-12-04 | England | 1.0 | 0.0 | Senegal | 
2022-12-05 | Japan | 1.0 | 1.0 | Croatia | 
2022-12-05 | Brazil | 3.0 | 1.0 | South Korea | 
2022-12-06 | Morocco | 1.0 | 1.0 | Spain | 
2022-12-06 | Portugal | 1.0 | 1.0 | Switzerland | 

On the phase of 16, the algorithm predicted some feature correct on 100% of the cases, divided in:
- 25% predicted the home goals;
- 75% predicted the away goals;
- 87% predicted the final outcome;
- 25% was bullseye, predicting both goals and outcome correct.

### Phase of 8
The phase of 8 predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-09 | Netherlands | 1.0 | 1.0 | Argentina |
2022-12-09 | Croatia | 1.0 | 2.0 | Brazil |
2022-12-10 | England | 1.0 | 1.0 | France |
2022-12-10 | Morocco | 2.0 | 1.0 | Portugal |

On the phase of 8, the algorithm got some feature righ in 100% of the cases, being:
- 50% of the home goals;
- 50% of the final outcomes;
- No away goals nor bullseye happened on this stage.

### Semifinals
The semifinals predictions were:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-13 | Argentina | 1.0 | 1.0 | Croatia |
2022-12-14 | France | 2.0 | 1.0 | Morocco |

On the semifinals phase, the algorithm was able to predict right:
- 50% of the final outcomes;
- 50% of the home goals.

### Final
The final and third place predictions are:

date | home_team | home_score_predicted | away_score_predicted | away_team |
--- | --- | --- | --- | --- |
2022-12-17 | Croatia | 1.0 | 1.0 | Morocco |
2022-12-18 | Argentina | 1.0 | 1.0 | France |

On finals phase, the algorithm was able to predict right:
- The away goals on third place game;
- The final outcome of the final game (draw).

# Overalls

- The phase of 16 was the higher number of correct outcomes, predicting more than 80% of the games;
- On the phase of 8 and the semifinals, the algorithm predicted right half of the outcomes;
- On group phase, the algorithm was better predicting the home goals (31% right), and on the phase of 16 it was better predicting away goals (75%);
- Overall, the algorithm predicted right 48% of the outcomes.