Feature: Search

Scenario: Registered client can perform the search
    Given registered client logged in
    # # I decided to go to registration page manually to check all the natural flow
    When performing a search with set of details
     | desde    | hasta  | peso  | largo  | ancho   | alto  |
     | Madrid   | Madrid | 1     | 10     | 10      | 10    |
    Then client with choose the first service in the list



