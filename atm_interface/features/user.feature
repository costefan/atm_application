Feature: Login for site

  Scenario: Show form with keyboard
    Given unlogged user by card number
    When I visit home page
    Then I should see keyboard with input

  Scenario: Logging with wrong data
    Given unlogged user by card number
    When I gave not valid data
    Then I should see login form and see error message

  Scenario: Logging in to our system
    Given unlogged user by card number
    When I gave valid data
    Then I should see pin page