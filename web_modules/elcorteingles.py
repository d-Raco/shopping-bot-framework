from bs4 import BeautifulSoup

def check(driver, url):
    '''Check the availability of an ElCorteInglés product by opening its URL and parsing the website contents.
    
    Arguments:
        - driver: web_utilities.Browser
            Instance of the Browser class that will open the URL and retrieve its HTML.
        - url: str
            Website link where the specific product is being sold.
    
    Return: 
        - bool
            True if there is stock, False otherwise.'''

    html = BeautifulSoup(driver.get_html_delayed(url, 5), 'html.parser')

    single_product = html.find_all('div', {'id' : 'product-detail-container'})

    if len(single_product) != 0:
        buttons = html.find_all('button', {'id' : 'js_add_to_cart_desktop'})

        for b in buttons:
            if b.has_attr('class'):
                for att in b['class']:
                    if att == '_enabled':
                        return True
    else:
        divs = html.find_all('span', {'class' : 'js-currency'})

        if len(divs) != 0:
            return True

    return False

def buy(driver, url):
    if not check(driver, url):
        return False
        
    # To do
    return True
