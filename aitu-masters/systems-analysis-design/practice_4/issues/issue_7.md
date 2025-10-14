# List all products in the catalog

**As a** User
**I need** ability to list all products in the catalog on e-commerce website
**So that** I can check all available products on the platform (for Customer/Buyer) and compare them with others (for Seller)

### Details and Assumptions
* Product metadata should be received from persistent database
* Product data (like attachments, files, images, multimedia, etc.) should be received from file/object storage
* About products list availability to not registered users: #2
* Backend API should be HTTP/HTTPS GET method on route "/products/":

### Acceptance Criteria
```gherkin
# From backend API side
Given that a user want to get list of all products in the catalog
When send via HTTP client request with GET method on route "/products/"
Then receive HTTP response with 200 status
    And data of products in list

# From frontend side
Given that a user want to get list of all products in the catalog
When on the e-commerce website
    And logged-in to account
    And on a home page
    And press "catalog" in header
Then redirects to "catalog" page where list of available products in form of cards (brief information and picture)
```
