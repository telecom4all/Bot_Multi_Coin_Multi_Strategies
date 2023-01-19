import time

class UtilitiesBot():
    def get_open_position(exchange, configuration):
        coinPositionList = []

        try :
            coinPositionList = exchange.get_open_position()
            time.sleep(int(configuration['delay_coin']))
            
        except Exception as e:
            print("ERROR : "+str(e))
        
        openPositions = len(coinPositionList)
        return openPositions
    
    def cancel_order_open(exchange, configuration, pair):
        open_order =  exchange.get_open_order(pair)
        if len(open_order) > 0:
            for order in open_order:
                exchange.cancel_order_by_id(order['info']['orderId'], pair)
        