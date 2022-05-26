import globals as g, web_modules as wm, alert_modules as am, web_utilities.browser as browser, ascii
import time, importlib

# Represents the products which have already been purchased. This is used to ensure only one specific product will be bought.
purchased = {}

# Represents the state of the product. This is used to 'check' when the product has stock and when it is out of stock. It will be initially set to False.
has_stock = {}

def process_url(driver, url, action):
    '''Notify about stock change by calling the specific alert module.
    
    Arguments:
        - driver: web_utilities.Browser
            Instance of the Browser class that will open the URL and retrieve its HTML.
        - url: str
            Website link where the specific product is being sold.
        - action: str
            Variable used to know what action to take: check stock, buy the product, etc...
    
    Return: 
        - bool
            True if action performed successfully, False otherwise.'''

    specific_module = None

    for module in g.webmodules:
        if url.startswith(module):
            try:
                # Get a specific web_module based on the relationship established in g.webmodules
                specific_module = importlib.import_module('.' + g.webmodules[module], package=wm.__name__)

                # Call the action related method of the specific web_module
                return getattr(specific_module, action)(driver, url)

            except ModuleNotFoundError:
                print('[!!] Error: web_module "' + g.webmodules[module] + '" could not be found\n')
                return False
            except AttributeError:
                print('[!!] Error: web_module "' + g.webmodules[module] + '" has no method for the "' + action + '" action\n')
                return False

    if specific_module is None:
        print('[!!] Error: no web_module exists for "' + url + '"\n')
        return False

def alert(url, action, state):
    '''Notify about stock change by calling the specific alert module.
    
    Arguments:
        - url: str
            Website link where the specific product is being sold.
        - action: str
            Variable used to alert if the product stock has been checked or purchased.
        - state: bool
            Variable used to keep track of changes in product stock.
    
    Return: None'''

    specific_module = None

    for module in g.alertmodules:
        if module == action:
            try:
                # Get a specific alert_module based on the relationship established in g.alertmodules
                specific_module = importlib.import_module('.' + g.alertmodules[module], package=am.__name__)

                # Call the action related method of the specific alert_module
                getattr(specific_module, action)(url, state)

            except ModuleNotFoundError:
                print('[!!] Error: alert_module "' + g.alertmodules[module] + '" could not be found\n')
            except AttributeError:
                print('[!!] Error: alert_module "' + g.alertmodules[module] + '" has no "' + action + '" method\n')

    if specific_module is None:
        print('[!!] Error: no alert_module exists for "' + action + '"\n')

def execute():
    '''Main loop of the bot, it processes all URLs based on the action specified and alerts the user of any changes. 
    It finishes when all the products with distinct ID have been purchased.
    
    Arguments: None
    
    Return: None'''

    all_purchased = False

    driver = browser.Browser()

    try:
        while not all_purchased:
            all_purchased = False

            time.sleep(g.time_interval)

            for product in g.product_list:
                product_id = product[0]
                url = product[1]
                action = product[2]

                if not purchased[product_id]:
                    driver.start_driver()
                    result = process_url(driver, url, action)

                    if has_stock[url] is not result:
                        purchased[product_id] = action == 'buy'
                        has_stock[url] = result
                        alert(url, action, result)
                    
                    driver.stop_driver()

            for purchased_product in purchased:
                all_purchased = all_purchased and purchased_product
    except KeyboardInterrupt:
        print('\n[!!] Stopping execution...\n')
    
    del driver

def init():
    '''Initialize variables before the main execution of the bot.
    
    Arguments: None
    
    Return: None'''

    g.init_globals()
    ascii.print_ascii_title()

    if not hasattr(g, 'product_list') or g.product_list is None or len(g.product_list) <= 0:
        print('[!!] Error: product_list must be initialized with some product URLs\n')
        return False

    if not hasattr(g, 'time_interval') or g.time_interval is None or g.time_interval < 0:
        print('[!!] Error: time_interval must be set to a number larger than or equal to 0\n')
        return False

    for product in g.product_list:
        # Initially set all the products as not purchased and set the stock state of all urls as False
        product_id = product[0]
        url = product[1]
        purchased[product_id] = False
        has_stock[url] = False

    return True

def main():
    if init():
        execute()

if __name__ == '__main__':
    main()
