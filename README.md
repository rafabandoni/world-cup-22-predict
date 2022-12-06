# World Cup 2022 Prediction: Random Forest Approach
This is a personal project that tries to predict the results of the FIFA World Cup games with a random forest approach.  

## Data Used
For this project, 3 datasets were used:  
- Historical games (which includes world cups and other championships);
- Historical outcomes ratio (win, loose and draw);
- Historical rank on FIFA and rank points.

## Approach
A random forest approach was applied, below we have the log for the tunning on the approach:

### Group Stage: n_estimators = 1000, random_seed = 42:
On this approach, we got:
- Something right (outcome, goals for the home team and/or goals for the visitor team) in 70.83% of the cases;
- Outcome correct on 37.5% of the cases;
- Home goals correct on 29,17% of the cases;
- Visitor goals correct on 35,42% of the cases;
- Bullseye (correct outcome and both team goals) on 6,25% of the cases.  

## Playoffs Stage: n_estimators = 1000, random_seed = 42:
Still developing the predictions for the playoffs.