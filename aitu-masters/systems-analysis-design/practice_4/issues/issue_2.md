# Retrieve a product from the catalog

**As a** User
**I need** ability to retrieve a product from the catalog on e-commerce website
**So that** I can check particular product in general for its details (for Customer/Buyer) and that is displayed correctly with right information (for Seller)

### Details and Assumptions
* TODO: determine whether the user must be logged-in to view any products (be a platform member to enhance security and reduce availability risks) or if product information can be publicly accessible (without account) for SEO and advertising purposes. 
* Product metadata should be received from persistent database
* Product data (like attachments, files, images, multimedia, etc.) should be received from file/object storage
* Backend API should be HTTP/HTTPS GET method on route "/products/{id}":
  - id (unique identifier of the product) in path parameters

### Acceptance Criteria
```gherkin
# From backend API side
Given that a any user has a product that they want to find
When send via HTTP client request with GET method on route "/products/{id}"
    And id of the product in path parameters
Then receive HTTP response with 200 status
    And data of the product

# From frontend side
It is a service function used to dynamically fetch data within
the product page and shouldn't be described in this scenario
```
