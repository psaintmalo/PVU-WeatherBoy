from enum import Enum
from time import sleep
import datetime
import os
import requests
import re


LOG_ERRORS = False
base_url = "https://pvuextratools.com/"
forecast_url = "en/weather/forecast"

class PlantType(Enum):
    DARK = 0
    ELECTRO = 1
    FIRE = 2
    ICE = 3
    LIGHT = 4
    METAL = 5
    PARASITE = 6
    WATER = 7
    WIND = 8


class Weather(Enum):
    NULL = -1

    CLOUDY = 0

    IRON_RAIN = 1
    IRONRAIN = 1

    COLD_WAVE = 2
    COLDWAVE = 2

    LOCUSTS_SWARM = 3
    LOCUSTSWARM = 3

    CORONAL_MASS_EJECTION = 4
    CORONALMASSEJECTION = 4

    MAGNETIC_RECONNECTION = 5
    MAGNETICRECONNECTION = 5

    EARTHQUAKE = 6

    MALARIA = 7

    FLOOD = 8

    MOONLIGHT = 9
    MOON_LIGHT = 9

    HEATWAVE = 10
    HEAT_WAVE = 10

    PROTON_STORM = 11
    PROTONSTORM = 11

    HURRICANES = 12
    RAINY = 13

    RATS_SWARM = 14
    RATSSWAM = 14

    TORNADO = 15

    SNOWY = 16

    TSUNAMI = 17

    SOLAR_FLARES = 18
    SOLARFLARES = 18

    VOLCANO = 19

    SOLAR_MAXIMA = 20
    SOLARMAXIMA = 20

    WINDY = 21

    SUNNY = 22

    WINTER_STORM = 23
    WINTERSTORM = 23

    THUNDER_STORM = 24
    THUNDERSTORM = 24


class Season(Enum):
    ALL = -1
    SPRING = 0
    SUMMER = 1
    AUTUMN = 2
    WINTER = 3


def effects(metal=0.0, dark=0.0, light=0.0, water=0.0, ice=0.0, wind=0.0, electro=0.0, fire=0.0, parasite=0.0):
    return {PlantType.DARK: dark, PlantType.ELECTRO: electro, PlantType.FIRE: fire, PlantType.LIGHT: light,
            PlantType.METAL: metal, PlantType.PARASITE: parasite, PlantType.WATER: water, PlantType.WIND: wind,
            PlantType.ICE: ice}


weatherCloudy = effects(light=-0.1, wind=-0.5)

weatherIronRain = effects(metal=1.2, water=0.4)

weatherColdWave = effects(ice=1.2, fire=-0.6)  # fire -0.6 or -0.4??? Discord says -0.6

weatherLocustSwarm = effects(parasite=1.0)

weatherCoronalMassEjection = effects(light=1.0, fire=0.4)  # light 1.0 or 1.2??? Discord says 1.0

weatherMagneticReconnection = effects(metal=0.5, electro=0.5)

weatherEarthquake = effects(metal=1.0, wind=0.5)

weatherMalaria = effects(parasite=1.0)

weatherFlood = effects(metal=-1.0, water=1.0)

weatherMoonlight = effects(dark=4.0)

# weatherHeatwave = effects(dark=0.1, light=0.2, water=-0.3, ice=-0.6)  # Actual in game weather below
weatherHeatwave = effects(metal=0.1, light=0.2, fire=1.0, water=-0.3, ice=-0.6)

weatherProtonStorm = effects(light=2.0)

weatherHurricanes = effects(dark=0.4, light=-0.2, water=0.5, ice=0.4, wind=0.4, electro=0.4, fire=-0.4)

weatherRainy = effects(metal=-0.3, water=1.0, fire=-0.3)

weatherRatsSwarm = effects(parasite=1.0)

weatherTornado = effects(dark=0.5, light=-0.4, water=0.2, wind=1.0, electro=0.5)

weatherSnowy = effects(water=0.6, ice=1.0, fire=-0.4)

weatherTsunami = effects(metal=-0.6, dark=0.2, light=-0.2, water=0.6, ice=0.3, fire=-0.4)

weatherSolarFlares = effects(light=0.8, fire=0.8)

weatherVolcano = effects(metal=0.4, water=-0.2, ice=-0.4, fire=1.0)

weatherSolarMaxima = effects(light=1.0, fire=0.4)

weatherWindy = effects(light=0.2, wind=0.5)

weatherSunny = effects(water=-0.3, fire=0.6)

weatherWinterStorm = effects(light=-0.2, ice=0.6, wind=0.1, electro=0.5, fire=-0.4)

weatherThunderStorm = effects(metal=-0.2, dark=1.0, light=-0.2, water=0.1, electro=1.0)

allWeather = {Weather.CLOUDY: weatherCloudy, Weather.IRON_RAIN: weatherIronRain,
              Weather.COLDWAVE: weatherColdWave, Weather.SNOWY: weatherSnowy,
              Weather.CORONAL_MASS_EJECTION: weatherCoronalMassEjection,
              Weather.MAGNETICRECONNECTION: weatherMagneticReconnection,
              Weather.FLOOD: weatherFlood, Weather.MOON_LIGHT: weatherMoonlight,
              Weather.EARTHQUAKE: weatherEarthquake, Weather.HEATWAVE: weatherHeatwave,
              Weather.HURRICANES: weatherHurricanes, Weather.LOCUSTS_SWARM: weatherLocustSwarm,
              Weather.MALARIA: weatherMalaria, Weather.PROTON_STORM: weatherProtonStorm,
              Weather.RAINY: weatherRainy, Weather.RATS_SWARM: weatherRatsSwarm,
              Weather.SOLAR_FLARES: weatherSolarFlares, Weather.SOLAR_MAXIMA: weatherSolarMaxima,
              Weather.SUNNY: weatherSunny, Weather.THUNDER_STORM: weatherThunderStorm,
              Weather.TORNADO: weatherTornado, Weather.TSUNAMI: weatherTsunami,
              Weather.VOLCANO: weatherVolcano, Weather.WINDY: weatherWindy,
              Weather.WINTERSTORM: weatherWinterStorm}

springSeason = {Weather.CLOUDY: weatherCloudy, Weather.EARTHQUAKE: weatherEarthquake,
                Weather.HURRICANES: weatherHurricanes, Weather.IRON_RAIN: weatherIronRain,
                Weather.LOCUSTS_SWARM: weatherLocustSwarm, Weather.MALARIA: weatherMalaria,
                Weather.RAINY: weatherRainy, Weather.RATS_SWARM: weatherRatsSwarm,
                Weather.SUNNY: weatherSunny, Weather.TSUNAMI: weatherTsunami,
                Weather.VOLCANO: weatherVolcano}

summerSeason = {Weather.CLOUDY: weatherCloudy, Weather.CORONAL_MASS_EJECTION: weatherCoronalMassEjection,
                Weather.EARTHQUAKE: weatherEarthquake, Weather.HEATWAVE: weatherHeatwave,
                Weather.HURRICANES: weatherHurricanes, Weather.LOCUSTS_SWARM: weatherLocustSwarm,
                Weather.MALARIA: weatherMalaria, Weather.PROTON_STORM: weatherProtonStorm,
                Weather.RAINY: weatherRainy, Weather.RATS_SWARM: weatherRatsSwarm,
                Weather.SOLAR_FLARES: weatherSolarFlares, Weather.SOLAR_MAXIMA: weatherSolarMaxima,
                Weather.SUNNY: weatherSunny, Weather.THUNDER_STORM: weatherThunderStorm,
                Weather.TORNADO: weatherTornado, Weather.TSUNAMI: weatherTsunami,
                Weather.VOLCANO: weatherVolcano}

autumnSeason = {Weather.CLOUDY: weatherCloudy, Weather.EARTHQUAKE: weatherEarthquake,
                Weather.FLOOD: weatherFlood, Weather.HURRICANES: weatherHurricanes,
                Weather.IRON_RAIN: weatherIronRain, Weather.LOCUSTS_SWARM: weatherLocustSwarm,
                Weather.MALARIA: weatherMalaria, Weather.MOONLIGHT: weatherMoonlight,
                Weather.RAINY: weatherRainy, Weather.RATS_SWARM: weatherRatsSwarm,
                Weather.SUNNY: weatherSunny, Weather.THUNDER_STORM: weatherThunderStorm,
                Weather.TORNADO: weatherTornado, Weather.TSUNAMI: weatherTsunami,
                Weather.VOLCANO: weatherVolcano, Weather.WINDY: weatherWindy,
                Weather.WINTER_STORM: weatherWinterStorm}

winterSeason = {Weather.COLD_WAVE: weatherColdWave, Weather.CORONAL_MASS_EJECTION: weatherCoronalMassEjection,
                Weather.EARTHQUAKE: weatherEarthquake, Weather.MAGNETIC_RECONNECTION: weatherMagneticReconnection,
                Weather.SNOWY: weatherSnowy, Weather.SOLAR_FLARES: weatherSolarFlares,
                Weather.SOLAR_MAXIMA: weatherSolarMaxima, Weather.VOLCANO: weatherVolcano,
                Weather.WINDY: weatherWindy, Weather.WINTER_STORM: weatherWinterStorm}


masterWeather = {Season.SPRING: springSeason, Season.SUMMER: summerSeason, Season.AUTUMN: autumnSeason,
                 Season.WINTER: winterSeason}


def manual_data_input():

    season_input = input("Enter current season: ")
    s = Season["ALL"]

    try:
        s = Season[clean_name(season_input)]
        if(s == Season.ALL):
            print("Using all for the season is not recommended.")
            return s, (Weather.NULL, Weather.NULL)
    except KeyError as e:

        if LOG_ERRORS:
            raise e

        exit("Invalid season. Valid season are: Spring, Summer, Autumn and Winter or ALL if unsure")

    weather_yesterday = Weather["NULL"]
    weather_today = Weather["NULL"]

    try:
        weather_yesterday_input = input("Enter yesterday's weather: ")
        weather_yesterday = Weather[clean_name(weather_yesterday_input)]

        weather_today_input = input("Enter today's weather: ")
        weather_today = Weather[clean_name(weather_today_input)]
    except KeyError as e:

        if LOG_ERRORS:
            raise e

        exit("Invalid weather name. If unsure about weather, use \"null\"")

    return s, (weather_yesterday, weather_today)


def setDriver():

    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        # Set up the driver to use headless chrome
        options = Options()
        options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        return driver

    except ImportError as e:

        if LOG_ERRORS:
            raise e

        exit("\nPlease ensure the selenium python package is installed and the driver is present in order to use "
             "the automatic weather fetcher\n")


# No longer supported. Left in for reference
def selenium_scraper():

    print("Starting driver")
    driver = setDriver()
    print("Fetching data")
    driver.get(base_url + forecast_url)
    # sleep(1)
    events = driver.find_elements_by_class_name("event")
    w = (Weather[clean_name(events[0].get_attribute("textContent")[7:])],
         Weather[clean_name(events[1].get_attribute("textContent")[7:])])

    seasons = driver.find_elements_by_class_name("season")
    s = Season[clean_name(seasons[2].get_attribute("textContent")[8:])]

    dates = driver.find_elements_by_class_name("card-date")
    print("\nPredicting day: " + dates[2].get_attribute("textContent"))
    print("Tomorrows Season: " + s.name.title())
    print("Previous weather: {}, {}".format(w[0].name.title().replace("_", " ")
                                            , w[1].name.title().replace("_", " ")))

    try:
        driver.quit()
    except Exception as e:

        if LOG_ERRORS:
            raise e

        exit("Error while closing the driver")

    return s, w


def requests_scraper():

    print("Fetching data")

    find_runtime_regex = r"(?<=<script src=\")(runtime.)[a-zA-Z0-9]{20}(.js)(?=\" defer><\/script>)"
    find_stats_regex = r"(?<={)([0-9]{1})(:\")([a-z0-9]{20})(?=\"})"
    base_stats_regex = r"(?<={}\":\")([0-9A-Za-z\/ ]+)(?=\",)"

    skeleton_r = requests.get(base_url + forecast_url)
    skeleton_text = skeleton_r.text

    runtime_url = re.search(find_runtime_regex, skeleton_text).group(0)

    runtime_r = requests.get(base_url + runtime_url)
    runtime_text = runtime_r.text

    runtime_regex_groups = re.search(find_stats_regex, runtime_text)
    stats_url = "{}.{}.js".format(runtime_regex_groups.group(1), runtime_regex_groups.group(3))

    stats_r = requests.get(base_url + stats_url)
    stats_text = stats_r.text

    yesterday_event_text = re.search(base_stats_regex.format("yesterdayEvent"), stats_text).group(1)
    yesterday_event = Weather[clean_name(yesterday_event_text)]

    today_event_text = re.search(base_stats_regex.format("todayEvent"), stats_text).group(1)
    today_event = Weather[clean_name(today_event_text)]

    w = (yesterday_event, today_event)

    season_text = re.search(base_stats_regex.format("tomorrowSeason"), stats_text).group(1)
    s = Season[clean_name(season_text)]

    tomorrow_date = re.search(base_stats_regex.format("tomorrowDate"), stats_text).group(1)

    print("\nPredicting day: " + tomorrow_date)
    print("Tomorrows Season: " + s.name.title())
    print("Previous weather: {}, {}".format(w[0].name.title().replace("_", " ")
                                            , w[1].name.title().replace("_", " ")))

    return s, w


def auto_data_scraper(mode):
    try:
        if mode == "1":
            s, w = requests_scraper()
        elif mode == "2":
            s, w = selenium_scraper()
        else:
            exit("Invalid mode")

    except Exception as e:

        if LOG_ERRORS:
            raise e

        print("Something went wrong with the automatic fetch...")
        s, w = manual_data_input()

    return s, w


def clean_name(name):
    return name.strip().upper().replace(" ", "_")


def get_possible_weather(s, c):
    enumResult = []
    result = []
    if(s != Season.ALL):
        for wEnum, weather in masterWeather.get(s).items():
            if wEnum in c:
                continue
            enumResult.append(wEnum)
            result.append(weather)

    else:
        for wEnum, weather in allWeather.items():
            enumResult.append(wEnum)
            result.append(weather)

    return enumResult, result


def get_relevant(wL, type):
    positiveImpact = []
    negativeImpact = []

    for w in wL:
        impact = w.get(type)
        if impact > 0.0:
            positiveImpact.append(impact)
        elif impact < 0.0:
            negativeImpact.append(impact)

    return positiveImpact, negativeImpact


def avg_impact(wL, type):
    avg = 0.0
    size = len(wL)

    for weather in wL:
        effect = weather.get(type)
        avg += effect/size

    return avg


def all_impact_stats(wL):

    result = {}

    for type in PlantType:
        posImpact, negImpact = get_relevant(wL, type)
        avgImpact = avg_impact(wL, type)
        result[type] = [avgImpact, (posImpact, negImpact)]

    return result


def printStats(ptype, avg, pos, neg, weatherLen):
    numOfNegImpact = len(neg)
    numOfPosImpact = len(pos)
    maxBuff = max(pos)*100 if numOfPosImpact > 0 else 0
    maxDebuff = abs(min(neg)*100) if numOfNegImpact > 0 else 0

    if numOfNegImpact == 0:
        recText = "No Bad Weather - Safe"
    elif avg < 0:
        recText = "! Greenhouse !"
    elif avg < 0+SAFETY_MARGIN:
        recText = "Safety Greenhouse"
    else:
        recText = "Safe"

    print("- {} - ({}) ".format(ptype.name.title(), recText))
    print("   Probabilities: (+){:.2f}%, (-){:.2f}%, (~){:.2f}%".format(
        (numOfPosImpact/weatherLen)*100, (numOfNegImpact/weatherLen)*100,
        ((weatherLen-(numOfNegImpact+numOfPosImpact))/weatherLen)*100))
    print("   Max Impact: +{:.0f}% | -{:.0f}%".format(maxBuff, maxDebuff))

    if numOfPosImpact > 0:
        print("   Possible Buffs: ", end="")
        for buf in sorted(pos, reverse=True):
            print("+{:.0f}% ".format(buf*100), end="")

    if numOfNegImpact > 0:
        print("\n   Possible Debuffs: ", end="")
        for debuf in sorted(neg):
            print("{:.0f}% ".format(debuf*100), end="")
        print("")

    print("   Average Impact: {:.2f}%\n".format((avg*100)))


def loadSettings(file_location):
    result = {}

    with open(file_location, "r") as file:

        for line in file:

            if line.strip() == "":
                pass
            elif line[0].strip() == "#":
                pass
            else:
                fields = line.split("=")
                fields = list(map(lambda field: field.strip(), fields))
                if len(fields) != 2:
                    pass
                else:
                    result[fields[0]] = fields[1]

    return result


if __name__ == "__main__":

    options_filename = "options.txt"

    # Default settings values
    AUTO_ENABLED = "1"
    SAFETY_MARGIN = 5
    WAIT_EXIT = True

    # Try to load the settings
    if not os.path.isfile(options_filename):
        print("Options file not found. Attempting auto fetch. Default safety margin = 5")
    else:
        settings = loadSettings(options_filename)

        if settings["AUTO_ENABLED"] in ["0", "1", "2"]:
            AUTO_ENABLED = settings["AUTO_ENABLED"]
        else:
            print("Invalid AUTO_ENABLED mode")

        if settings["SAFETY_MARGIN"].isnumeric():
            num = int(settings["SAFETY_MARGIN"])
            if 100 > num > -100:
                SAFETY_MARGIN = num/100
            else:
                print("SAFETY_MARGIN should be between 100 and -100")
        else:
            print("Invalid SAFETY_MARGIN value")

        if settings["WAIT_EXIT"] == "0":
            WAIT_EXIT = False
        elif not settings["WAIT_EXIT"] in ["0", "1"]:
            print("Invalid WAIT_EXIT value")

        if settings["LOG_ERRORS"] == "1":
            LOG_ERRORS = True
        elif not settings["LOG_ERRORS"] in ["0", "1"]:
            print("Invalid LOG_ERRORS mode")

    # Use the appropriate data input method
    if AUTO_ENABLED in ["1", "2"]:
        season, weatherCooldown = auto_data_scraper(AUTO_ENABLED)
    else:
        season, weatherCooldown = manual_data_input()

    _, weatherList = get_possible_weather(season, weatherCooldown)
    weatherLen = len(weatherList)

    masterData = all_impact_stats(weatherList)
    catBreakdown = {"no_debuffs": [], "safe": [], "safety_margin": [], "unsafe": []}

    print("\n\nTomorrows Weather Prediction:\n")

    masterSorted = dict(sorted(masterData.items(), key=lambda item: item[1][0], reverse=True))

    for ptype, stats in masterSorted.items():

        avg = stats[0]
        n_debuffs = len(stats[1][1])
        pTuple = (ptype, avg)

        if n_debuffs == 0:
            catBreakdown["no_debuffs"].append(pTuple)
        elif avg > SAFETY_MARGIN:
            catBreakdown["safe"].append(pTuple)
        elif avg < 0:
            catBreakdown["unsafe"].append(pTuple)
        else:
            catBreakdown["safety_margin"].append(pTuple)

        printStats(ptype, stats[0], stats[1][0], stats[1][1], weatherLen)

    print("Summary:")
    print("No Bad Weather: ", end="")
    for ptype, avg in catBreakdown["no_debuffs"]:
        print("{} (+{:.0f}%)".format(ptype.name.title(), 100 * avg), end="  ")

    print("\nSafe: ", end="")
    for ptype, avg in catBreakdown["safe"]:
        print("{} (+{:.0f}%)".format(ptype.name.title(), 100*avg), end="  ")

    print("\nUnder Safety Margin: ", end="")
    for ptype, avg in catBreakdown["safety_margin"]:
        print("{} (+{:.0f}%)".format(ptype.name.title(), 100*avg), end="  ")

    catBreakdown["unsafe"] = catBreakdown["unsafe"][::-1]

    print("\nUnsafe: ", end="")
    for ptype, avg in catBreakdown["unsafe"]:
        print("{} ({:.0f}%)".format(ptype.name.title(), 100*avg), end="  ")

    if WAIT_EXIT:
        input("\n\nPress enter to exit")
    else:
        print("")
