from collections import namedtuple

# Base Page
base_page_locators = namedtuple('base_page', ['url', 'header_moto', 'navigate_to_pro'])
# Register Pro page
register_page = namedtuple('register_page', ['url', 'register_button', 'login_button'])
register_form = namedtuple('register_form', ['email_field', 'password_field', 'sendings_qty', 'online_shops',
                                             'marketplace_shops', 'phone_field', 'submit_button'])
login_form = namedtuple('login_form', ['email_field', 'password_field', 'submit_button'])
onboarding_page = namedtuple('onboarding_page', ['next_button'])
onboarding_form = namedtuple('onboarding_form', ['name_field', 'last_name_filed', 'postal_code_field',
                                                                                  'address_field'])


base_page = base_page_locators(url='https://www.packlink.es/',
                               header_moto='css=h2.com-home__hero-moto',
                               navigate_to_pro='css=p.com-searchbox__pro-cta')

register_page = register_page(url='https://pro.packlink.es/registro',
                              register_button='link=Empieza a enviar',
                              login_button='link=Acceder')

register_form = register_form(email_field='css=input#signUpFormEmail',
                              password_field='css=input#signUpFormPassword',
                              sendings_qty='css=select#signUpFormShipments',
                              online_shops='css=select#signUpFormEcommerce',
                              marketplace_shops='css=select#signUpFormMarketplace',
                              phone_field='css=input#signUpFormPhone',
                              submit_button='css=button.button--primary h-mt-m')

login_form = login_form(email_field='css=input#signInFormUser',
                        password_field='css=input#signInFormPassword',
                        submit_button='css=button#signInFormButton')

onboarding_page = onboarding_page(next_button='css=button#btn-welcomenew-next')

onboarding_form = onboarding_form(name_field='css=input#sender-name',
                                  last_name_filed='css=input#sender-surname',
                                  postal_code_field='css=input#postalcode',
                                  address_field='css=textarea#address')
