import time
from oura import OURA
from atom import ATOM

if __name__ == '__main__':
    atom = ATOM()
    oura = OURA()
    params ={ 
            'start_datetime': '2023-03-18T10:00:00+09:00',
            'end_datetime': '2023-03-18T12:00:00+09:00'
            }
    oura.set_params(params=params)
    df_pre = None
    while True:
        print('start')
        df = oura.get_pd()
        if df is None:
            print('none')
            pass
        elif df.empty is False and df.equals(df_pre) is False:
            print('new data incoming')
            df_pre = df
            name_oura = 'oura_HR_'+ atom.get_now()+'.csv'
            df.to_csv('./'+name_oura,index=False)
            print(df.iloc[-1])

        time.sleep(15)
