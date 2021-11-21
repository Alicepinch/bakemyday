# Bake My Day

Bake my day is an online e-commerce store where users can search through all of the different products on offer and add anything that they would like to purchase to their basket. On Bake my day not only can you search through the array of products that are on offer but you can also order personalised cakes, cupcakes and more. 

[Bake My Day Live Site](https://bakemydaybyamber.herokuapp.com/)

## Table of Index: 
- [UX](#ux)
   - [User Stories](#user-stories)
   - [Wireframes](#wireframes)
   - [Design](#design)
- [Features](#features)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Data Schema](#data-schema)
- [Testing](TESTING.md)
- [Deployment](#deployment)
   - [Github cloning](#creating-a-local-repository)
   - [Heroku deployment](#heroku-deployment)
- [Credits](#credits)
 
## UX

### Target Audience

- People who need a cake for a special occasion such as Birthdays, Easter, Christmas etc. 
- People who want to order sweet treats for their friends or family during the global pandemic.
- People who want to support a local business. 

### Visitor/User goals:

- Purchase products in a safe and secure way.
- Be provided with all the necessary information regarding cake ingredients for allergen reasons. 
- Be able to easily navigate across the site and to feel comfortable doing so, easily finding what they want and need. 
- Be able to gain valuable information from the blog section.

### Site Owner Goals

- To be able to easily make any adjustments needed to any products across the website.
- For customers to get a feel for the brand and what it is through the design and layout of the website.
- For customers to not only visit the website but complete orders.
- For customers to feel they can trust the brand by providing them with as much important information as they need.

## User Stories

### Shopper

- As a shopper on bakemyday I would like to be able to view all products available
- As a shopper on bakemyday I would like to be able to view product details
- As a shopper on bakemyday I would like to be able to sort products by category/occasion
- As a shopper on bakemyday I would like to be able identiy if there are any deals on the website
- As a shopper on bakemyday I would like to be able to add a product to my basket
- As a shopper on bakemyday I would like to be able to view all the products I have added to my basket
- As a shopper on bakemyday I would like to be able to search the website and see my results
- As a shopper on bakemyday I would like to be able to easily select the quantity of what I add to my basket
- As a shopper on bakemyday I would like to recieve email confirmation after I have placed an order
- As a shopper on bakemyday I would like to be able to view my order history after placing an order
- As a shopper on bakemyday I would like to be able to checkout safe and secure

### Site User

- As a site user of bakemyday I would like to easily register for an account
- As a site user of bakemyday I would like to easily login and logout
- As a site user of bakemyday I would like to easily be able to change my password
- As a site user of bakemyday I would to easily recover my password incase I forget it
- As a site user of bakemyday I would like to recieve email confirmation after registering
- As a site user of bakemyday I would like to be able to post blog posts
- As a site user of bakemyday I would like to be able to edit or delete a blog post I have created
- As a site user of bakemyday I would like to be able to comment on & view other users blog posts

## Wireframes

Below are all the wireframes that have been created for bakemyday.

### Homepage (All users):
<details><summary>Desktop </summary>

![](docs/readme/wireframes/bakemyday-homepage-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

### Products page (All users)

<details><summary>Desktop</summary>


![](docs/readme/wireframes/bakemyday-product-page-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

### Products detail page (All users)

<details><summary>Desktop </summary>

![](docs/readme/wireframes/bakemyday-product-detail-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

### Profile page (Registered users)

<details><summary>Desktop</summary>

![](docs/readme/wireframes/bakemyday-profile-page-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes.png)

</details>

### Shopping Bag (All users)

<details><summary>Desktop </summary>

![](docs/readme/wireframes/bakemyday-shopping-bag-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

### Login Page (All users)

<details><summary>Desktop </summary>

![](docs/readme/wireframes/bakemyday-login-page-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

### Register page (All users)

<details><summary>Desktop</summary>

![](docs/readme/wireframes/bakemyday-register-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>


### Contact page (All users)

<details><summary>Desktop </summary>

![](docs/readme/wireframes/bakemyday-contact-page-wireframe.png)

</details>

<details><summary>Mobile</summary>

![](docs/readme/wireframes/.png)

</details>

## Design 

### Typography 

The fonts chosen for this website are Bebas Neue and Montserrat the reason for this choice was because they were clean, modern and complimented each other. 

### Colour Scheme 

The main colour's chosen for the website are pink and brown. For links and the hover colour for the Navigation bar I chose a brown colour to match the logo and a lighter brown for the hover as a lighter contrast. For links and buttons throughout the same pink colour with brown writing and on the pink background on the home I have used the reverse colourway. 

## Features

- Products
- Product detail page
- Navigate to products with different occasions and categorys
- Checkout
- Stripe payments
- Django-allauth authorisation
- CRUD for all products
- Contact page
- Add to bag
- Profile page
- Error pages
- Blog section
- Comment section for blog
- CRUD for blog posts and comments
- About us page
 
## Future Features

- Personalisation for each product on page
- Social account login
- Multiple images per product
- Pagination
- Discount System
- Form where users can personalise a cake and generate an order
- Customer can select what size cake/how many cupcakes they would like to purchase and price will update accordingly

## Data Modelling 

Heroku PostgreSQL has been used to host the backend database in production. The database used during development of the app is SQLite.

Below are all the models used for this project. This different models within this project map to a table in the project’s database, with each of its attributes corresponding to a specific column in that table.

The data schema was planned using [dbdiagram.io](https://dbdiagram.io/home).

![](docs/readme/wireframes/bake-my-day-data-modelling.jpg) - Need to update

## Key Models

### UserProfile

- The UserProfile model is connected to the User model that is created by Allauth when a user registers
- The default fields are fields that will populate is a user has saved information, this speeds up the checkout process by pre-populating shipping details when a user order's again.

### Order

- The Order model is connected to the UserProfile model, allowing the user to view all their previous orders.
- The Order model acts as a container for the order items. Although the item is stored within the OrderItem model, having them connected allows retrieving the item purchased.

### Blog Post

- The BlogPost model is conntected to the User model from allauth to generate the author of blogpost. 
- The BlogPost model holds all information for the blogpost.

### Blog Comment
- The BlogComment model is connected to the BlogPost model to link comments to the relevant blogpost that a user is commenting on
- The BlogComment is also connected to the User model from allauth to generate the author of the comment.
- When the blogpost is deleted, the comments connected to it will also delete in the database.

### Product

- The Product model holds all information for each product on the website.
- The Product model is connected to the Category model and Occasion Models which allows a user to filter products by category and occasion in navigation.

## Technologies Used

- Python 3.8.2
- Django
- HTML
- CSS
- Heroku
- Bootstrap
- Git & GitHub.com
- Jinja templating 

### Other Tools Used

- [Font Awesome](https://fontawesome.com/) 
- [Google fonts](https://fonts.google.com/) 
- [Balsamiq](https://balsamiq.com/) 
- [Gimp](https://www.gimp.org/) 
- [W3Schools](https://www.w3schools.com/) 
- [StackOverflow](https://stackoverflow.com/) 
- [Coloors](https://coolors.co/) 
- [JShint](https://jshint.com/) 
- [W3cValidator](https://validator.w3.org/)
- Google chrome developer tools
- Stripe 
- Django Crispy Forms 
- Gunicorn 
- Psycopg2 
- AWS S3 Bucket
- Boto3
- Django Storages

### Databases
- SQlite3
- PostgreSQL 

## Testing

All the testing carried out for Bake My Day can be found [here](TESTING.md)

## Deployment

### Creating a local repository:

In order to run this on your local IDE you need to insure you have the following installed on your machine:

- PIP
- Python
- Git
- You will also need an account on MongoDB 

In order to deploy your own version of this website you will need to clone a local copy of the repository. To do this you need to follow the following steps.

- Click on the 'Code' button next to 'Add a file' when you have opened a repository
- To clone your repository by https:// click on the clipboard icon next to the URL.
- Once you have done this, open the terminal of your own IDE
  - The current directory will need to be changed to where you want your cloned directory.
- Type ```git clone https://github.com/Alicepinch/bakemydaybyamber.git``` into your terminal.

(There are other ways that you can clone a repository and these can be found on the [GitHub docs.](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories))

Once the repository is cloned you will need to ensure that all the packages needed to run this app are installed. To install all packages from requirements.txt file using the following command in terminal.
``` pip3 -r requirements.txt ```

In your local IDE create a file called env.py.
Inside the env.py file create the following environment variables: 

``` 
os.environ.setdefault("SECRET_KEY", "{YOUR SECRET KEY}")
os.environ.setdefault("STRIPE_SECRET_KEY", "{YOUR STRIPE SECRET KEY}")
os.environ.setdefault("STRIPE_WH_SECRET", "{YOUR WH SECRET KEY}")
os.environ.setdefault("SECRET_PUBLIC_KEY", "{YOUR PUBLIC KEY}")
os.environ.setdefault("DEVELOPMENT", "True")

```

**As some of this information is sensitive, be sure to create a ".gitignore" file and add "env.py"**

### Heroku deployment:

This repository can now be deployed to Heroku:

To deploy this project to Heroku you will need a Heroku acccount.
Once you have an account please follow the below steps. 

Before you deploy to heroku make sure you have dj_database_url and psycopg2 installed. To do this then enter the below into your terminal :

```
pip3 install dj_database_url
pip3 install psycopg2

```

1. In Heroku create a new app and set the region to EU. 
2. Next you want to Login to the Heroku CLI ```heroku login -i``` 
3. Run migrations on Heroku Postgres - ```heroku run python manage.py migrate```
3. Then Create a superuser - ```python manage.py createsuperuser``` 
4. Install gunicorn ```pip3 install gunicorn```
5. In your github project create a requirements.txt file using the terminal command ```pip3 freeze —-local > requirements.txt ``` (This is so Heroku can read all of the web apps that have been used in the project)

6. Create a Procfile by typing ```echo web: python app.py > Procfile``` into the terminal.

7. You will need to disable Heroku from collecting static files in your terminal with ```heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>```

8. Then add all files to github by typing 'git add .' into the terminal to stage all of your files. Then ```git commit -m "<message here>``` to commit the changes ready to be pushed to GitHub.

9. When all your files are ready to be pushed to github, type ```git push``` in the terminal.

10. Back on your Heroku dashboard for your application, go to 'Deploy'.

11. Within this section, scroll down to 'Deployment method' and select 'Connect to GitHub'

12. In the 'Connect to GitHub' section below - search for the github repository name. When you see the repository name click on the 'Connect' button.

13. Confirm the linking of the heroku app to the correct GitHub repository.

14. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

15. In the fields fill out the following:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
DISABLE_COLLECTSTATIC |	1 
SECRET_KEY | `<your_secret_key>`
SECRET_KEY | `<your_secret_key>`
STRIPE_SECRET_KEY | `<your_stripe_key>`
STRIPE_PUBLIC_KEY| `<your_stripe_secret_key>`
SECRET_WH_KEY | `<your_webhook_secret_key>`

16. Back in your terminal the next time you add, commit and push any of your changes this will automatically deploy to heroku

### AWS S3 Bucket

1. Go to Amazon AWS and create a new account
2. In apps search for S3 and create a new bucket 
   - Name your bucket to match heroku app name
   - Select region close to you
   - Allow public access for files
3. Open bucket settings and allow static website hosting 

4. Under Permissions > CORS Configuration
   - In permission tab, add in below cors configaration to set up required access for heroku app and S3 bucket:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under Permissions > Bucket Policy
   - Generate Bucket Policy 
   - Allow all principles using a * and set AWS action as 'Get Object'
   - Copy ARN from AWS into bucket policy in the ARN Box
   - Add Statement then generate policy
   - Copy policy into bucket policy generator 
   - Add the end of the resource key add /* to allow access to all resources and save policy
6. Under Access Control Tab 
   - In the public access section set 'List Objects Permission' to 'everyone'

#### AWS IAM (Identity and Access Management):

- In AWS Service menu open IAM 
- Create a group for a user to live in
- Go to JSON Tab and 'Import managed policy'
- Import S3 Full access policy 
- Copy Bucket policy ARN and paste it into S3 Full access policy 'Resource' 
- Create policy
- Navigate back to group that was created
- Attach policy to group that we created
- On users page create user with progammatic access
- Add user to group
- Download CSV file which contains users access key and secret access key
- Make sure you save this as you can't download these again

#### Connect Heroku to AWS 

- Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
- Add the secret key and access key from the .csv file to Heroku Config Vars
- Set 'USE_AWS' to true for heroku to fetch files from AWS
- Delete DISABLE_COLLECTSTATIC variable from Config Variables and deploy Heroku app
- The variables in heroku should look like:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
SECRET_KEY | `<your_secret_key>`
SECRET_KEY | `<your_secret_key>`
STRIPE_SECRET_KEY | `<your_stripe_key>`
STRIPE_PUBLIC_KEY| `<your_stripe_secret_key>`
SECRET_WH_KEY | `<your_webhook_secret_key>`
USE_AWS | TRUE
STRIPE_PUBLIC_KEY| `<your_stripe_secret_key>`
SECRET_WH_KEY | `<your_webhook_secret_key>`
AWS_ACCESS_KEY_ID | `<your_aws_acess_key>`
AWS_SECRET_ACCESS_KEY | `<your_aws_secret_key>`

## Credits

All images and content has been taken from the [@bakemyday_byamber](https://www.instagram.com/bakemyday_byamber/) instagram account. 
I have full permission to use all images and all branding for this website from the owner of this business. 

## Codes

- [Django Central](https://djangocentral.com/building-a-blog-application-with-django/) was used to help build the blog app