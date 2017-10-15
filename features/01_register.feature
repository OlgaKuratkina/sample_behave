Feature: Register

Scenario: Internet User can navigate to /registration page and see registration form
    Given internet user is on start page
    # # I decided to go to registration page manually to check all the natural flow
    When user navigates Pro Packlink
    And user clicks on Register button
    Then user sees the registration form with five fields

Scenario Outline: Internet User can register with email and random password and land to onboarding
    Given internet user is on register page
    When user registers with <email> and password
    Then user will land into the onboarding process

    Examples:
     | email                            |
    # | qacandidaeolgak@packlink.es      |
      | testabc6@domain.com               |
   #  | qacandidatekuratkina@packlink.es |

 Scenario: Registered client can login and finish onboarding
    Given registered user
    When user log in for the first time
    Then user will complete the onboarding process


