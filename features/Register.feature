Feature: Register

Scenario: Internet User can navigate to /registration page and see registration form
    Given internet user is on start page
    # # I decided to go to registration page manually to check all the natural flow
    When user navigates Pro Packlink
    And user clicks on Register button
    Then user sees the registration form with five fields

Scenario: Internet User can navigate to /registration page and see registration form
    Given internet user is on register page
    When user registers with email and random password
    And user clicks on Register button
    Then user sees the registration form with five fields
