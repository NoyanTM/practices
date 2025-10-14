# Query a subset of products in the catalog

**As a** User
**I need** ability to query a subset of products in the catalog on e-commerce website
**So that** I can do precise search on specific subset/categories of products

### Details and Assumptions
* Generally, it is an extension for optimization needs of #7
* Pagination: Backend API should be HTTP/HTTPS GET method on route "/products/"
    - Different forms of pagination such as: limit-offset, cursor, etc.
    - Reference: https://www.django-rest-framework.org/api-guide/pagination/
* Filtering: Backend API should be HTTP/HTTPS on route "/products/search" or "/search/"
    - Can be GET method with additional query parameters (?ascending, ?title, ?count, etc.)
    - Or POST/QUERY method where filters passed as body payload, due to 414 status (Request-URI Too Long) even with base64-like encoding
    - Using regular expressions, fuzzy search, ranking / recommendation system, etc.
    - Reference: https://www.django-rest-framework.org/api-guide/filtering/
### Acceptance Criteria  

```gherkin

# From backend API side
TODO:

# From frontend side
Given that a user want to get list of all products in the catalog
When on the e-commerce website
    And logged-in to account
    And on a catalog page
    And задает в поиске определенный фильтр
    And задает определенные лимиты и т.д.
Then 

refreshes "catalog" page с определенным subset of products
in form of cards (brief information and picture)
```
