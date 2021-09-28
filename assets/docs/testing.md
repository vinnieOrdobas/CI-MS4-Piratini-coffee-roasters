# Team Tracker - Testing details

[Main README.md file](/README.md)

[View website in Heroku](https://ci-ms4-piratini-co.herokuapp.com/)

## Testing

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) - To check validity of CSS Code.
- [W3C Markup Validation](https://validator.w3.org/) - To check validity of HTML Code.
- [web.dev](https://web.dev/) - To check responsiveness and audit the website.
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - To check if mobile-friendly.
- [Web Page Test by Catchpoint](https://www.webpagetest.org/) - To test performance.

## Flow testing

Usual flow through the app:

- Home > Products > Bag > Checkout > Order confirmation > Profile
- Each page section (products/bags/checkouts) have controls that allow the user to go back and forth seamlessly.

The website as a whole was thought-through to simplify navigation for the customers, providing buttons/controls based on a known online shopping experience.

## Testing user stories from "User Stories" section of README.md

### Pervasive user expectations

**Standardization**

The app was thought-through with consistency in mind, regardless of where the user happens to be.
- The Navbar and Footer are the same across pages, creating an easy-to-grasp-experience for the user.
- Headings and icons are homogenous, to relay a consistent layout.
- Product cards and collections are uniformly shaped, creating a predictable experience for the shopper.

**Effortless navigation**

- Page titles/headings describe the content of each page
- Search functionality helps the user to find the products/collections without browsing.
- Tooltip function provide information on larger displays.
- Footer encompasses information about the page and copyrights, together with social media links.

**Instinctive blueprint**

- Intuitive icons were chosen to convey typical functions of a webapp, such as padlock, heart, bag, user, magnifying glass for search, etc.
- Toasts give shoppers in-app messages to confirm user-performed actions.

**Responsive design**

- Content adjusts to a wide range of screen sizes due to Materialize grid layout and flexbox capabilities.
- When space for content is compressed, structure mutates dynamically to allow more space for the renderization of elements (for instance, pushing elements to a new row on the bag page on smaller screens).
- If necessary, text gets truncated to maintain layout.

**User security**

- Django's Allauth supplies a sturdy account framework while Stripe allows shoppers to securely checkout - webhooks generates redundancy to add an extra layer of protection.

**Attractive aesthetics**

- The landing page takes the user to a "Visual Narrative", with a hero's slideshow that relays a graphic story.
- Natural, earthy tones and use of constrasting "call-to-action" buttons create an intuitive shopping experience.
- Standard layout creates a well-known shopping experience for the user and bonds the elements together.

### As a Shopper...

**View a list of collections/products**

- The hero slideshow provides shortcuts that immediately take the shopper to the aforementioned products/collections.

**Identify deals and special offers**

- Shopper can sort products by price (either ascending or descending) to have a better outlook on how the products are priced.
- There are numerous discount codes that can be applied in the **bag** app - these discounts are communicated via email for Members of the club.

**Check my total spendings**

- Shopper can see Grand total of the order in the bag icon dropdown (for desktop users), in the **bag** app before checking out and during **checkout**, where Grand total is displayed in the Order Summary.
- Before clicking on Complete order, there's a message box that displays the amount the shopper will be charged on their credit card.

**Sort a specific category of product / Sort multiple categories/products**

- Within the "All Products page" the shopper has the option to sort products by Collection and easily categorize products.
- Shopper can further sort products within categories by price and/or alphabetically.

**Search for a product by name**

- Shoppers can look for products via the search button(magnifying glass icon on desktop) on the navigation bar.

**Select quantity of a product when purchasing it**

- Product quantities can be adjusted in the Product detail page before adding to the bag.


**View items in my bag to be purchased**

- In the **bag** app, shopper can see which products are currently in their **bag** and use the links provided to navigate to each product.
- Grand Total of the bag is displayed in the page, together with subtotal, bag total and delivery.

**Adjust the quantities of individual items in my bag**

- Shopper can adjust quantities of products in the **bag** app via the "Update | Remove" controls.

**Enter payment information**

- In the **checkout** section, shopper can quickly and securely input payment details.

**Be sure that my credit card information is safe**

- In the **checkout** section, **Stripe** provides a secure environment to input credit card information and to securely complete purchase.

**View order confirmation after checkout**

- After **Stripe** receives confirmation of payment, it takes the shopper to an order confirmation page that shows an order summary with everything the shopper bought and the grand total of the purchase.

**Receive an email confirmation after checking out**

- Shopper receives an email confirmation that the order received and displays an order summary with the grand total of the purchase.

### As a Site user...

**Register for an account**

- Users can register via the navigation bar by clicking register and signing up for an account.

**Login and Logout**

- Users can login via the user icon (for desktop users) or in the side menu (for mobile users) via the login link. That takes them to their profile page.
- Users can logout via the user icon (for desktop users) or in the side menu (for mobile users) via the logout link. That logs them out of the store.
- Users can recover their password by clicking 

**Receive email confirmations**

- After registering, users receive an email with a discount code attached prompting them to confirm their email address to login in the store.

**Have a personalized user profile**

- Registered users can login and see their personalized user dashboard, with access to their previous orders/order confirmations, default delivery information, Wish List and Membership details (if they have an active one).


### As a Site owner...

**Add a product**

- Store owners can access the Add Product page from the navbar by clicking "Store".
- In the Add product page, store owners can decide in which collection the new product will appear, the SKU number, the default image, price and the tags the product will have.

**Edit/update a product**

- The Edit Product page can be accessed from any of the pages in which a product appears by clicking the edit icon.
- The form fields are prepopulated with the existing product's details, including the image.
- From the front-end a product can only be deleted via the product detail page to minimise accidents, by clicking the trashcan icon.
- A modal appears to confirm whether they want to go ahead.

## Manual testing

### Home App

1. Navigation bar:
    1. Click nav bar links to double check if they're not broken.
    2. Check if "User" icon displays dropdown menu with "Store (if superuser)", "My Profile" and "Logout" and check if links are not broken.
    3. Check if "Bag" icon displays dropdown with "View bag" and "Checkout" and if the links work appropriately.
    4. Within the 'three dots' icon, check if elements are positioned to the right of the screen and if the JavaScript embedded in the menu loads properly.
    5. Check if search bar/functionality work properly and if leads to the right results.
    6. Change display sizes to check if elements positions are correct, specially the responsiveness of the nav bar.
    7. Check functionality and responsiveness on mobile phones, tablets and other devices.

2. Home Page Links:
    1. Check if links on slideshow lead to the appropriate collections.
    2. Check if "Discover" button leads to "About page".
    3. Check if "Join the Club" button leads to the "Membership" collection page.
    4. Check if Footer links work.

3. About Page:
    1. Check if "About page" cards/pictures renders adequately and if card images zoom in upon clicking.

4. Review bullet points in different devices, such as tablets, phones and consoles.

### Products App

1. All Products page:
    1. Check if Collections collapsible renders all collections/links appropriately.
    2. Check if sorting methods under collapsible "Sort by" works properly and with each and every collection.
    3. Check if product cards are rendered correctly, and if buttons "Add to wish list", "Collection Tag/Chip" and "Edit|Remove" buttons work.
    4. Check if product link works by clicking the product image.

2. Product Detail page:
    1. Check if "Collections" collapsible renders all collections/links appropriately.
    2. Check if "Description" collapsible renders the product description.
    3. Check if quantity widgets works properly, with arrow buttons and the typing functionality.
    4. Check if "Add to Bag" button adds the correct product to the bag and displays toast message.
    5. Check if "Add to Wish List" button adds the correct product to the User's wishlist.
    6. Check if "Add to Wish List" triggers modal if user not logged in.
    7. Check if button "Keep Shopping" leads to the "All products page".
    8. Check if "Collection Tag/Chip" and "Edit|Remove" button functions adequately.

3. Add product page (as superuser):
    1. Check if "Add product form" renders correctly, with the adequate collections on the dropdown list.
    2. Check if form field "tag" renders the appropriate tags.
    3. Check if "Choose file" widget loads properly when adding a file for product image.
    5. Check if "Add product" button creates the product in the database and display toast message.

4. Edit product page (as superuser):
    1. Check if "Edit product form" automatically populates the product's information to be edited.
    2. Check if form field "tag" renders the appropriate tags.
    3. Check if "Current image" renders the current product's image.
    3. Check if "Choose file" widget loads properly when adding a file for product image.
    5. Check if "Update product" button updates the product in the database and display toast message.

5. Remove product (as superuser)
    1. Check if upon clicking "Remove" under the product card in the "All Products page" and "Product Detail page" removes the product from the database and display toast message.

6. Review bullet points in different devices, such as tablets, phones and consoles.

### Bag App

1. Bag Page:
    1. Check if bag renders the products added via product app clicking the "Add to bag" link and if product render correctly under the bag table with round picture, card name, SKU, price, quantity widget, subtotal and "Update | Remove" functionalities.
    2. Check if "Update | Remove" widget works in conjunction with quantity widget, and if product gets updated or removed upon using controls.
    3. Check if "Bag total", "Delivery" and "Grand total" gets updated dynamically by editing bag.
    4. Check if "Add coupon" functionality triggers the renderization of a text input and button "Apply discount" affects the "Grand total" and "Discount" dynamically upon adding a valid coupon.
    5. Check if "Keep Shopping" button links to the "All Products page".
    6. Check if "Secure Checkout" leads to Checkout app with appropriate information/products.
2. Review bullet points in different devices, such as tablets, phones and consoles.

### Checkout App

1. Checkout Page:
    1. Check if "Order Summary" renders the table with product(s) information and with the appropriate count beside the section's title.
    2. Check if product's image gets rendered properly with a link to the "Product detail" page.
    3. Check if product's information gets rendered adequately, with Product information such as Name, subtotal and quantity.
    4. Check if "Order total" reflects the price of the bag, if "Delivery" reflects the appropriate cost (if under €50 euros, if above Free Delivery), if Discount (if exists) renders the appropriate percentage and if "Grand Total" reflects the sum of the cost.
    5. Check if "Checkout Form" gets rendered properly, with appropriate labels and functionality, including "Country" dropdown.
    6. Check if "Save this delivery information to my profile" renders properly if user logged in or if links to Register/Log in get rendered if user is a guest.
    7. Check if Payment/Stripe widget gets rendered properly, and message box underneath shows the appropriate amount to be charged on the credit card.
    8. Check if payment system works and generates an Order confirmation with Order number, Date and information about the order. If user logged in, if order gets saved on the user's profile and if checkbox "Save this delivery information to my profile" updates delivery information on the user's profile.
2. Review bullet points in different devices, such as tablets, phones and consoles.

### Profile App

1. Login page:
    1. Check if all the inputs in the form have appropriate width and if they're responsive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
    3. Check if the login button triggers function and compares the input with data written in the database.
    4. Check if wrong login/password returns a valid response and directs the user to try again/or to register to use the app.
    5. Checks if "Register Account" link directs the user to the register endpoint.

2. Register page:
    1. Check if all the inputs in the form have appropriate width and if they're responsive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
    3. Check if the Register button triggers function and writes the input to database.
    4. Check if username are already registered and returns a valid response if that's the case it prompts the user to try again/login.
    5. Checks if "Log In" link directs the user to the login endpoint.

1. Profile Page:
    1. Check if the profile page renders correctly according to the user's profile, including collapsibles "Default Information", "Order History", "Membership" and "Wish List".
    2. Check if "Default information" renders user's delivery information, and if "Update" button updates informations (writes to the database).
    3. Check if orders get rendered from the database in case the user has orders - if so, check if orders lead to order confirmation page with message communicating that this is an older order.
    4. Check if "Wish List" widget renders products in a table format, with appropriate product images (leading to product detail page), with name, SKU, Collections (and if the link to the collection leads the user to the collection's page), price and "Remove" button.
    5. Check if "Remove" button removes the product from the Wish List. (bug found - check README.md)
    6. Check if "Membership" collapsible renders Membership number and link to membership product on a table.
    7. Review bullet points in different devices, such as tablets, phones and consoles.

## Further testing

1. Published page on Heroku and shared on diverse social media - asked friends, family and fellow Code Institute students to test the website and let me know if any bugs should appear.
