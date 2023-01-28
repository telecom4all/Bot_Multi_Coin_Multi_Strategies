from message_telegram import MessageTelegram
import time

class StopLost():
        
    def put_stop_lost(exchange, configuration, message, type_trade, quantity, price, dfList, coin, pair):
        exchange_config = configuration['exchange_active']
        if(type_trade == "long"):
            pct_sl = float(configuration['sl'])
            pct = (price * pct_sl)
            trigger_price = price - pct
            limit_price = price - pct 
            
            time.sleep(int(configuration['delay_coin'])) 
            print(
                        f"Place Stop Lost Long Limit Order: {quantity} {pair[:-5]} at the price of {price}$ ~{round(quantity, 2)}$"
                    )
            if exchange_config == "BITGET":     
                exchange.place_market_stop_loss(pair, "buy", quantity, trigger_price,  reduce=False)
            if exchange_config == "BINANCE":
                positionSide = "LONG"
                exchange.place_market_stop_loss(pair, "buy", quantity, trigger_price, positionSide, reduce=False)    
            message = MessageTelegram.addMessageComponent(message, f"Place SL for the Long Limit Order: {quantity} {pair[:-5]} at the price of {trigger_price}$ ~{round(quantity, 2)}$\n")
                     
                                    
        if(type_trade == "short"):
            
            pct_sl = float(configuration['sl'])
            pct = (price * pct_sl)
            trigger_price = price + pct
            limit_price = trigger_price + 0.1
            
            time.sleep(int(configuration['delay_coin'])) 
            print(
                        f"Place Stop Lost Short Limit Order: {quantity} {pair[:-5]} at the price of {price}$ ~{round(quantity, 2)}$"
                    )
            
            if exchange_config == "BITGET": 
                exchange.place_market_stop_loss(pair, "sell", quantity, trigger_price, reduce=False)
            if exchange_config == "BINANCE":
                positionSide = "SHORT"
                exchange.place_market_stop_loss(pair, "sell", quantity, trigger_price, positionSide, reduce=False)  
                
            message = MessageTelegram.addMessageComponent(message, f"Place SL for the Short Limit Order: {quantity} {pair[:-5]} at the price of {trigger_price}$ ~{round(quantity, 2)}$\n")
             
        return message
            