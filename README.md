# PVU-WeatherBoy
 Calculator to predict the probability of weather affecting your plants in Plant vs Undead (Plantvsundead | PVU)

The program will recommend wether to use a greenhouse in 3 different ways:
* -Electro- (! Greenhouse !) -> Average impact is negative
* -Electro- (Safety Greenhouse) -> Recommends a greenhouse based on `SAFETY_MARGIN`
* -Electro- (Safe) -> Average impact above `SAFETY_MARGIN`

If auto fetch is disabled, and you are unsure of the previous weathers, you can use *NULL*.
The Season is currently required.

## Settings
If you want to disable the automatic weather fetch, open options.txt with notepad or any editor and
change the line `AUTO_ENABLED = 1` to `AUTO_ENABLED = 0`, if there is no internet or the fetch fails
, the program will automatically ask for the data to be manually entered.

The `SAFETY_MARGIN`  used to recommend a greenhouse can be edited in the options.txt file
at the line `SAFETY_MARGIN = 1`.
A value of 1 means that it will recommend a greenhouse if the average impact is below 1%.

## Instalation
To use this script you will need Python 3+ installed, https://www.python.org/. 
In order to run it you can simply double click `main.py`

## Current Features:
* Show probability of positive, negative and neutral weather tomorrow
* List the maximum impact, both positive and negative, that may occur
* List all the positive and negative effects that could occur
* Display the average of all possible weather effects
* Automatically fetch the weather data if possible
* Recommend using a greenhouse depending on the average impact and a safety margin
* Show a summary of all recommendation towards the plant types
* Sort output by most to least effected

## Using selenium (Deprecated)

If you wish to use selenium instead of the requests library, then you can enable it by setting the 
`AUTO_ENABLED` option equal to 2. You will also have to install the selenium package (`pip install selenium`)
download `chromedriver.exe`, which can be found here:
https://sites.google.com/chromium.org/driver/, and place it in the PVU-WeatherBoy folder.
This method is slower and will most probably stop working as it may not be mantained.


## Sample of output
```
Fetching data

Predicting day: 10/10/2021
Tomorrows Season: Autumn
Previous weather: Thunder Storm, Locusts Swarm


Tomorrows Weather Prediction:

- Dark - (Safe) 
   Probabilities: (+)33.33%, (-)0.00%, (~)66.67%
   Max Impact: +400% | -0%
   Possible Buffs: +400% +100% +50% +40% +20% 
   Average Impact: 40.67%

- Parasite - (Safe) 
   Probabilities: (+)20.00%, (-)0.00%, (~)80.00%
   Max Impact: +100% | -0%
   Possible Buffs: +100% +100% +100% 
   Average Impact: 20.00%

- Water - (Safe) 
   Probabilities: (+)40.00%, (-)13.33%, (~)46.67%
   Max Impact: +100% | -30%
   Possible Buffs: +100% +60% +50% +40% +20% +10% 
   Possible Debuffs: -30% -20% 
   Average Impact: 15.33%

- Electro - (Safe) 
   Probabilities: (+)20.00%, (-)0.00%, (~)80.00%
   Max Impact: +100% | -0%
   Possible Buffs: +100% +50% +50% 
   Average Impact: 13.33%

- Wind - (Safe) 
   Probabilities: (+)26.67%, (-)6.67%, (~)66.67%
   Max Impact: +100% | -50%
   Possible Buffs: +100% +50% +50% +50% 
   Possible Debuffs: -50% 
   Average Impact: 13.33%

- Metal - (Safe) 
   Probabilities: (+)20.00%, (-)20.00%, (~)60.00%
   Max Impact: +120% | -60%
   Possible Buffs: +120% +100% +40% 
   Possible Debuffs: -60% -30% -20% 
   Average Impact: 10.00%

- Fire - (Safe) 
   Probabilities: (+)13.33%, (-)20.00%, (~)66.67%
   Max Impact: +100% | -40%
   Possible Buffs: +100% +60% 
   Possible Debuffs: -40% -40% -30% 
   Average Impact: 3.33%

- Ice - (Safe) 
   Probabilities: (+)13.33%, (-)6.67%, (~)80.00%
   Max Impact: +40% | -40%
   Possible Buffs: +40% +30% 
   Possible Debuffs: -40% 
   Average Impact: 2.00%

- Light - (! Greenhouse !) 
   Probabilities: (+)6.67%, (-)33.33%, (~)60.00%
   Max Impact: +20% | -40%
   Possible Buffs: +20% 
   Possible Debuffs: -40% -20% -20% -20% -10% 
   Average Impact: -6.00%

Summary:
Safe: Dark (+41%)  Parasite (+20%)  Water (+15%)  Electro (+13%)  Wind (+13%)  Metal (+10%)  
Under Safety Margin: Fire (+3%)  Ice (+2%)  
Unsafe: Light (-6%)  

Press enter to exit
```