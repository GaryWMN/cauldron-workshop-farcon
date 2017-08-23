import cauldron as cd
import pandas as pd
import requests
import io
import string

url_prefix = 'https://s3-us-west-2.amazonaws.com/cauldron-workshop/data'

data_frames = []

for character in string.ascii_lowercase:
    response = requests.get('{}/{}.csv'.format(url_prefix, character))
    data = response.text
    buffer = io.StringIO(data)
    data_frames.append(pd.read_csv(buffer))

df = pd.concat(data_frames) #Python 2.4
# df: pd.DataFrame = pd.concat(data_frames) #Python 3.6 (adds typing)
# df = df.sort_values(by='user_id') # to see different data in head

cd.display.table(df.head(100))
