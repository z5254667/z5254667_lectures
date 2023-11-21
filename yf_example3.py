""" yf_example3.py

Week 4: Quizzes and code challenges submission
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file

    Parameters
    ----------
    year : int
        The year for which the stock price time series will be downloaded.

    """

    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    start = f'{year}-01-01'
    end = f'{year}-12-31'

    yf_example2.yf_prc_to_csv(tic, pth, start, end)

if __name__ == '__main__':
    year = 2020

    qan_prc_to_csv(year)
