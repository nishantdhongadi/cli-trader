import robin_stocks.robinhood as rh


def login(username, password):
   
    """Login to Robinhood"""
   
    try:
        rh.login(username, password)
        return True
    except Exception as e:
        print(f"Error logging in: {e}")
        return False


def buy_crypto(symbol, amount):
    
    """Buy cryptocurrency"""
    
    try:
        result = rh.orders.order_crypto(symbol, amount, 'buy')
        return f"Bought {amount} of {symbol}"
    except Exception as e:
        return f"Error buying crypto: {e}"


def sell_crypto(symbol, amount):
    
    """Sell cryptocurrency"""
    
    try:
        result = rh.orders.order_crypto(symbol, amount, 'sell')
        return f"Sold {amount} of {symbol}"
    except Exception as e:
        return f"Error selling crypto: {e}"


def check_balance():
    
    """Check account balance"""
    
    try:
        balance = rh.profiles.load_account_profile()
        return balance
    except Exception as e:
        return f"Error checking balance: {e}"
