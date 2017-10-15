Feature: Search

Scenario: Registered client can login and finish onboarding
    Given registered user
#    When user log in for the first time with <email> and <password>
    When user log in for the first time
    Then user will complete the onboarding process

#      Examples:
#     | email                             | password  |
#     | qacandidaeolgak@packlink.es       | 145qwerty |
#     #| abc@domain.com                   | 123qwerty |

Scenario: Registered client can perform the search
    Given registered client logged in
    # # I decided to go to registration page manually to check all the natural flow
    When performing a search with set of details
     | desde    | hasta  | peso  | largo  | ancho   | alto  |
     | Madrid   | Madrid | 1     | 10     | 10      | 10    |
    Then client with choose the first service in the list



