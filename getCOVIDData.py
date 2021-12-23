# Import required packages
import pandas as pd
import time
import requests

###################################################################################################################################

# Defines a function to get all the data and export to CSV
def get_data():

    # Get Japan COVID data from API
    ids = list()
    name = list()
    location = list()
    cases_num = list()
    total_death = list()
    total_severe = list()
    hospitalize = list()
    
    url = 'https://covid19-japan-web-api.now.sh/api//v1/prefectures'
    api_data = requests.get(url).json()
    # print('Total prefectures: ',len(api_data))
    
    # Put API responses into lists
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
    
    # Create a dictionary from the lists above.
    data = {
        '#': ids,
        'prefecture':name,
        'location': location,
        'total_cases': cases_num,
        'total_death' :total_death,
        'total_severe' : total_severe,
        'hospitalize' : hospitalize
    }
    
    # Create a dataframe from the dictionary above
    df = pd.DataFrame(data=data)
    #Export to CSV file
    df.to_csv(r'B:\COVID-19-Analysis\covid19_japan_data.csv',index=False,header=True)
    print('Data saved to CSV file (Japan)')
    
    ###################################################################################################################################
    # Get Malaysia COVID data from API
    url2="https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"
    df2=pd.read_csv(url2)
    df2['date'] = pd.to_datetime(df2['date'], infer_datetime_format=True, errors='coerce') # Change date column to datetime format

    # Filtered date in df2
    df2 = df2[df2['date'] >= pd.to_datetime('2021-01-01')]
    #Export to CSV file
    df2.to_csv(r'B:\COVID-19-Analysis\cases_msia_2021.csv', index = False)
    print('Data saved to CSV file (Malaysia)')
    time.sleep(5)

get_data() # Will output 2 CSV files to specified path
