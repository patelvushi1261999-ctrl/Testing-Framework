Feature: Multiple app scenarios

  # 1. Zomato-style restaurant search
  Scenario: Search for Italian cuisine
    Given I open the Zomato app
    When I search for cuisine "Italian"
    Then I should see matching restaurant names

  # 2. Movie rating with parse step parser
  Scenario: Rate a movie
    When I rate the movie "Pathaan" as 4 stars

  # 3. Flipkart-style product filter with regex parser
  Scenario: Filter products by category and price
    When I filter category "Electronics" with price range "10000-20000"

  # 4. BookMyShow ticket booking with fixture
  Scenario: Book a movie ticket
    Given I select the movie "Inception"
    Then I should see booking confirmation

  # 5. WhatsApp-like message sending feature
  Scenario: Send a WhatsApp message
    When I send a message "Hello, how are you?" to contact "Rahul"
