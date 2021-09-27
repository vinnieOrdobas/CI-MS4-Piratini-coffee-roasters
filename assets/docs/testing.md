# Team Tracker - Testing details

[Main README.md file](/README.md)

[View website in Heroku](https://ci-ms4-piratini-co.herokuapp.com/)

## Testing

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) - To check validity of CSS Code.
- [W3C Markup Validation](https://validator.w3.org/) - To check validity of HTML Code.
- [web.dev](https://web.dev/) - To check responsiveness and audit the website.
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - To check if mobile-friendly.
- [Web Page Test by Catchpoint](https://www.webpagetest.org/) - To test performance.

### Flow testing

Usual flow through the app:

- Home > Products > Bag > Checkout > Order confirmation > Profile
- Each page section (products/bags/checkouts) have controls that allow the user to go back and forth seamlessly.

The website as a whole was thought-through to simplify navigation for the customers, providing buttons/controls based on a known online shopping experience.

### Testing user stories from "User Stories" section of README.md



### Manual testing

#### Home App

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

#### Products App

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

#### Bag App

1. Bag Page:
    1. Check if bag renders the products added via product app clicking the "Add to bag" link and if product render correctly under the bag table with round picture, card name, SKU, price, quantity widget, subtotal and "Update | Remove" functionalities.
    2. Check if "Update | Remove" widget works in conjunction with quantity widget, and if product gets updated or removed upon using controls.
    3. Check if "Bag total", "Delivery" and "Grand total" gets updated dynamically by editing bag.
    4. Check if "Add coupon" functionality triggers the renderization of a text input and button "Apply discount" affects the "Grand total" and "Discount" dynamically upon adding a valid coupon.
    5. Check if "Keep Shopping" button links to the "All Products page".
    6. Check if "Secure Checkout" leads to Checkout app with appropriate information/products.
2. Review bullet points in different devices, such as tablets, phones and consoles.

#### Checkout App

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

#### Profile App

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
