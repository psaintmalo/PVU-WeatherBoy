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
change the line `AUTO_ENABLED = 1` to `AUTO_ENABLED = 0`, if selenium or chromedriver.exe
are missing, the program will automatically ask for the data to be manually entered.

The `SAFETY_MARGIN`  used to recommend a greenhouse can be edited in the options.txt file
at the line `SAFETY_MARGIN = 1`.
A value of 1 means that it will recommend a greenhouse if the average impact is below 1%.

## Required Packages:
In order to use the automatic weather fetcher you need to have *selenium* python package installed.
If it is not installed then you will be prompted to enter the weather manually. For ease of use I 
have included chromedriver.exe, if you dont feel comfortable, feel free to delete the one included 
and get chromedriver.exe from the official website: https://sites.google.com/chromium.org/driver/,
and place it inside the PVU-WeatherBoy folder.

## Current Features:
* Show probability of positive, negative and neutral weather tomorrow
* List the maximum impact, both positive and negative, that may occur
* List all the positive and negative effects that could occur
* Display the average of all possible weather effects
* Automatically fetch the weather data if possible
* Recommend using a greenhouse depending on the average impact and a safety margin
* Show a summary of all recommendation towards the plant types
