# Piratini Coffee Roasters

## [**LIVE DEMO**](https://piratini-coffee-roaster.onrender.com/)


An e-commerce website that features speciality coffee beans, collections of brewing accessories and a subscription service for monthly deliveries - Piratini Coffee Roasters is a company that believes in sustainability and working with nature.

## Table of Contents

> - [Motivation](#motivation)
> - [Description](#description)
> - [User Stories](#userstories)
> - [UX](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Resources](#resources)
> - [Testing](#testing)
> - [Bugs and Turnarounds](#bugs-and-turnarounds)
> - [Code validity](#code-validity)
> - [Version Control](#version-control)
> - [Deployment](#deployment)
> - [Installation](#installation)
> - [Credits](#credits)
> - [Acknowledgments](#acknowledgments)
> - [Support](#support)

## Motivation

> Coffee is a major export commodity, being the top legal agricultural export for numerous countries - it is one of the most valuable products exported by developing countries. Green, unroasted coffee is one of the most traded agricultural commodities in the world. More than 450 million cups of coffee are consumed **everyday** in the United States.

## Description

> Piratini Coffee Roasters is a company that believes in sourcing sustainable coffee beans that were produced with the utmost care and love for nature. Over one hundred million people in developing countries have become dependent on coffee as their primary source of income - we believe in investing on the communities producing these beans, we can move away from the *commodity* type of coffee. We only work with traditional, award-winning Brazilian producers to bring the best produce to your doorstep. We are firm believers that good coffee is made with love and care, on the comfort of your own home. 

---

### User Stories

|**AS A/AN**|**I WANT TO**|**SO I CAN...**|
|:-----|:-----|:-----|
|**Shopper**|View a list of collections/products|Purchase Items|
||See product details|Find the price, description and product image|
||Identify deals and special offers|Benefit from special savings and offers|
||Check my total spendings|Avoid spending to much|
||Sort the list of products|Identify the best priced and categorically sorted products|
||Sort a specific category of product|Browse through different categories to see narrow down my search for products|
||Sort multiple categories/products|Filter my product search even further|
||Search for a product by name|Find a specific product I'd like to purchase|
||Learn about the subscription service|Register with confidence|
||Select quantity of a product when purchasing it|Ensure I don't accidentally select wrong product/quantity|
||View items in my bag to be purchased|Identify the total cost of my purchase and all items I'll get|
||Adjust the quantities of individual items in my bag|Make changes to my order before checkout|
||Enter payment information|Check out quickly, without hassle|
||Be sure that my credit card information is safe|Confidently provide information to make a purchase|
||View order confirmation after checkout|Double check if the order has no mistakes|
||Receive an email confirmation after checking out|Keep the confirmation of what I've purchased|
|**Site user**|Register for an account|Have a personal account and view my profile|
||Login and logout|Access my personal account information|
||Recover my password if needs be|Recover access to my account|
||Receive email confirmations|Verify my account registration was successful|
||Have a personalized user profile|View my personal order history and order confirmations, save payment information|
|**Site owner**|Add a product|Add new items to my store|
||Edit/update a product|Change product prices, descriptions, images and other product criteria|
||Delete a product|Remove items that are no longer for sale|

---

### UX

> - Built to be visually appealing as a narrative, to help customers connect to the brand and what we believe in: high quality, sustainable speciality coffee beans and brewing accessories, to take the home-brewing experience to a next level. The user experience consists of bringing the user to the story of our producers and their traditional processes of growing coffee plants - fused with our cutting edge technology on roasting coffee beans. We offer a subscription service to retain our customer base, alongside cupping sessions.

#### 1. Strategy

> To achieve and simple yet compelling narrative for our users, the website leads the user through a journey to connect with the brand, where we showcase the products and accessories in their best light.
>
> ##### Project Goals
>
> - Designed for *visual storytelling*, to lead the user to connect to the brand and its products. 
>
> - Lead shoppers on an experience of brewing their coffee at home, creating a positive association with the brand/website.
>
> - Have a simple flow ot take customers to products/subscription pages and to the checkout, making it a seamless experience.
>
> ##### Customer Goals
>
> - Layout using Mobile-first approach.
> - Easy flow to reach products/collections/subscription services, while having *call-to-action* buttons to simplify the shopping experience.
> - Easy log in system to be able to check order history and save credit card information.
> - Straightforward flow to learn more about the brand and the impact it has on third-world countries.
> - Intuitive layout with toasts, messages and notifications to inform the user of every step during the experience.

#### 2. Scope

> The objective is to reach the threshold version of the app with enough usability - the Minimum viable product (MVP), that includes:
> - Authentication system for user to login/logout and sign-up - personalised profile with order history, wishlist and personal information.
> - Checkout system for users to securely pay for their items and arrange delivery.
> - The ability to add/edit/delete products by the store owner to keep the store up-to-date.
> - Showcase products, collections and subscription services on the landing page through a visual narrative of the brand.

#### 3. Structure

> - The structure of the app was based on a catalog of products, in which the visually appealing elements prompt the user to action on it. With *call-to-action* buttons, the experience becomes a journey that ends on the customer's doorstep.
> - The navbar, modals and *call-to-action* buttons were chosen to be on the background, to not take attention from the visuals and the focus on the products/accessories.

##### Data Model

> - External data modelling documentation can be found following this [link](assets/docs/data_model.md).

#### 4. Skeleton

> - [Wire frames](assets/docs/wireframes.pdf): E-commerce website with products section, collections section, profile and checkout.
>
> - Custom apps: Discount codes, Membership and Wish list.
>
> - Navigation bar - Links to each app/section of the website.
>

---

#### 5. Surface

> - I have used earth/warm tones to convey a natural layout. As inspiration, I've used [Darko Mihajlovski's Behance Coffee Shop Website Moodboard](https://www.behance.net/collection/186391225/Coffee-Shop-Website-Inspiration) as inspiration for this project.
>
> ##### Colours
>
> - To contrast with the background and the slideshow, I've opted for a transparent background navbar and collapsibles with a strong colour for icons as contrast. (#bf360c)
> - For body text, I've used a neutral black to contrast with the mild background tone (#EAE7E0).
> - For the footer, I've opted for a mild brown for warmth and a natural feeling (#D7CCC8).

---

> #### Typography
>
> - "Arvo" font (with fall-back font of serif) for body content and titles.

### Features

#### Existing Features

> - Designed with HTML5, CSS3, Python, Django, JavaScript and Materialize.
> - Navigation bar allows users to engage with the system in a seamless, easy way.
> - Easy access to products/collections, via search bar or sorting methods.
> - In-app communication via toasts.
> - Register/sign-in functions to and user profile to easily access order history, wish list, membership card and default shipping information.
> - Fully functioning checkout system powered by [Stripe](https://stripe.com/ie).
> - Store management functionalities to add/edit/remove products, collections and discount codes.

#### Features to implement

> - Subscription system to handle membership payments.
> - Search based on product's tags.
> - Expand store management functionalities, such as creating discount codes via the website (rather than the admin.)
> - Expand mailing functionalities, as registering email accounts to receive newsletters.
---

### Technologies Used

#### 1. Languages

> - [HTML5](https://en.wikipedia.org/wiki/HTML5)
>
> - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
>
> - [JavaScript](https://www.javascript.com/)
>
> - [Python](https://www.python.org/)

##### 2. Integrations

> - [Django](https://www.djangoproject.com/) - Python Framework
>
> - [Materialize](https://materializecss.com/) - Classes for the overall layout of the website
>
> - [PostgreSQL](https://www.postgresql.org/) - External Database
>
> - [FontAwesome](https://fontawesome.com/) - Card Icons, footer social media links
>
> - [Google Fonts](https://fonts.google.com/) - Typography
>
> - [jQuery](https://jquery.com/) - JavaScript Library
>
> - [Stripe](https://stripe.com/ie) - Payment infrastructure
>
> - [Amazon Web Services](https://www.aws.com/) - Used to host project static and media files on production
>
> - [materialize-css-form](https://github.com/kalwalkden/django-materializecss-form) - Django package to handle project forms with MaterializeCSS
>
> - [dbdiagram.io](https://dbdiagram.io/) - Used to create data_model.md file

##### 3. Workspace, version control and Repository storage

> - [VSCode](https://code.visualstudio.com/) - IDE
>
> - [Git](https://git-scm.com/) - Version Control
>
> - [GitHub](https://github.com/) - Repository Storage

##### 4. Other

> - [Autoprefixer](https://autoprefixer.github.io/) Parses CSS and adds vendor prefixes.
>
> - [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) Mobile-friendly check on site.
>
> - [Website Page Test](https://www.webpagetest.org/) Runs a website speed test from multiple locations around the globe using real browsers (IE and Chrome) and at real consumer connection speeds.
>
> - [Online-Spellcheck](https://www.online-spellcheck.com/) Online spelling and grammar checks.
>
> - [web.dev](https://web.dev/) Runs an audit on the website's performance.

### Resources

> - [Code Institute Course Content](https://courses.codeinstitute.net/) - Primary resource for this project.
> - [Balsamiq](https://balsamiq.com/wireframes/) - Wire framing design tool.
> - [Bootsrap Grid Explanation by Anna Greaves](https://ajgreaves.github.io/bootstrap-grid-demo/) - Resource for Bootstrap Grids.
> - [Stack Overflow](https://stackoverflow.com/) - Common questions.
> - [Youtube](https://www.youtube.com/) - Tutorials.
> - [CSS-Tricks](https://css-tricks.com/) - Quick CSS resources.
> - [Common Mark](https://commonmark.org/help/) - For Markdown language reference.
> - [Grid Critters](https://gridcritters.com/) - To learn CSS Grid technology.
> - [Markdown Tutorial](https://www.markdowntutorial.com/) - Used to learn Markdown.
> - Code Institute **SLACK Channel** - Assistance.
> - [Creating a Toggled Search Bar](https://www.solodev.com/blog/web-design/creating-a-toggled-search-bar.stml) - To create navbar **search box**
> - [Django forms with materializecss](https://www.youtube.com/watch?v=qte0MSKClVM) - To use **materializecss** filter on Django forms
> - [Django by Example: Creating a Coupon System](https://www.youtube.com/watch?v=_dSCGMJcoe4) - Insights on how to create **discounts app**
> - [Python Django Ecommerce Customer Wish List](https://www.youtube.com/watch?v=OgA0TTKAtqQ) - Insights on how to create **wishlist app**




### Testing

> External testing documentation can be found following this [link](assets/docs/testing.md).

---

### Bugs and turnarounds

> - Sidenav trigger icon in "base.html" disappearing on small screens for page products.html. The "about-card" div element had the clas "offset-s6" which pushed the sidenav trigger button to the outskirts of the view port. Adjusted the issue by putting the menu items on a higher z-index value.
> - Control buttons for "bag.html" and "product_detail.html" weren't changing the quantity in the quantity input box. Followed this [**Tutorial - Number Increment Buttons with jQuery**](https://css-tricks.com/number-increment-buttons/) to solve the issue and create own JavaScript function.
> - OrderLineItem model in "checkout/models.py" not calculating price and saving it - Django error: "no such column: checkout_orderlineitem.lineitem_total". Found typo on the function save in the OrderLineItem model "self.lineitems_total = self.product.price * self.quantity". Updated "self.lineitems_total" to "self.lineitem_total" and fixed the bug.
> - OrderLineItem model (order_line_item) not saving, due to a TypeError: "unsupported operand types for * : 'float' and  'decimal'". Variable settings.STANDARD_DELIVERY_PERCENTAGE had the value of 0.1(transforming it in a float). Changed to integer 10. 
> - In "checkout/webhook_handler.py" - creating the discount code and applying to the order model, webhook kept spitting error: "ERROR: NOT NULL constraint failed: checkout_order.discount_code". Dumped products/collections and wiped the DB to make it functional again.
> - When sending confirmation email after the order has been processed, Django throws the error: django.template.exceptions.TemplateDoesNotExist: checkout/confirmation_emails/confirmation_email_subject.txt. Moved folder "confirmation_emails" to checkout/templates/checkout and fixed the bug.
> - WishList model unable to add products via ManyToMany field in checkout_success view. Used the method profile.membership.get() to circumvent the issue and add the product.
> - Getting 500 server error when trying to send confirmation emails. Fixed the bug by resetting App profile on Gmail.com.
> - Wish list icon on products page not adding products to the wish list/triggering login required modal. Changed the ID and the action button to fix the issue.
> - In "product.detail.html", "Add to bag" button triggering "Membership already exists" modal even though object wasn't there. Changed the if statement to "user.membership.exists" to circumvent the issue.
> - "Forgot Password" throwing Server error (500) in production - in development, allauth was unable to render materializecss filter for form as it wasn't loaded in the template.
---

### Code validity

> [W3C](https://validator.w3.org/) - Markup Validation
>
> [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation
>
> [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) - Validates if tags are correctly closed.
>
> [JSHINT](https://jshint.com/) - JavaScript code warning & error check.
>
> [PEP8 online](http://pep8online.com/) - PEP8 validator.
---

### Version Control

> - Used Git for version control.

---

### Deployment

This project has been deployed on Heroku following this process:

> - All code was written on VS Code, an IDE.
> - The code was then pushed to GitHub where it is stored in my [Repository](https://github.com/vinnieOrdobas/CI-MS4-Piratini-coffee-roasters).
> - Navigate to [Heroku](https://www.heroku.com/) and login.
> - On the dashboard, click on the 'New' button and select 'Create new app'.
> - Enter the app name and select a region.
> - On the project resources tab, provision a new PostgreSQL database for this project.
> - Navigate to [Stripe](https://www.stripe.com) and register to get a Public Key, a Secret Key and a Webhook Secret
> - Create an account on Amazon AWS and add a new S3 bucket for this project, get an user access ID and Access key.
> - Under the 'Settings' tab, click on 'Config Vars' and add the following variables:
```
DISABLE_COLLECTSTATIC=1
SECRET_KEY=<your_project_key>
STRIPE_PUBLIC_KEY=<your_personal_public_key>
STRIPE_SECRET_KEY=<your_personal_secret_key>
STRIPE_WH_SECRET=<your_personal_webhook_key>
EMAIL_HOST_PASS=<your_email_password>
EMAIL_HOST=<your_email_address>
USE_AWS= True
AWS_ACCESS_KEY_ID=<your_aws_user_access_id>
AWS_SECRET_ACCESS_KEY=<your_aws_user_access_password>
DATABASE_URL=<your_heroku_postgres_uri>
```
> - On your `settings.py` file, in the `ALLOWED_HOSTS` array add your Heroku project URL as a string.
> - In the menu select the 'Deploy' option.
> - Under 'Deployment method' select the GitHub option to connect to your GitHub repository. Ensure GitHub username is selected and use the search function to find the relevant repository.
> - Select Automatic deploys from the main branch and click 'Deploy Branch'.

#### How to run this project locally

To clone this project into your IDE you will need:

> - A **GitHub** account. Create one [here](https://github.com/join).
> - **Google Chrome** browser.

Follow this steps:

1. Install [Gitpod Browser Extentions for Chrome](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki).
2. After installation, restart the browser.
3. Log into [Gitpod](https://www.gitpod.io/) with your gitpod account.
4. Navigate to the [Project GitHub repository](https://github.com/vinnieOrdobas/CI-MS4-Piratini-coffee-roasters).
5. Click the green button "Gitpod" in the top right corner of the repository.
6. On the terminal, install Django with the follow command:
```
pip3 install django
```
7. Install project dependencies by running the command:
```
pip3 install -r requirements.txt
```
8. Add the below environment variables to run the project:
   ```
   DEVELOPMENT=True
   STRIPE_PUBLIC_KEY=<your_personal_public_key>
   STRIPE_SECRET_KEY=<your_personal_secret_key>
   STRIPE_WH_SECRET=<your_personal_webhook_key>
   ```
9. Create project models and database by running the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
10. Run server locally with the following command:
```
python3 manage.py runserver
```
To work on the project within a local IDE (such as VScode):

1. Follow this link to the [Project GitHub repository](https://github.com/vinnieOrdobas/CI-MS4-Piratini-coffee-roasters).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to ve made.
6. Type "git clone" on your terminal, then paste the URL of the project.
7. On the terminal, install Django with the follow command:
```
pip3 install django
```
8. Install project dependencies by running the command:
```
pip3 install -r requirements.txt
```
9. Add the below environment variables to run the project:
   ```
   DEVELOPMENT=True
   STRIPE_PUBLIC_KEY=<your_personal_public_key>
   STRIPE_SECRET_KEY=<your_personal_secret_key>
   STRIPE_WH_SECRET=<your_personal_webhook_key>
   ```
10. Create project models and database by running the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
11. Run server locally with the following command:
```
python3 manage.py runserver
```
### Credits

> #### Media
>
>
> - Icons rendered by [Font Awesome](https://fontawesome.com/)
>
> - Pictures taken from [Shopify Burst](https://burst.shopify.com/)
>
> - Layout based on Shopify's [Narrative Theme](https://themes.shopify.com/themes/narrative/styles/earthy?price%5B%5D=free&surface_inter_position=1&surface_intra_position=3&surface_type=all)
>
> - Product images [Cafe Especial Brasil](https://cafeespecialbrasil.net.br/), [Coffee Mais](https://coffeemais.com/), [MelhorCafe](https://melhorcafe.com/), [CoffeeShop.ie](https://www.coffeeshop.ie/), [BREWBOXCOFFEE](https://www.brewboxcoffee.ie/)

> ##### Content
>
> - Text content was written by me.
>
>
>
> ##### Acknowledgments
>
> I would like to thank:
>
> - **Victor Miclovich**, my Mentor, for his insights, composure and experience. His invaluable assistance helped make this project reality.
> - **Anderson Gonçalves** for taking the time to meet me and talk about this project, for tips and incredible insights, but above all, for his friendship.
> - **CI Mentors** for helping me identify and define problems.
> - **CI staff** for their care and affableness, and for always make sure I was in the right path.
> - **Slack Community** for their help with my code, for support and to make me feel part of the community.

##### Support

> For bug resolution, please reach Vinnie Ordobas on viniordobas@icloud.com