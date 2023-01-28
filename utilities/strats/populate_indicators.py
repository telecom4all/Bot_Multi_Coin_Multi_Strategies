import time
from custom_indicators import CustomIndocators
import ta

class DataIndicators():
    def populate_indicator(configuration, dfList):
        strat_active = configuration['strat_active']
        if strat_active == "BOLLINGER":
            return DataIndicators.populate_bollinger(configuration, dfList)   
        if strat_active == "RANGE_1":
            return DataIndicators.populate_range_1(configuration, dfList)    
        
    
    
    def populate_bollinger(configuration, dfList):
        for coin in dfList:
            #print("test")
            # -- Drop all columns we do not need --
            if configuration['debug'] == "True":
                print("Get Indicator for : " + coin)
            
            dfList[coin].drop(columns=dfList[coin].columns.difference(['open','high','low','close','volume']), inplace=True)

            dfList[coin].drop(columns=dfList[coin].columns.difference(['open','high','low','close','volume']), inplace=True)
            bol_band = ta.volatility.BollingerBands(close=dfList[coin]["close"], window=int(configuration['bol_window']), window_dev=float(configuration['bol_std']))
            dfList[coin]["lower_band"] = bol_band.bollinger_lband()
            dfList[coin]["higher_band"] = bol_band.bollinger_hband()
            dfList[coin]["ma_band"] = bol_band.bollinger_mavg()

            dfList[coin]['long_ma'] = ta.trend.sma_indicator(close=dfList[coin]['close'], window=int(configuration['long_ma_window']))

            dfList[coin] = CustomIndocators.get_n_columns(dfList[coin], ["ma_band", "lower_band", "higher_band", "close"], 1)
            
            
        return dfList
    
    def populate_range_1(configuration, dfList):
        for coin in dfList:
            #print("test")
            # -- Drop all columns we do not need --
            if configuration['debug'] == "True":
                print("Get Indicator for : " + coin)
            
            dfList[coin].drop(columns=dfList[coin].columns.difference(['open','high','low','close','volume']), inplace=True)

            dfList[coin].drop(columns=dfList[coin].columns.difference(['open','high','low','close','volume']), inplace=True)
            
            bol_band = ta.volatility.BollingerBands(close=dfList[coin]["close"], window=int(configuration['bol_window']), window_dev=float(configuration['bol_std']))
            dfList[coin]["lower_band"] = bol_band.bollinger_lband()
            dfList[coin]["higher_band"] = bol_band.bollinger_hband()
            dfList[coin]["ma_band"] = bol_band.bollinger_mavg()

            kama_windows = int(configuration['kama_windows'])
            kama_pow1 = int(configuration['kama_pow1'])
            kama_pow2 = int(configuration['kama_pow2'])
            dfList[coin]['kama'] = ta.momentum.kama(dfList[coin]['close'], window=kama_windows, pow1=kama_pow1, pow2=kama_pow2)
            
            rsi_windows = int(configuration['rsi_windows'])
            dfList[coin]['rsi'] = ta.momentum.rsi(dfList[coin]['close'], window=rsi_windows, fillna=False) 
            dfList[coin] = CustomIndocators.get_n_columns(dfList[coin], ["ma_band", "lower_band", "higher_band", "close"], 1)
            
            
        return dfList
