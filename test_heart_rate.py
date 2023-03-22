from oura import OURA
from atom import ATOM

if __name__ == '__main__':
    atom = ATOM()
    oura = OURA()
    params = {
            'start_datetime': '2023-02-22T10:00:00+09:00',
            'end_datetime': '2023-03-22T00:00:00+09:00'
            }
    oura.set_params(params=params)
    df = oura.get_pd()
    name_oura = 'oura_HR_' +  atom.get_now() + '.csv'
    df.to_csv('./' + name_oura, index=False)
    print(df)
    print('data acquired')
