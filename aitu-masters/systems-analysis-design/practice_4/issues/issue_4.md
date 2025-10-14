# Delete a product from the catalog

**As a** Seller  
**I need** ability to delete a product from the catalog on e-commerce website
**So that** I can remove outdated, unnecessary, or discontinued products from the catalog
   
### Details and Assumptions
* TODO: delete record or mark record as deleted (is_deleted / is_active: bool) - hard delete vs. soft delete
* Product metadata should be deleted from persistent database
* Product data (like attachments, files, images, multimedia, etc.) should be deleted in file/object storage
* Backend API should be HTTP/HTTPS DELETE method on route "/products/{id}"
    - id (unique identifier of the product) in path parameters
* Seller cannot specify id of the product that is not owned by him, so it is not possible to delete resource belonging to another seller
   
### Acceptance Criteria
```gherkin
# From backend side
Given that a seller want to update one of its products
When send via HTTP client request with DELETE method on route "/products/{id}"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 200 status
    And data of the published product

Given that a seller want to update one of its products
When send via HTTP client request with DELETE method on route "/products/{id}"
    And id of the product in path parameters
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 403 status
    And exception/error explanation

# From frontend side
Given that a seller want to delete one of its products
When on the e-commerce website
    And logged-in to account
    And on a product page
    And press "delete product" button
    And press "confirm" button
Then a success message appears
    And redirects to the home page

Given that a seller want to delete someone else's product
When on the e-commerce website
    And logged-in to account
    And on a product page
Then the product page will not show "delete product" button (hidden element), because system checks owned id matching
```
