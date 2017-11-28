from riotwatcher import RiotWatcher
import csv
import numpy as np
import pandas as pd

class DataScraper:
    # TODO make it Faster ._.
    def __init__(self, apikey):
        self.watcher = RiotWatcher(apikey)
        self.chNames = {
            516: "Ornn",
            164: "Camille",
            497: "Rakan",
            498: "Xayah",
            141: "Kayn",
            266: "Aatrox",
            412: "Thresh",
            23: "Tryndamere",
            79: "Gragas",
            69: "Cassiopeia",
            136: "Aurelion Sol",
            13: "Ryze",
            78: "Poppy",
            14: "Sion",
            1: "Annie",
            202: "Jhin",
            43: "Karma",
            111: "Nautilus",
            240: "Kled",
            99: "Lux",
            103: "Ahri",
            2: "Olaf",
            112: "Viktor",
            34: "Anivia",
            27: "Singed",
            86: "Garen",
            127: "Lissandra",
            57: "Maokai",
            25: "Morgana",
            28: "Evelynn",
            105: "Fizz",
            74: "Heimerdinger",
            238: "Zed",
            68: "Rumble",
            82: "Mordekaiser",
            37: "Sona",
            96: "Kog'Maw",
            55: "Katarina",
            117: "Lulu",
            22: "Ashe",
            30: "Karthus",
            12: "Alistar",
            122: "Darius",
            67: "Vayne",
            110: "Varus",
            77: "Udyr",
            89: "Leona",
            126: "Jayce",
            134: "Syndra",
            80: "Pantheon",
            92: "Riven",
            121: "Kha'Zix",
            42: "Corki",
            268: "Azir",
            51: "Caitlyn",
            76: "Nidalee",
            85: "Kennen",
            3: "Galio",
            45: "Veigar",
            432: "Bard",
            150: "Gnar",
            90: "Malzahar",
            104: "Graves",
            254: "Vi",
            10: "Kayle",
            39: "Irelia",
            64: "Lee Sin",
            420: "Illaoi",
            60: "Elise",
            106: "Volibear",
            20: "Nunu",
            4: "Twisted Fate",
            24: "Jax",
            102: "Shyvana",
            429: "Kalista",
            36: "Dr. Mundo",
            427: "Ivern",
            131: "Diana",
            223: "Tahm Kench",
            63: "Brand",
            113: "Sejuani",
            8: "Vladimir",
            154: "Zac",
            421: "Rek'Sai",
            133: "Quinn",
            84: "Akali",
            163: "Taliyah",
            18: "Tristana",
            120: "Hecarim",
            15: "Sivir",
            236: "Lucian",
            107: "Rengar",
            19: "Warwick",
            72: "Skarner",
            54: "Malphite",
            157: "Yasuo",
            101: "Xerath",
            17: "Teemo",
            75: "Nasus",
            58: "Renekton",
            119: "Draven",
            35: "Shaco",
            50: "Swain",
            91: "Talon",
            40: "Janna",
            115: "Ziggs",
            245: "Ekko",
            61: "Orianna",
            114: "Fiora",
            9: "Fiddlesticks",
            31: "Cho'Gath",
            33: "Rammus",
            7: "LeBlanc",
            16: "Soraka",
            26: "Zilean",
            56: "Nocturne",
            222: "Jinx",
            83: "Yorick",
            6: "Urgot",
            203: "Kindred",
            21: "Miss Fortune",
            62: "Wukong",
            53: "Blitzcrank",
            98: "Shen",
            201: "Braum",
            5: "Xin Zhao",
            29: "Twitch",
            11: "Master Yi",
            44: "Taric",
            32: "Amumu",
            41: "Gangplank",
            48: "Trundle",
            38: "Kassadin",
            161: "Vel'Koz",
            143: "Zyra",
            267: "Nami",
            59: "Jarvan IV",
            81: "Ezreal"
        }

    def getSummonerDataByName(self, region, name):
        data = self.watcher.summoner.by_name(region,name)
        self.currentData[name] = {'id':data['id'],'name':data['name'],'summonerLevel':data['summonerLevel']}

    def getMatchData(
            self,name,region,win=False,deaths=False,totalDamage=False,physicalDamage=False,magicDamage=False,
            wardsPlaced=False,visionScore=False,goldEarned=False,kills=False,cs=False,pentaKills=False,gameCount=False,
            totalDamagetaken=False
    ):
        data = {}
        matchHistory = self.watcher.match.matchlist_by_account(region,self.watcher.summoner.by_name(region,name)['accountId'])
        matchInf = self.watcher.match.by_id
        targetID = self.watcher.summoner.by_name(region,name)['accountId']
        for i in matchHistory['matches']:
            matchInfo = matchInf(region,i['gameId'])
            for j in matchInfo['participantIdentities']:
                if j['player']['accountId'] == targetID:
                    partID = j['participantId']
                    for z in matchInfo['participants']:
                        if(z['participantId']==partID):
                            data[i['gameId']] = {}#{'PhysicalDmgDealt':z['stats']['physicalDamageDealt'], 'MagicDamageDealt':z['stats']['magicDamageDealt']}
                            if(win): data[i['gameId']]['win'] = z['stats']['win']
                            if(deaths): data[i['gameId']]['deaths'] = z['stats']['deaths']
                            if(totalDamage): data[i['gameId']]['totalDamage'] = z['stats']['totalDamageDealt']
                            if(physicalDamage): data[i['gameId']]['physicalDamage'] = z['stats']['physicalDamageDealt']
                            if(magicDamage): data[i['gameId']]['magicDamage'] = z['stats']['magicDamageDealt']
                            if(wardsPlaced): data[i['gameId']]['wardsPlaced'] = z['stats']['wardsPlaced']
                            if(visionScore): data[i['gameId']]['visionScore'] = z['stats']['visionScore']
                            if(goldEarned): data[i['gameId']]['goldEarned'] = z['stats']['goldEarned']
                            if(kills): data[i['gameId']]['kills'] = z['stats']['kills']
                            if(cs): data[i['gameId']]['cs'] = z['stats']['neutralMinionsKilled']
                            if(pentaKills): data[i['gameId']]['pentaKills'] = z['stats']['pentaKills']
                            if(totalDamagetaken): data[i['gameId']]['totalDamageTaken'] = z['stats']['totalDamageTaken']
        if(gameCount): data['GameCount'] = matchHistory['totalGames']
        return data

    def average(self,name,region):
        uData = self.getMatchData(name,region)
        rData = {}

        return {
            'PhysicalDamage':(sum(b['PhysicalDmgDealt'] for a, b in uData.items())/len(uData))
            ,'MagicalDamage':(sum(b['MagicDamageDealt'] for a, b in uData.items())/len(uData))
        }


if __name__ == '__main__':
    root = DataScraper('RGAPI-1d3d34c6-5a35-48f7-bdc4-15b5e3a5af54')
    mainData = root.getMatchData("an3craft",'euw1',deaths=True,kills=True,cs=True,pentaKills=True)

