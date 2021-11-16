## User Stories Tested:

### Shopper

<details><summary>As a shopper on bakemyday I would like to be able to view all products available</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to view product details</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to sort products by category/occasion</summary>

<br>


</details>

<details><summary>As a shopper on bakemyday I would like to be able identiy if there are any deals on the website</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to add a product to my basket</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to view all the products I have added to my basket</summary>

<br>

</details>
<details><summary>As a shopper on bakemyday I would like to be able to create a personalised order</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to personalise my order</summary>

<br>

</details>
<details><summary>As a shopper on bakemyday I would like to be able to search the website and see my results</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to easily select the quantity of what I add to my basket</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to sort product by name an description</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to recieve email confirmation after I have placed an order</summary>

<br>

</details>

<details><summary>As a shopper on bakemyday I would like to be able to view my order history after placing an order</summary>

<br>

</details>


### Site User

<details><summary>As a site user of bakemyday I would like to easily register for an account</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would like to easily login and logout</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would like to easily be able to change my password</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would to easily recover my password incase I forget it</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would like to recieve email confirmation after registering</summary>

<br>

</details>


<details><summary>As a site user of bakemyday I would like to have a personalized user profile</summary>

<br>

</details>

<details><summary>As a site user of bakemydat I would like to be able to post blog posts</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would like to be able to edit or delete a blog post I have created</summary>

<br>

</details>

<details><summary>As a site user of bakemyday I would like to be able to comment on & view other users blog posts</summary>

<br>

</details>


## Usability Testing

iPhone 11 Plus
- Safari
- Chrome

MacBook Pro 13"
- Safari
- Chrome
- Firefox
- Microsoft Edge

iMac
- Safari
- Chrome
- Firefox
- Microsoft Edge

## W3C Validators:

### W3C HTML Validator:

0 Errors
0 Warnings

### W3C CSS Validator

0 Errors


### JSHint
JavaScript code passed through JShint with no major issues. Once run through, it prompted to add some semicolons that were missing. These were all added in where necessary.

0 Errors
1 Undefined variable stripe

### Python Testing
Pep8 Flake8 

## Form Testing

## 404, 500 Errors

If a user tries to access a page that is non existent then they will be directed to the custom 404 page. On this page there is a CTA that redirects the user back to the homepage. I have forced this error by typing a wrong URL into the bar.
In case of an internal server error occurring then a 500 error page has also been implemented. This looks similar to the 400 error page and has a CTA for users to click back to the homepage.


## Notes

Git commit: 6b66b7f81d052d42873224147e38fecd9833ff7c was a large commit due to deleting database and migrations due to a database issue meaning I couldnt create multiple blog posts. Also included was changes to allauth templates which should have been split up into two or three commits. A whole commit was done by accident