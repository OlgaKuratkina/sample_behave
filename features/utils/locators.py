from collections import namedtuple

base_page_locators = namedtuple('base_page', ['url', 'header_moto', 'navigate_to_pro'])
register_page = namedtuple('register_page', ['url', 'register_button'])
register_form = namedtuple('register_form', ['email_field', 'password_field', 'sendings_qty', 'online_shops',
                                             'marketplace_shops', 'phone_field'])

base_page = base_page_locators(url='https://www.packlink.es/',
                               header_moto='css=h2.com-home__hero-moto',
                               navigate_to_pro='css=p.com-searchbox__pro-cta')

register_page = register_page(url='https://pro.packlink.es/registro',
                              register_button='link=Empieza a enviar')

register_form = register_form(email_field='css=input#signUpFormEmail',
                              password_field='css=input#signUpFormPassword',
                              sendings_qty='css=select#signUpFormShipments',
                              online_shops='css=select#signUpFormEcommerce',
                              marketplace_shops='css=select#signUpFormMarketplace',
                              phone_field='css=input#signUpFormPhone')
