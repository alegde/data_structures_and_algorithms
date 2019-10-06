import quandl
import pandas as pd

ql.ApiConfig.api_key = 'NyGpUZeLsW4nFTRKJMsf'
my_data = ql.get('EOD/AAPL', start_date='2019-09-02', end_date='2019-09-03')
