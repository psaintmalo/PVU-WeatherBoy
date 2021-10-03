AUTO_ENABLED = True
SAFETY_MARGIN = 5  # E.g. If average impact is below +5%, it will recommend a greenhouse.

from enum import Enum
from time import sleep
import datetime


def setDriver():
    # Set up the driver to use headless chrome
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver


if AUTO_ENABLED:
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except ImportError as e:
        AUTO_ENABLED = False
        print("\nPlease ensure the selenium python package is installed in order to use the automatic weather fetcher\n")


def effects(metal=0.0, dark=0.0, light=0.0, water=0.0, ice=0.0, wind=0.0, electro=0.0, fire=0.0, parasite=0.0):
    return {PlantType.DARK: dark, PlantType.ELECTRO: electro, PlantType.FIRE: fire, PlantType.LIGHT: light,
            PlantType.METAL: metal, PlantType.PARASITE: parasite, PlantType.WATER: water, PlantType.WIND: wind,
            PlantType.ICE: ice}


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
    COLD_WAVE = 2
    LOCUSTS_SWARM = 3
    CORONA_MASS_EJECTION = 4
    MAGNETIC_RECONNECTION = 5
    EARTHQUAKE = 6
    MALARIA = 7
    FLOOD = 8

    MOONLIGHT = 9
    MOON_LIGHT = 9

    HEATWAVE = 10
    HEAT_WAVE = 10

    PROTON_STORM = 11
    HURRICANES = 12
    RAINY = 13
    RATS_SWARM = 14
    TORNADO = 15
    SNOWY = 16
    TSUNAMI = 17
    SOLAR_FLARES = 18
    VOLCANO = 19
    SOLAR_MAXIMA = 20
    WINDY = 21
    SUNNY = 22
    WINTER_STORM = 23
    THUNDER_STORM = 24


class Season(Enum):
    SPRING = 0
    SUMMER = 1
    AUTUMN = 2
    WINTER = 3


weatherCloudy = effects(light=-0.1, wind=-0.5)

weatherIronRain = effects(metal=1.2, water=0.4)

weatherColdWave = effects(ice=1.2, fire=-0.6)  # fire -0.6 or -0.4??? Discord says -0.6

weatherLocustSwarm = effects(parasite=1.0)

weatherCoronaMassEjection = effects(light=1.0, fire=0.4)  # light 1.0 or 1.2??? Discord says 1.0

weatherMagneticReconnection = effects(metal=0.5, electro=0.5)

weatherEarthquake = effects(metal=1.0, wind=0.5)

weatherMalaria = effects(parasite=1.0)

weatherFlood = effects(metal=-1.0, water=1.0)

weatherMoonlight = effects(dark=4.0)

# weatherHeatwave = effects(dark=0.1, light=0.2, water=-0.3, ice=-0.6)  # Actual in game weather below
weatherHeatwave = effects(metal=0.1, light=0.2, fire=1.0, water=-0.3, ice=-0.6)

weatherProtonStorm = effects(light=2.0)

weatherHurricanes = effects(dark=0.4, light=-0.2, water=0.5, ice=0.4, wind=0.5, electro=0.5, fire=-0.4)

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

springSeason = {Weather.CLOUDY: weatherCloudy, Weather.EARTHQUAKE: weatherEarthquake,
                Weather.HURRICANES: weatherHurricanes, Weather.IRON_RAIN: weatherIronRain,
                Weather.LOCUSTS_SWARM: weatherLocustSwarm, Weather.MALARIA: weatherMalaria,
                Weather.RAINY: weatherRainy, Weather.RATS_SWARM: weatherRatsSwarm,
                Weather.SUNNY: weatherSunny, Weather.TSUNAMI: weatherTsunami,
                Weather.VOLCANO: weatherVolcano}

summerSeason = {Weather.CLOUDY: weatherCloudy, Weather.CORONA_MASS_EJECTION: weatherCoronaMassEjection,
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

winterSeason = {Weather.COLD_WAVE: weatherColdWave, Weather.CORONA_MASS_EJECTION: weatherCoronaMassEjection,
                Weather.EARTHQUAKE: weatherEarthquake, Weather.MAGNETIC_RECONNECTION: weatherMagneticReconnection,
                Weather.SNOWY: weatherSnowy, Weather.SOLAR_FLARES: weatherSolarFlares,
                Weather.SOLAR_MAXIMA: weatherSolarMaxima, Weather.VOLCANO: weatherVolcano,
                Weather.WINDY: weatherWindy, Weather.WINTER_STORM: weatherWinterStorm}


masterWeather = {Season.SPRING: springSeason, Season.SUMMER: summerSeason, Season.AUTUMN: autumnSeason,
                 Season.WINTER: winterSeason}


def manual_data_input():

    try:
        manSeason = Season[input("Enter current season: ").upper()]
    except KeyError:
        exit("Invalid season. Season can be: Spring, Summer, Autumn or Winter")

    try:
        manWeatherYesterday = Weather[clean_name(input("Enter yesterdays weather: "))]
        manWeatherToday = Weather[clean_name(input("Enter todays weather: "))]
    except KeyError:
        exit("Invalid weather name. If unsure about weather, use \"null\"")

    oldWeather = (manWeatherYesterday, manWeatherToday)

    return manSeason, oldWeather


def auto_data_scraper():
    try:
        print("Starting driver")
        driver = setDriver()
        print("Fetching data")
        driver.get("https://pvuextratools.com/")
        #sleep(1)
        events = driver.find_elements_by_class_name("event")
        w = (Weather[clean_name(events[0].get_attribute("textContent")[7:])],
             Weather[clean_name(events[1].get_attribute("textContent")[7:])])

        seasons = driver.find_elements_by_class_name("season")
        s = Season[clean_name(seasons[2].get_attribute("textContent")[8:])]

    except Exception:
        print("Something went wrong with the automatic fetch...")
        s, w = manual_data_input()

    try:
        driver.quit()
    except Exception:
        pass

    return s, w


def clean_name(name):
    return name.strip().upper().replace(" ", "_")


def get_possible_weather(s, c):
    enumResult = []
    result = []

    for wEnum, weather in masterWeather.get(s).items():
        if wEnum in c:
            continue
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

    if avg < 0:
        recText = "! Greenhouse !"
    elif avg < 0+SAFETY_MARGIN/100:
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

    print("\n   Average Impact: {:.2f}%\n".format((avg*100)))


if __name__ == "__main__":

    if AUTO_ENABLED:
        season, weatherCooldown = auto_data_scraper()
    else:
        season, weatherCooldown = manual_data_input()

    _, weatherList = get_possible_weather(season, weatherCooldown)
    weatherLen = len(weatherList)

    masterData = all_impact_stats(weatherList)

    print("\n\nTomorrows Weather Prediction:\n")

    for ptype, stats in masterData.items():
        printStats(ptype, stats[0], stats[1][0], stats[1][1], weatherLen)



    #input("\nPress enter to exit")
