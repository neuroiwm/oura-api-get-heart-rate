import requests
import pandas as pd


class OURA():
    def __init__(self):
        self.url = 'https://api.ouraring.com/v2/usercollection/heartrate' 
        self.params={ 
            'start_datetime': '2023-02-1T00:00:00-08:00', 
            'end_datetime': '2023-02-22T00:00:00-08:00' 
            }
        self.headers = { 
            'Authorization': 'INSERT TOKEN HERE' }

    def set_params(self,params):
        self.params = params

    def get_data(self):
        response = requests.request('GET', self.url, headers=self.headers, params=self.params) 
        response_json = response.json()
        if len(response_json) == 1:
            bpms = None
            timestamp = None
            source = None
        else:
            bpms = [i['bpm'] for i in response_json['data']]
            timestamp = [i['timestamp'] for i in response_json['data']]
            source = [i['source'] for i in response_json['data']]

        return bpms, timestamp, source

    def get_pd(self):
        bpms, timestamp, source = self.get_data()
        if bpms is None:
            df = None
        else:
            df = pd.DataFrame(list(zip(timestamp,bpms,source)), columns = ['Time','BPM','State'])
        return df
