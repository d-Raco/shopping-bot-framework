def check(url, state):
    '''Print the availability of a product alongside its URL.
    
    Arguments:
        - url: str
            Website link where the specific product is being sold.
        - state: bool
            Variable used to keep track of changes in product stock.
    
    Return: None'''

    if state:
        print('[++] Available stock: ' + url + '\n')
    else:
        print('[--] Unavailable stock: ' + url + '\n')

def buy(url, state):
    '''Print if a product has been bought alongside its URL.
    
    Arguments:
        - url: str
            Website link where the specific product is being sold.
        - state: bool
            Variable used to keep track of changes in product stock.
    
    Return: None'''

    print('[++] Product purchased: ' + url + '\n')
