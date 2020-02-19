
Feature: Payment authorizations

  Scenario: No matching policy
    Given policy for user Chewbecca with benefit dentist for max total amount of 500 USD
    When a payment is received from Chewbecca for benefit candies with amount 10 USD
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_NOT_FOUND

    When a payment is received from Chewbecca for benefit dentist with amount 10 GBP
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_NOT_FOUND

    When a payment is received from Yoda for benefit dentist with amount 10 USD
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_NOT_FOUND
    
  Scenario: Matching policy
    Given policy for user R2-D2 with benefit maintenance for max total amount of 200 GBP
    When a payment is received from R2-D2 for benefit maintenance with amount 120 GBP
    Then the payment was successful
    When a payment is received from R2-D2 for benefit maintenance with amount 70 GBP
    Then the payment was successful
    When a payment is received from R2-D2 for benefit maintenance with amount 20 GBP
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_AMOUNT_EXCEEDED
    
  Scenario: Correctly matched policy
    Given policy for user C-3PO with benefit memory_backup for max total amount of 300 AUD
    And policy for user BB-8 with benefit memory_backup for max total amount of 100 AUD
    When a payment is received from BB-8 for benefit memory_backup with amount 130 AUD
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_AMOUNT_EXCEEDED

  Scenario: Unsuccessful payment is not considered
    Given policy for user Jar_Jar_Binks with benefit surgery for max total amount of 80 USD
    When a payment is received from Jar_Jar_Binks for benefit surgery with amount 90 USD
    Then the payment was unsuccessful
    And the payment declination reason was POLICY_AMOUNT_EXCEEDED
    When a payment is received from Jar_Jar_Binks for benefit surgery with amount 78 USD
    Then the payment was successful

    