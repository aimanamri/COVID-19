  
import requests
import pandas as pd
import streamlit as st

st.title('COVID-19 Data Analysis')
@st.cache
def get_data():
    names = list()
    lat_list = list()
    long_list = list()
    cases_num = list()
    total_death = list()
    total_severe = list()
    hospitalize = list()
    age = list()
    gender = list()
    occupation = list
    
    url = 'https://covid19-japan-web-api.now.sh/api//v1/prefectures'
    url2 = 'https://covid19-japan-web-api.now.sh/api//v1/positives'

    api_data = requests.get(url).json()
    api_data2 = requests.get(url2).json()
    print('Total prefectures: ',len(api_data))

    for pref in api_data[0:]:
        id = str(pref['id'])
        nama = f"{pref['name_en']} ({pref['name_ja']})"
        lat = pref['lat']
        lon = pref['lng']
        cases = pref['cases']
        pcr = pref['pcr']
        deaths = pref['deaths']
        severe = pref['severe']
        hosp = pref['hospitalize']

        names.append(nama)
        lat_list.append(lat)
        long_list.append(lon)
        cases_num.append(cases)
        total_death.append(deaths)
        total_severe.append(severe)
        hospitalize.append(hosp)

    # for pref2 in api_data2[0:]:
    #     name_ja = pref2['prefecture']
    #     ag = pref2['age']
    #     gendr = pref2['gender']
    #     occ = pref2['attribute']

    #     names.append(name_ja)
    #     age.append(ag)
    #     gender.append(gendr)
    #     occupation.append(occ)
        
    info = {
        # '#': ids,
        'prefecture':names,
        'lat': lat_list,
        'lon':long_list,
        'total_cases': cases_num,
        'total_death' :total_death,
        'total_severe' : total_severe,
        'hospitalize' : hospitalize,
        # 'age' :  age,
        # 'gender': gender,
        # 'occupation':occupation
    }

    df = pd.DataFrame(data=info)
    return df

df = get_data()
st.subheader('Raw data')
st.write(df)
map_data = df.iloc[:,1:3]
st.map(map_data)