# PVU-WeatherBoy
 Calculator to predict the probability of weather affecting your plants in Plant vs Undead (Plantvsundead | PVU)

The program will recommend wether to use a greenhouse in 3 different ways:
* -Electro- (! Greenhouse !) -> Average impact is negative
* -Electro- (Safety Greenhouse) -> Recommends a greenhouse based on `SAFETY_MARGIN`
* -Electro- (Safe) -> Average impact above `SAFETY_MARGIN`
* -Electro- (No Bad Weather - Safe) -> No weather with a negative impact possible for the next day

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
* Sort output by most to the least effected

## Using selenium (Deprecated)

If you wish to use selenium instead of the requests library, then you can enable it by setting the 
`AUTO_ENABLED` option equal to 2. You will also have to install the selenium package (`pip install selenium`)
download `chromedriver.exe`, which can be found here:
https://sites.google.com/chromium.org/driver/, and place it in the PVU-WeatherBoy folder.
This method is slower and will most probably stop working as it may not be mantained.


## Sample of output
```
Fetching data

Predicting day: 10/17/2021
Tomorrows Season: Winter
Previous weather: Locusts Swarm, Hurricanes


Tomorrows Weather Prediction:

- Light - (! Greenhouse !) 
   Probabilities: (+)6.67%, (-)33.33%, (~)60.00%
   Max Impact: +20% | -40%
   Possible Buffs: +20% 
   Possible Debuffs: -40% -20% -20% -20% -10% 
   Average Impact: -6.00%

- Ice - (Safe)
   Probabilities: (+)30.00%, (-)10.00%, (~)60.00%
   Max Impact: +120% | -40%
   Possible Buffs: +120% +100% +60%
   Possible Debuffs: -40%
   Average Impact: 24.00%

- Metal - (No Bad Weather - Safe)
   Probabilities: (+)30.00%, (-)0.00%, (~)70.00%
   Max Impact: +100% | -0%
   Possible Buffs: +100% +50% +40%    Average Impact: 19.00%

- Fire - (Safe)
   Probabilities: (+)40.00%, (-)30.00%, (~)30.00%
   Max Impact: +100% | -60%
   Possible Buffs: +100% +80% +40% +40%
   Possible Debuffs: -60% -40% -40%
   Average Impact: 12.00%

- Wind - (No Bad Weather - Safe)
   Probabilities: (+)30.00%, (-)0.00%, (~)70.00%
   Max Impact: +50% | -0%
   Possible Buffs: +50% +50% +10%    Average Impact: 11.00%

- Electro - (No Bad Weather - Safe)
   Probabilities: (+)20.00%, (-)0.00%, (~)80.00%
   Max Impact: +50% | -0%
   Possible Buffs: +50% +50%    Average Impact: 10.00%

- Water - (Safety Greenhouse)
   Probabilities: (+)10.00%, (-)10.00%, (~)80.00%
   Max Impact: +60% | -20%
   Possible Buffs: +60%
   Possible Debuffs: -20%
   Average Impact: 4.00%

- Dark - (No Bad Weather - Safe)
   Probabilities: (+)0.00%, (-)0.00%, (~)100.00%
   Max Impact: +0% | -0%
   Average Impact: 0.00%

- Parasite - (No Bad Weather - Safe)
   Probabilities: (+)0.00%, (-)0.00%, (~)100.00%
   Max Impact: +0% | -0%
   Average Impact: 0.00%

Summary:
No Negative Weather: Metal (+19%)  Wind (+11%)  Electro (+10%)  Dark (+0%)  Parasite (+0%)
Safe: Ice (+24%)  Fire (+12%)
Under Safety Margin: Water (+4%)
Unsafe: Light (-6%)

Press enter to exit
```