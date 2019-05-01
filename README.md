# Calculation
The jupyter notebook that contains how we calculated the Specialty Score is at ./scoreCalculation.ipynb.
Or click [here](https://github.com/jacobhallberg/SpecialtyScore/blob/master/scoreCalculation.ipynb).

To calculate the Specialty Score statistic we first needed to merge data across all available Statcast data that we could find. This consisted of the 2014 - 2018 batting data.

Afterwards, we removed all of the rows from the database where the pitch_type field contained a NaN value because if the pitch did not have a recorded pitch type the data was useless for our calculation. We then also had to do a bit of preprocessing on the pitch_type field itself by removing all values that contained a digit because there existed quite a few anomalous entries that looked similar to 2412_1214. To do this we first removed the "_" contained within these entries. We then iterated again over each value and removed each entry that was purely a digit, 2412_1214 becomes 24121214. This allowed us to just have the pitch types themselves which could be used for the Specialty Score calculation.

We then create another column called hit type that reads from the pitching description to determine if the ball was hit successfully. Essentially we have a conditional that checks if the description contains the word "hit" and the hit was not a ball or foul ball. This way we only measure the balls that were successfully hit. If the ball was successfully hit we then increment the successful hit counter with respect to the thrown pitch type for that batter.

After getting a count for the number of times that a player has seen each pitch type and the count for the number of successful hits we then begin to calculate the percentage of each pitch type that was successfully hit by each batter. This is simply done by just taking the total number of successfully hit balls for each pitch type and dividing it by the total number of times that the player saw and then multiplying by 100 to get a percentage.

The final calculation is what makes up the Specialty Score statistic itself. Each of the percentage hit calculations for each pitch type is passed through a weighted sum where,
p={pitchType1,pitchType2,...,pitchTypen}
w={w1,w2,...,wn}
SpecialtyScore=∑i=ni=1wi∗pi

What is great about the Specialty Score statistic is that the analyst of a team can work with their team manager and pitchers to adjust the weights of specialty pitches to come up with a Speciality Score that is more useful for their pitcher against some batter. 

# Specialty Score Website
http://specialtyscore.herokuapp.com/

![alt text](https://github.com/jacobhallberg/SpecialtyScore/blob/master/webApp/website.PNG)

# Explanation
 In sabermetrics, there are a variety of statistics used to evaluate the skill of a batter. Statistics such as batting average, slugging, on-base percentage, strikeouts, and other similar statistics evaluate the overall skill of a batter. None of these statistics consider a batter’s ability to hit varying types of pitches, just the batter’s ability to hit pitches as a whole. Some pitchers may be able to effectively hit all types of pitches, while others may only be able to be effective pitchers for fastballs. The Speciality Score statistic aims to gauge a batter’s ability to hit "speciality" pitches such as curveballs, sliders, changeups, and so on. Batters with high batting skill for these speciality pitches will have a high speciality score while batter with less skill for these pitches will have a lower speciality score.

This statistic could be used to identify batters with a unique batting skill as compared to other batters. A team manager could use this information to ensure that the team is well-balanced in terms of batting ability: a team needs batters that are able to excel against specialty pitches. Pitchers could also benefit from this information by using against batters with low specialty scores. If a pitcher is going to pitch to a batter who has a low specialty score, then he can throw specialty pitches to the batter.

The statistic is presented with a website: http://specialtyscore.herokuapp.com/. A user can access the website and read some information about the statistic and how it is calculated. A user can enter a Major League Baseball player’s name and see his Specialty Score. The Specialty Scores will be available for all players that have enough Statcast data for which we can calculate their score (AB > 200). 

# Data
To calculate the Specialty Score we used the Statcast database spanning the years 2014 - 2018. We only included players with over 200 at-bats.
