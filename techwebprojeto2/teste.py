import requests
import asyncio
api_key = 'RGAPI-6afeac07-f74a-4b7b-a1a9-4b413f99c736'
riot_api = 'https://br1.api.riotgames.com'
summoner_api = riot_api + '/lol/summoner/v4/summoners/by-name/tesujiroqmemame'
summoner = requests.get(summoner_api, headers={'X-Riot-Token': api_key})
encryptedSummonerId = summoner.json()['id']
print(summoner.json())
maestria_api = riot_api + f'/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}'
maestria = requests.get(maestria_api, headers={'X-Riot-Token': api_key})
print(maestria.json())
