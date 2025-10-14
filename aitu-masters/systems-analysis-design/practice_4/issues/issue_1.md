# Create a product in the catalog

**As a** Seller
**I need** ability to create a product in the catalog on e-commerce website
**So that** I can showcase and keep all my new products for sale or advertising them to customers

### Details and Assumptions
* Added products should be stored in persistent database for their metadata
* Added product data (like attachments, files, images, multimedia, etc.) should be stored in file/object storage
* A product should have unique identifier and required fields to be searched 
* Backend API should be HTTP/HTTPS POST method on route "/products/{id}" with required fields as body:
  - product_id (unique identifier, automatically generated)
  - owner_id (unique identifier, automatically passed from who created)
  - created_at (automatically generated)
  - title (required)
  - description (required)
  - price and currency
  - image_url, attachments, etc.
  - ...

### Acceptance Criteria  
```gherkin
# From backend API side
Given that a seller has a product that they want to publish
When send via HTTP client request with POST method on route "/products/{id}"
    And data passed as body payload
    And valid session token of the user passed in headers/cookies
Then receive HTTP response with 201 status
    And data of the published product

# From frontend side
Given that a seller has a product that they want to publish
When on the e-commerce website
    And logged-in to account
    And press "publish product" button
    And they enter the correct required data into the form
    And press "confirm" button
Then a success message appears
    And a button that redirects to the created product's page/publication
```
