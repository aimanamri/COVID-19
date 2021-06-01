  
import requests
import pandas as pd

def get_data():
    ids = list()
    name = list()
    location = list()
    cases_num = list()
    total_death = list()
    total_severe = list()
    hospitalize = list()
    
    url = 'https://covid19-japan-web-api.now.sh/api//v1/prefectures'
    api_data = requests.get(url).json()
    print('Total prefectures: ',len(api_data))

    for pref in api_data[0:]:
        id = str(pref['id'])
        name_en = pref['name_en']
        loc = (pref['lat'],pref['lng'])
        cases = pref['cases']
        pcr = pref['pcr']
        deaths = pref['deaths']
        severe = pref['severe']
        hosp = pref['hospitalize']

        ids.append(id)
        name.append(name_en)
        location.append(loc)
        cases_num.append(cases)
        total_death.append(deaths)
        total_severe.append(severe)
        hospitalize.append(hosp)

    data = {
        '#': ids,
        'prefecture':name,
        'location': location,
        'total_cases': cases_num,
        'total_death' :total_death,
        'total_severe' : total_severe,
        'hospitalize' : hospitalize
    }

    df = pd.DataFrame(data=data)
    df.to_csv('covid19_japan_data.csv',index=False,header=True)


if __name__ == '__main__':
    get_data()