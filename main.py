from pyramid.config import Configurator
from cornice import Service

QUOTES = Service(name="quotes",
                path="/",
                description="Get quotes")

@QUOTES.get()
def get_quote(request):
    return {
        "William Shakespeare": {
            "quote": ['Love all, trust a few, do wrong to none',
                      'Some are born great, some achieve greatness, and some have greatness thrust upon themselves.']
            },
        "Linus": {
            "quote": ['Talk is cheap. Show me the code.']
            }
        }
    
with Configurator() as config:
    config.include('cornice')
    config.scan()
    application = config.make_wsgi_app()