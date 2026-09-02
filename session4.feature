Feature: Multi-app scenarios

  # 1. Zomato restaurant search with Scenario Outline
  Scenario Outline: Search for restaurants by cuisine
    Given I open the Zomato app
    When I search for cuisine "<cuisine>"
    Then I should see matching restaurant names

    Examples:
      | cuisine  |
      | Italian  |
      | Chinese  |
      | Indian   |

  # 2. Flipkart product search with Background
  Feature: Flipkart product search

  Background:
    Given I launch the browser
    And I navigate to the Flipkart homepage

  Scenario: Search for laptops
    When I enter "Laptop" in the search box
    Then I should see laptop products listed

  Scenario: Search for shoes
    When I enter "Shoes" in the search box
    Then I should see shoe products listed

  # 3. BookMyShow movie booking with Background + Scenario Outline
  Feature: BookMyShow movie booking

  Background:
    Given I open the BookMyShow app
    And I log in with valid credentials

  Scenario Outline: Select seat and make payment
    When I choose seat type "<seat_type>"
    And I pay using "<payment_method>"
    Then I should see booking confirmation for "<seat_type>" with "<payment_method>"

    Examples:
      | seat_type | payment_method |
      | Gold      | Credit Card    |
      | Silver    | UPI            |
      | Platinum  | Net Banking    |

  # 4. Shared search step reuse
  Feature: Shared search functionality

  Scenario: Zomato search reuse
    Given I open the Zomato app
    When I enter "Pizza" in the search box
    Then I should see matching restaurant names

  Scenario: Flipkart search reuse
    Given I launch the browser
    And I navigate to the Flipkart homepage
    When I enter "Mobile" in the search box
    Then I should see mobile products listed
