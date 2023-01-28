class ConditionTrade():
    #====================
    # CONDITION LONG - SHORT
    #====================
    def open_long(row, configuration):
        # entree_long = (last_price < lower[i]) & (rsi[i] < 20) & (kama[i] < last_price)
        if configuration['debug_detail'] == "True":
                print("---------------  open_long  --------------- ")
                print("row['close']:" + str(row['close']) + " row['lower_band']:"+str(row['lower_band'])  )
                print("row['rsi']:"+str(row['rsi'] ))
                print("row['kama']:" + str(row['kama']) + " row['close']:" + str(row['close']) )
           
        if (row['close'] < row['lower_band']):
            if (row['rsi'] < 20 ):
                if (row['kama'] < row['close']):
                    if (configuration['debug_detail'] == "True"):
                        print("True")
                        print("------------------------------------------- ")
                    return True
                else:
                    if configuration['debug_detail'] == "True":
                        print("False")
                        print("------------------------------------------- ")
                    return False
            else:
                if configuration['debug_detail'] == "True":
                    print("False")
                    print("------------------------------------------- ")
                return False
        else:
                if configuration['debug_detail'] == "True":
                    print("False")
                    print("------------------------------------------- ")
                return False

    #sortie_long = (last_price > kama[i])
    def close_long(row, configuration):
        if configuration['debug_detail'] == "True":
                print("---------------  close_long  --------------- ")
                print("row['close']:" + str(row['close']) + " row['kama']:"+str(row['kama'] ) )
       
        if (row['close'] > row['kama']):
            if configuration['debug_detail'] == "True":
                print("True")
                print("------------------------------------------- ")
            return True
        else:
            if configuration['debug_detail'] == "True":
                print("False")
                print("------------------------------------------- ")
            return False

    def open_short(row, configuration):
        #entree_short = (last_price > upper[i]) & (rsi[i] > 20) & (kama[i] > last_price)
        if configuration['debug_detail'] == "True":
                print("---------------  open_short  --------------- ")
                print("row['close'] :" + str(row['close'] ) + " row['higher_band']:"+str(row['higher_band']) )
                print("row['rsi'] :"+str(row['rsi']) ) 
                print("row['kama']:" + str(row['kama']) + " row['close']:" + str(row['close']) )
             
                
        if (row['close'] > row['higher_band'] ):
            if(row['rsi'] > 20) :
                if(row['kama'] > row['close']):
                    if configuration['debug_detail'] == "True":
                            print("True")
                            print("------------------------------------------- ")
                    return True
                else:
                    if configuration['debug_detail'] == "True":
                        print("False")
                        print("------------------------------------------- ")
                    return False
            else:
                if configuration['debug_detail'] == "True":
                    print("False")
                    print("------------------------------------------- ")
                return False
        else:
            if configuration['debug_detail'] == "True":
                print("False")
                print("------------------------------------------- ")
            return False
        
                    
        

    def close_short(row, configuration):
        #sortie_short = (last_price < kama[i])
        if configuration['debug_detail'] == "True":
                print("---------------  close_short  --------------- ")
                print("row['close']:" + str(row['close']) + " row['kama']:"+str(row['kama'] ) )
       
        if (row['close'] < row['kama']):
            return True
        else:
            if configuration['debug_detail'] == "True":
                print("False")
                print("------------------------------------------- ")
            return False
  
        