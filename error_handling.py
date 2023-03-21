import logging
import traceback

# Create a logger object
logger = logging.getLogger('binance_trader')
logger.setLevel(logging.ERROR)

# Define a file handler to output the log messages
file_handler = logging.FileHandler('binance_trader.log')
file_handler.setLevel(logging.ERROR)

# Define a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Define custom exception classes for better error handling
class BinanceAPIException(Exception):
    def __init__(self, message):
        self.message = message

class InsufficientFundsException(BinanceAPIException):
    pass

class InvalidOrderTypeException(BinanceAPIException):
    pass

class InvalidOrderException(BinanceAPIException):
    pass

class BinanceConnectionException(Exception):
    def __init__(self, message):
        self.message = message

# Define the error handling function
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BinanceAPIException as e:
            logger.error(f'Binance API Exception: {e.message}')
            print(f'Binance API Exception: {e.message}')
        except InsufficientFundsException as e:
            logger.error(f'Insufficient funds to place order: {e.message}')
            print(f'Insufficient funds to place order: {e.message}')
        except InvalidOrderTypeException as e:
            logger.error(f'Invalid order type: {e.message}')
            print(f'Invalid order type: {e.message}')
        except InvalidOrderException as e:
            logger.error(f'Invalid order: {e.message}')
            print(f'Invalid order: {e.message}')
        except BinanceConnectionException as e:
            logger.error(f'Binance connection error: {e.message}')
            print(f'Binance connection error: {e.message}')
        except Exception:
            logger.error(f'Unexpected error: {traceback.format_exc()}')
            print('An unexpected error occurred. Please check the logs for more details.')
    return wrapper