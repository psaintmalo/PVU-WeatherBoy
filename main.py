from enum import Enum


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
    HEATWAVE = 10
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

weatherColdWave = effects(ice=1.2, fire=-0.4)

weatherLocustSwarm = effects(parasite=1.0)

weatherCoronaMassEjection = effects(light=1.2, fire=0.4)

weatherMagneticReconnection = effects(metal=0.5, electro=0.5)

weatherEarthquake = effects(metal=1.0, wind=0.5)

weatherMalaria = effects(parasite=1.0)

weatherFlood = effects(metal=-1.0, water=1.0)

weatherMoonlight = effects(dark=4.0)

weatherHeatwave = effects(dark=0.1, light=0.2, water=-0.3, ice=-0.6)

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

weatherThunderStorm = effects(metal=-0.2, dark=1.0, wind=-0.2, water=0.1, electro=1.0)

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


def get_possible_weather(season, cooldown):
    result = []

    for wEnum, weather in masterWeather.get(season).items():
        if wEnum in cooldown:
            continue

        result.append(weather)

    return result


def get_relevant(weatherList, type):
    positiveImpact = []
    negativeImpact = []

    for w in weatherList:
        impact = w.get(type)
        if impact > 0.0:
            positiveImpact.append(impact)
        elif impact < 0.0:
            negativeImpact.append(impact)

    return positiveImpact, negativeImpact


def avg_impact(weatherList, type):
    avg = 0.0
    size = len(weatherList)

    for weather in weatherList:
        effect = weather.get(type)
        avg += effect/size

    return avg


def all_impact_stats(weatherList):

    result = {}

    for type in PlantType:
        posImpact, negImpact = get_relevant(weatherList, type)
        avgImpact = avg_impact(weatherList, type)
        result[type] = [avgImpact, (posImpact, negImpact)]

    return result


def printStats(ptype, avg, pos, neg, weatherLen):
    numOfNegImpact = len(neg)
    numOfPosImpact = len(pos)
    maxBuff = max(pos)*100 if numOfPosImpact > 0 else 0
    maxDebuff = abs(min(neg)*100) if numOfNegImpact > 0 else 0

    print(ptype)
    print("   Probabilities: (+){:.2f}%, (-){:.2f}%, (~){:.2f}%".format(
        (numOfPosImpact/weatherLen)*100, (numOfNegImpact/weatherLen)*100,
        ((weatherLen-(numOfNegImpact+numOfPosImpact))/weatherLen)*100))
    print("   Max Impact: +{:.0f}%, -{:.0f}%".format(maxBuff, maxDebuff))
    print("   Possible Buffs: ", end="")
    for buf in sorted(pos, reverse=True):
        print("+{:.0f}% ".format(buf*100), end="")

    print("\n   Possible Debuffs: ", end="")
    for debuf in sorted(neg):
        print("{:.0f}% ".format(debuf*100), end="")

    print("\n   Average Impact: {:.2f}%\n".format((avg*100)))


if __name__ == "__main__":
    try:
        season = Season[input("Enter current season: ").upper()]
    except KeyError:
        exit("Invalid season. Season can be: Spring, Summer, Autumn or Winter")
    try:
        weatherYesterday = Weather[input("Enter yesterdays weather: ").strip().upper()]
        weatherToday = Weather[input("Enter todays weather: ").strip().replace(" ", "_").upper()]
    except KeyError:
        exit("Invalid weather name. If unsure about yesterdays weather, use \"null\"")

    weatherCooldown = (weatherYesterday, weatherToday)

    weatherList = get_possible_weather(season, weatherCooldown)
    weatherLen = len(weatherList)

    masterData = all_impact_stats(weatherList)

    print("\n\nTomorrows Weather Prediction:\n")

    for ptype, stats in masterData.items():
        printStats(ptype, stats[0], stats[1][0], stats[1][1], weatherLen)
