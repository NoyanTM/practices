# Like a product in the catalog

**As a** User
**I need** ability to like a product in the catalog on e-commerce website
**So that** I can rate products that might be interested to me or got my interest

### Details and Assumptions
* TODO: upgrade to complex review commenting and following/subscribing/favorites systems
* TODO: add condition that only Customer/Buyer can set like/dislike to product, so Seller cannot do such operation to their own products - only on those that do not belong to him to prevent any manipulations
* "Like" counter (and who liked) is attached to product metadata which is stored in persistent database
* "Like" counter can go up and down in integer format (0 is default, but never less than 0)
* User cannot give more than "like" one time at total for each product
* Backend API should be HTTP/HTTPS POST method on route "/products/{id}/like"

### Acceptance Criteria
```gherkin
# From backend side
Given that a user want to give "like" to a product
When send via HTTP client request with POST method on route "/products/{id}/like"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 200 status
    And "like" counter is increased by 1, "like" of the user to the product is added

Given that a user want to give "like" to a product that is already with "like" from same user
When send via HTTP client request with POST method on route "/products/{id}/like"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 400 status
    And exception/error explanation

# From frontend side
Given that a user want to give "like" to a product
When on the e-commerce website
    And logged-in to account
    And on a product page
    And press "like product" button
Then the button becomes filled green (activated)
    And "like" counter increased next to that button

Given that a user want to give "like" to a product that is already with "like" from same user
When on the e-commerce website
    And logged-in to account
    And on a product page
    And press "like product" button
Then the button is not changed, because it is already activated
```
