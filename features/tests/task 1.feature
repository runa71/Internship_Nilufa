# Created by nilufayesmin at 10/19/23

  Feature: Filter by sale status with Out of Stocks tag

   Scenario: User can filter by sale status Out of Stocks

    Given Open the main page
    When Log in to the page
    And Click on off plan at the left side menu
    And Verify the right page opens
    And Filter by sale status of Out of Stocks
    Then Vergirify each product contains the Out of Stocks tag