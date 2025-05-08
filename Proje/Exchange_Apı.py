import requests
import json

api_key = "26acb9d5271a79a714e32e00"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_döviz = input("Bozulan döviz türü: ").upper()
alınan_döviz = input("Alınan döviz türü: ").upper()
miktar = int(input(f"Ne kadat {bozulan_döviz} bozdurmak istiyorsunuz? "))

result = requests.get(api_url + bozulan_döviz)
result_json = json.loads(result.text)
print(f"{miktar} {bozulan_döviz} = {result_json["conversion_rates"][alınan_döviz] * miktar} {alınan_döviz}")