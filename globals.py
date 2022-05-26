def init_globals():
    ''' Initialize some user specific global variables used by the shopping bot's modules.
    
    Arguments: None

    Return: None'''

    # Time interval in seconds that the bot will wait to check the stock again.
    global time_interval
    time_interval = 60 * 3

    # List of web modules to be used based on the domain name of the online store.
    global webmodules
    webmodules = {
        'https://www.amazon': 'amazon',
        'https://www.elcorteingles': 'elcorteingles',
        'https://www.fnac': 'fnac',
        'https://www.mediamarkt': 'mediamarkt',
        'https://www.pccomponentes': 'pccomponentes',
        'https://www.worten': 'worten'
    }

    # List of alert modules to be used per action.
    global alertmodules
    alertmodules = {
        'check': 'simple_print',
        'buy': 'open_url'
    }

    # List of URLs to check. Depending on the domain name, the specific module will be callled by the bot.
    # The list is made up of tuples:
    #   - The first element is an index that identifies a specific product. This is used to check multiple products at once.
    #   - The second element is a URL where the specific product is sold.
    #   - The third element of the tuple is the action to perform. The 'buy' action buys the product, and 'check' action only checks if the specific product is in stock. If a specific product is purchased on one domain, that product will not be purchased or checked on any of the other domains in the list.
    global product_list
    product_list = [
        (0, 'https://www.mediamarkt.es/es/product/_consola-sony-ps5-825-gb-4k-hdr-blanco-1487016.html', 'check'),
        (0, 'https://www.elcorteingles.es/videojuegos/A37046604-consola-playstation-5/', 'check'),
        (0, 'https://www.elcorteingles.es/videojuegos/ps5/consolas/', 'check'),
        (0, 'https://www.amazon.es/Sony-PlayStation-Consola-5/dp/B08H93ZRK9/', 'check'),
        (0, 'https://www.worten.es/productos/consolas-juegos/playstation/consola/ps5/consola-ps5-825gb-7196053', 'check'),
        (0, 'https://www.fnac.es/Consola-PlayStation-5-Videoconsola-Consola/a7724798', 'check'),
        (0, 'https://www.fnac.es/n127487/Playstation/Consolas-PS5', 'check'),
        (0, 'https://www.pccomponentes.com/sony-playstation-5', 'check'),
        (0, 'https://www.playstation.com/es-es/ps5/buy-now/', 'check')
    ]
