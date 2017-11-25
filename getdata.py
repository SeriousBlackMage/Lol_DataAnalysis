from riotwatcher import RiotWatcher
import csv
import numpy as np
import pandas as pd

class DataScraper:

    def __init__(self, apikey):
        self.watcher = RiotWatcher(apikey)
        self.currentData = {}

    def getSummonerDataByName(self, region, name):
        data = self.watcher.summoner.by_name(region,name)
        self.currentData[name] = {'id':data['id'],'name':data['name'],'summonerLevel':data['summonerLevel']}

    def getMatchData(self,name,region):
        data = {}
        matchHistory = self.watcher.match.matchlist_by_account(region,self.watcher.summoner.by_name(region,name)['accountId'])
        for i in matchHistory['matches']:
            matchInfo = self.watcher.match.by_id(region,i['gameId'])
            playerIdentity = matchInfo['participantIdentities']
            for j in matchInfo['participantIdentities']:
                if j['player']['summonerName'] == name:
                    partID = j['participantId']
                    for z in matchInfo['participants']:
                        if(z['participantId']==partID):
                            data[i['gameId']] = {'PhysicalDmgDealt':z['stats']['physicalDamageDealt'], 'MagicDamageDealt':z['stats']['magicDamageDealt']}
        return data

    def average(self,name,region):
        uData = self.getMatchData(name,region)
        phDmgSum = sum(b['PhysicalDmgDealt'] for a, b in uData.items())
        mgDmgSum = sum(b['MagicDamageDealt'] for a, b in uData.items())
        rData = {'PhysicalDamage':(phDmgSum/len(uData)),'MagicalDamage':(mgDmgSum/len(uData))}
        return rData


    def printInfoName(self,name):
        if name in self.currentData:
            for i in self.currentData[name]:
                print(i,":",self.currentData[name][i])
        else: print("Noch keine Daten")

    def printData(self):
        for i in self.currentData:
            for j in self.currentData[i]:
                print(j,":",self.currentData[i][j])
            print("")


#def main():
 #   root = DataScraper('RGAPI-a444d470-72a1-47c7-9b4a-52acf6674e64')
  #  root.average("ArtusTheSecond",'euw1')
   # while True:
    #    ui = str(input("Summonername eingeben oder exit[e]"))
     #   if ui == 'e': break
      #  else: root.getSummonerDataByName('euw1',ui)
    #####root.printData()



#main()
