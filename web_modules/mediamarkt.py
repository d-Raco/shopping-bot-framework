from bs4 import BeautifulSoup

def check(driver, url):
    '''Check the availability of an MediaMarkt product by opening its URL and parsing the website contents.
    
    Arguments:
        - driver: web_utilities.Browser
            Instance of the Browser class that will open the URL and retrieve its HTML.
        - url: str
            Website link where the specific product is being sold.
    
    Return: 
        - bool
            True if there is stock, False otherwise.'''

    html = BeautifulSoup(driver.get_html(url), 'html.parser')
    buttons = html.find_all('button')

    for b in buttons:
        if b.has_attr('id') and not b.has_attr('disabled'):
            if b['id'] == 'pdp-add-to-cart-button' or b['id'] == 'AddToCart':
                return True
    
    return False

def buy(driver, url):
    if not check(driver, url):
        return False
        
    # To do
    return True