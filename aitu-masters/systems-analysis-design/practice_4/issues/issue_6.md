# Dislike a product in the catalog

**As a** User
**I need** ability to dislike a product in the catalog on e-commerce website
**So that** I can rate products that might be not interested to me or violates something

### Details and Assumptions
* TODO: upgrade to complex review commenting and following/subscribing/favorites/report systems
* "Dislike" counter (and who disliked) is attached to product metadata which is stored in persistent database
* "Dislike" counter can go up and down in integer format (0 is default, but never less than 0)
* User cannot give more than "dislike" one time at total for each product
* If user already gave "like" and then "dislike", initial "like" will be removed (and vica versa like state machine)
* Backend API should be HTTP/HTTPS POST method on route "/products/{id}/dislike"

### Acceptance Criteria
```gherkin
# From backend side
Given that a user want to give "dislike" to a product (with no initial "like" and "dislike" from same user)
When send via HTTP client request with POST method on route "/products/{id}/dislike"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 200 status
    And "dislike" counter

Given that a user want to give "dislike" to a product with already "dislike" from same user
When send via HTTP client request with POST method on route "/products/{id}/like"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 400 status
    And exception/error explanation

Given that a user want to give "dislike" to a product with already "like" from same user
When send via HTTP client request with POST method on route "/products/{id}/like"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 200 status
    And "dislike" counter is increased by 1, "dislike" of the user to the product is added
    And "like" counter is decreased by 1, "like" of the user to the product is removed

# From frontend side
TODO: 
```

