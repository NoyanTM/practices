# Update a product in the catalog

**As a** Seller  
**I need** ability to update a product in the catalog on e-commerce website
**So that** I manage products that owned/created by me as needed in order to keep them actual/relevant

### Details and Assumptions
* Updated product metadata should be stored and changed in persistent database
* Updated product data (like attachments, files, images, multimedia, etc.) should be stored and changed in file/object storage
* Backend API should be HTTP/HTTPS PUT/PATCH methods on route "/products/{id}" with required fields as body payload
* Seller cannot specify id of the product that is not owned by him, so it is not possible to overwrite resource belonging to another seller

### Acceptance Criteria  
```gherkin
# From backend side
Given that a seller want to update one of its products
When send via HTTP client request with PUT/PATCH method on route "/products/{id}"
    And data passed as body payload
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 200 status
    And data of the published product

Given that a seller want to update someone else's product
When send via HTTP client request with PUT/PATCH method on route "/products/{id}"
    And data passed as body payload
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 403 status
    And exception/error explanation

# From frontend side
Given that a seller want to update one of its products
When on the e-commerce website
    And logged-in to account
    And on a product page
    And press "edit product" button
    And they enter the correct required data into the form
    And press "confirm" button
Then a success message appears
    And updated information on the product page

Given that a seller want to update someone else's product
When on the e-commerce website
    And logged-in to account
    And on a product page
Then the product page will not show "edit product" button (hidden element), because system checks owned id matching
```

