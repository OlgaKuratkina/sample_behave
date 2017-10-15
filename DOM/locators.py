from collections import namedtuple

# Base Page
base_page_locators = namedtuple('base_page', ['url', 'header_moto', 'navigate_to_pro'])
# Register Pro page
register_page = namedtuple('register_page', ['url', 'register_button', 'login_button'])
register_form = namedtuple('register_form', ['email_field', 'password_field', 'sendings_qty', 'online_shops',
                                             'marketplace_shops', 'phone_field', 'submit_button'])
pro_page = namedtuple('pro_page', ['url'])
login_form = namedtuple('login_form', ['email_field', 'password_field', 'submit_button'])
onboarding_page = namedtuple('onboarding_page', ['next_button', 'logout'])
onboarding_form = namedtuple('onboarding_form', ['name_field', 'last_name_filed', 'postal_code_field',
                                                 'address_field', 'packet_weight', 'packet_length', 'packet_width',
                                                 'packet_height', 'submit_package', 'create_link'])

search_page = namedtuple('seacrh_page', ['create_sending_list', 'create_sending',
                                         'change_address_button', 'new_address_button',
                                         'popover_div', 'predefined_address', 'postal_code',
                                         'package_selector', 'editable_package', 'services_list_buttons',
                                         'service_list', 'sending_details'])

create_sending_page = namedtuple('create_sending_page', ['url', 'header', 'save_button', 'sendings_table',
                                                         'sending_link', 'delete_button'])


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

onboarding_page = onboarding_page(next_button='css=button#btn-welcomenew-next',
                                  logout='xpath=//header//li[3]//span')

pro_page = pro_page('https://pro.packlink.es/')

onboarding_form = onboarding_form(name_field='css=input#sender-name',
                                  last_name_filed='css=input#sender-surname',
                                  postal_code_field='css=input#postalcode',
                                  address_field='css=textarea#address',
                                  packet_weight='css=input#weight',
                                  packet_length='css=input#length',
                                  packet_width='css=input#width',
                                  packet_height='css=input#height',
                                  submit_package='css=button#parcel-form-submit',
                                  create_link='xpath=//section/div/div[2]/a')

search_page = search_page(create_sending_list='xpath=//header/div/nav/span',
                          create_sending='xpath=//header//ul/li[1]',
                          change_address_button='xpath=//*[contains(text(), "Cambiar")]',
                          new_address_button='css=button.eb-select-warehouse__cancel-warehouse-btn ng-binding")',
                          popover_div='css=div.eb-select-warehouse__body',
                          predefined_address='xpath=//div/article/p',
                          postal_code='css=input#postalcodeto',
                          package_selector='xpath=//form/fieldset//span/span[2]/span',
                          editable_package='xpath=//form/fieldset//div[4]//span',
                          service_list='xpath=//service-list/section/article',
                          services_list_buttons='xpath=//service-list/section/article//button',
                          sending_details='xpath=//section/header/h3')


create_sending_page = create_sending_page(url='https://pro.packlink.es/private/shipments',
                                          header='xpath=//article/header',
                                          save_button='xpath=//article/header/button[1]',
                                          sendings_table='xpath=//table/tbody/tr',
                                          sending_link='xpath=//table/tbody//p[1]/span',
                                          delete_button='xpath=//aside/div//button')