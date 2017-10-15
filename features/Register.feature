Feature: Register

Scenario: Internet User can navigate to /registration page and see registration form
    Given internet user is on start page
    # # I decided to go to registration page manually to check all the natural flow
    When user navigates Pro Packlink
    And user clicks on Register button
    Then user sees the registration form with five fields

Scenario Outline: Internet User can register and begin onboarding process
    Given internet user is on register page
    When user registers with <email> and password
    Then user will land into the onboarding process

    Examples:
     | email                            |
     | testaccount1@abc.io               |
    # | qacandidaeolgak@packlink.es      |
    # | abc@domain.com                   | 123qwerty |
   #  | qacandidatekuratkina@packlink.es |

#145qwerty

