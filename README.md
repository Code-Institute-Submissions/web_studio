
![readme-testing](https://raw.githubusercontent.com/marcelkolarcik/web_studio/master/readme_images/marcelli.gif)
Live preview of the site : <a href="https://marcelli.herokuapp.com/">marcellidesigns</a>
# marcellidesigns



## What is it 

An online web development agency.

An agency, where you can order your next blog, website, online store, or anything else you have in mind.
Also place for freelance web developers and web designers to sign up and work with us... 




## Table of Contents

- [Usage](#Usage)
- [User Experience](#User-Experience)
   - [User story](#User-story)
   
      - [Public user](#Public-user)
      - [Logged in user](#Logged-in-user)
      - [Admin](#Admin)
      
   - [Step by step guides](#Step-by-step-guides)
   
      - [Create appointment](#Create-appointment)
      - [Edit appointment](#Edit-appointment)
      - [Delete appointment](#Delete-appointment)
      - [Purchase product](#Purchase-product)
     
      
      
      
- [Wireframes](#Wireframes)
- [Colors](#Colors)
   
- [Technologies](#technologies)

   - [cypress.io](#cypressio)
   - [javascript,HTML,CSS](#javascriptHTMLCSS)
   - [Python,Django](#PythonFlask)
   - [Mailgun](#Mailgun)
   - [AWS](#AWS)
  
   

- [Features](#Features)       
- [Testing](#testing)
- [Version Control](#Version-Control)
- [Deployment](#deployment)
- [Difficulties](#Difficulties)
- [Future Features](#future-features)
- [Browser support](#Browser-support)
- [Acknowledgements](#Acknowledgements)



## User Experience

 - ### User story
 
    - #### Public user
     
    
   As a potential customer I would like to be able to:
  
        -  see the work of the web studio
        -  see the products, they offer
        -  book an initial consultation
        -  purchase a product/service
        -  use the site on any type of device
       
     
   - #### Logged in user
          
         
   As a logged-in customer I would like to be able to:
     
       -  same as public user plus :
       -  have an account on the site
       -  edit consultation
       -  delete consultation
       -  purchase another consultation
       -  see my consultations and purchases from the site
       -  use the site on any device
 - #### Freelancer
          
         
   As a freelancer working for the agency I would like to be able to:
     
       
       -  have a dashboard where I can update the client on work progress
       -  communicate with the client through the dashboard
             
   - #### Admin
                    
                   
   As an Admin of the site I would like to be able to:
              
       -  have an account on the site
       -  preview all the consultations, and mark them as done, once they are done
       -  preview all the orders
       -  use the site on any device
       - receive an email, when there is a new appointment or order, or if there is an error during purchase.
             
   
 
  - ### Step by step guides
  
  Here guides for interactions with the application.
  
   - #### Create appointment
        
     To create an appointment, click on the products link in the top nav and select any product, and then click on 
     Book a free initial consultation button. You will be taken to the consultation page, where you need to fill in the form with your details. When you click on the book button, we will create your appointment and create an account for you,
     so that you can sign in and update or delete your appointment. If you decide to purchase any of our products, you will see your purchases as well. You will receive an email, confirming your appointment.

   - #### Edit appointment
     To edit your appointment, log in with your credentials by clicking on the Login link in the top navigation and entering your credentials into the login form. You will be logged in to your dashboard where you will see your appointment.
     Click on the edit appointment link. You will see the form with your appointment.
     You will be able to edit time, site type, and project description. 

   - #### Delete appointment
     To delete your appointment, log in with your credentials by clicking on the Login link in the top navigation and entering your credentials into the login form. You will be logged in to your dashboard where you will see your appointment.
     If you want to delete it, click on the edit appointment link, and then on the delete appointment button located under the form. 

   - #### Purchase-product
   To purchase a product, select the product from the drop-down menu in the top navigation or click on any Buy Now! button, you will be taken to the checkout page. Fill in your details, for testing purposes, you can use Stripe test credit card number
        
        4242 4242 4242 4242 
   with any date in the future for the expiry date and any number for CVC code.
   
   Once you click on the Complete Order button, you will receive an email confirming your purchase, or if there was an error,
   you will receive an email informing you, that there was an error, and that your card was not charged.
   - #### Communicate with developer ( client )
        
     To be able to communicate with the developer, log in into your dashboard and click on edit consultation and then write into the text area named "your project" and click on update. If the developer is logged in,
     he might reply to you
     
   - #### Communicate with client ( developer )
        
     To be able to communicate with the client, login in your dashboard and click on job progress
     and check what work has been done so far, so when the client logs into his dashboard, he will see
     progress with the work. 
     You can also write to the notes text area and click on the update. If the client is logged in,
     he might reply to you.
    
- ### Wireframes  
   
   I used Adobe Illustrator to create wireframes for the site. I used exact colors from the website,
   so that the client will have a better idea of how his website going to look like.
  
[Wireframes.pdf](readme_images/wireframes.pdf)
    
 - ### Colors 
 
   I decided on dark grey and turquoise color scheme with a touch of bright green to give it a bit of freshness. The color turquoise is associated with meanings of refreshing, sophisticated, energy, wisdom,  creativity, and dark grey is associated with timelessness and practicality
 
## Technologies 
### cypress.io
> Fast, easy and reliable testing for anything that runs in a browser.

I decided to write some tests for the front end in cypress.io. 
I Installed Cypress via npm: 

```cl 
cd /your/project/path
```

```cl 
npm install cypress --save-dev
```

And whenever I want to run tests, I use
```cl 
./node_modules/.bin/cypress open
```


 

 
 
 
 ### javascript,HTML,CSS
 
   - javascript 
   > JavaScript is a scripting or programming language that allows you to implement complex features on web pages
   
   - HTML
   > HTML is the standard markup language for creating Web pages.
   
   - CSS
   > CSS is is a style sheet language used for describing the presentation of a document written in 
    a markup language like HTML.CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
    
### Python,Django
   - Python 
   >    Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
It's high-level built-in data structures, combined with dynamic typing and dynamic binding,
 make it very attractive for Rapid Application Development, as well as for use 
as a scripting or glue language to connect existing components.
   
   - Django
   >    Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
    Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source.

### Mailgun
 I am using the Mailgun service for sending emails, as I created the account while releasing www.globtopus.com to the public.
 I can create email templates for every type of email and store it in Mailgan Dashboard, and when sending
 email from the app, I just name the template and send the variables with my MAILGUN KEYS, and the emails are sent
 with the templates I chose. 
 
### AWS
To store my images and static files like javascript and CSS files, I am using Amazon Web Services s3.
Which is a cloud-based storage service. I created an account by clicking on create an AWS account.
 On the account type page, I selected personal and filled out the required information.
And clicked to create account to continue. Once signed in I search for S3 services and create a new bucket, named marcellidesigns for easy remembering. And selected Europe as a region. I unchecked block all public access since this bucket needs to be public to allow access to our static files. Then I need to set some settings. By clicking on
the newly created bucket and then on the properties tab, I click on static website hosting, for index and error documents, I entered
default values. Then click Save. On the permissions tab, we will make a few changes. First I'll paste in a CORS configuration
which is going to set up the required access between our Heroku app and this s3 bucket.
Next, I'll go to the bucket policy tab.
And select a policy generator so we can create a security policy for this bucket.
The policy type is going to be an s3 bucket policy.
Will allow all principals by using a star.
And the action will be, get an object.
Now I'll copy the ARN which stands for Amazon resource name from the other tab.
And paste it into the ARN box at the bottom. I'll click Add statement. Then generate policy.
Then copy this policy into the bucket policy editor.
Before I click Save because I want to allow access to all resources in this bucket.
I'll add a slash star onto the end of the resource key.
Then I click save. The next thing to configure is to go to the access control list tab
and set the list objects permission for everyone under the Public Access section.

Now I need to create a user to access it.
I can do this through another service called IAM which stands for Identity and Access Management.
The process here is first I'm going to create a group for our user to live in.
Then I create an access policy giving the group access to the s3 bucket I created.
And finally, I assign the user to the group so it can use the policy to access all my files.
To create a group, I click on the group and give it the name manage-marcellidesigns. Then I click the next few times until I
see and click on the create group button. Now I can create the policy used to access our bucket by clicking policies and then create policy. I'll go to the JSON tab and then select import managed policy which will let me
import one that AWS has pre-built for full access to s3.
I'll search for s3 and then import the s3 full access policy.
I only want to allow full access to my new bucket and everything within it.
So I am going to get the bucket ARN from the bucket policy page in s3 and paste it into Resource.
Then I click on a review, give it name and description and click on create policy.

Now I need to attach the policy to the group I created.
I'll go to groups, click my manage-marcellidesigns group
and click attach the policy.
I will search for the policy I just created and select it.
And click attach the policy.
Finally, I'll create a user to put in the group.
On the user's page, I'll click add a user.
create a user named marcellidesigns-staticfiles-user.
Give him programmatic access.
And then select next. Now I can put the user in our group.
I'll click through to the end and then click to create a user.
Now I'll download the CSV file which will contain this users access key and secret access key
Which I'll use to authenticate him from my Django app.
To connect Django to the AWS s3 bucket I'll need to install
boto3 and Django-storages. I need to add some settings in settings.py like AWS_STORAGE_BUCKET_NAME
and AWS_S3_REGION_NAME which I downloaded from AWS.
Whenever collectstatic is run. Django will collect static files automatically and upload them to s3


 ## Features
 
 - ### Public client 
 
 A public client can :
    
       -  book Free initial appointment
       -  purchase any product on the site using secure checkout provided by Stripe, provided he has his project id from initial consultation
       -  use the site on any device
             
             
- ### Logged in client 
     
 Logged in client can :
     
       -  same as public user plus :
       -  Login after booking the initial appointment to manage his appointment, and see any purchases on the site
       -  update consultation details and comunicate with developer
      
 
- ### Admin 
     
Admin can :
              
       -  have an account on the site
       -  preview all Appointments,Orders,Projects and Freelancers
       -  mark Appointment as done
       -  assign Project to the Freelancer
       -  add new products to the site
       -  use the site on any device
       


 - ### Logged in freelancer 
     
 Logged in freelancer can :
     
      
       -  Update his registration details
       -  Communicate with the client through the dashboard
       -  Update client with the progress of the work


- ### Favicon
I have created a Favicon. Favicons save the users time in identifying a website from bookmarks, history,
 and other places where a browser places that favicon for quick identification. It just makes life easier for your average user.
 
 ## Testing
 The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project 
 to ensure there were no syntax errors in the project.
 
 Some front-end testing was done in cypress.io. Test case: Customer creating an appointment, logging in, editing appointment.
 
  
 All the back end tests were done with TestCase form django.test
 #### Test Cases:
 #### Appointment
     test_appointment_name_is_required PASS
     test_done_field_is_not_required PASS
     test_fields_are_explicit_in_form_metaclass PASS
     test_done_defaults_to_false PASS
     test_create_edit_appointment PASS
     test_get_add_appointment_page PASS
     test_get_edit_appointment_page PASS
     test_can_create_appointment PASS

 #### checkout
     test_checkout_blog_page PASS
     test_checkout_website_page PASS
     test_checkout_online_store_page PASS
     test_order_name_is_required PASS
     test_fields_are_explicit_in_form_metaclass PASS
     test_customer_name_repr_method_returns_name PASS

#### freelancers
     test_freelancer_name_is_required PASS
     test_on_the_job_field_is_not_required PASS
     test_fields_are_explicit_in_form_metaclass PASS
     test_done_defaults_to_false PASS
     test_appointment_string_method_returns_name PASS
     test_can_freelancer_create_account PASS
     test_freelancer_can_update_his_details PASS
     test_register_freelancer_page PASS

#### products
     test_product_name_is_required PASS
     test_product_price_is_required PASS
     test_product_form_with_price_and_name_is_valid PASS

#### projects
     test_project_number_is_required PASS
     test_project_form_with_project_number_is_valid PASS
     test_fields_are_explicit_in_form_metaclass PASS
     test_project_progress_steps_default_to_false PASS
     test_project_string_method_returns_project_number PASS
     test_project_preview_page PASS

#### public_USER
     test_index_page PASS
     test_portfolio_page PASS
     test_howitworks_page PASS
     test_appointments_page PASS
     test_freelancer_page PASS
     test_user_can_login PASS
 
 Stripe testing was done by using different types of test card numbers to produce different types of responses.
 
    4000000000000077   Charge succeeds and funds will be added directly to your available balance (bypassing your pending balance).
    4000003720000278   Charge succeeds and funds will be added directly to your available balance (bypassing your pending balance).
    4000000000000093   Charge succeeds and domestic pricing is used (other test cards use international pricing). This card is only significant in countries with split pricing.
    4000000000000010   The address_line1_check and address_zip_check verifications fail. If your account is blocking payments that fail postal code validation, the charge is declined.
    4000000000000028   Charge succeeds but the address_line1_check verification fails.
    4000000000000036   The address_zip_check verification fails. If your account is blocking payments that fail postal code validation, the charge is declined.
    4000000000000044   Charge succeeds but the address_zip_check and address_line1_check verifications are both unavailable.
    4000000000005126   Charge succeeds but refunding a captured charge fails asynchronously with a failure_reason of expired_or_canceled_card. Note that because refund failures are asynchronous, the refund will appear to be successful at first and will only have the failed status on subsequent fetches. We also notify you of refund failures using the charge.refund.updated webhook event.
    4000000000000101   If a CVC number is provided, the cvc_check fails. If your account is blocking payments that fail CVC code validation, the charge is declined.
    4000000000000341   Attaching this card to a Customer object succeeds but attempts to charge the customer fail.
    4000000000009235   results in a charge with a risk_level of elevated.
    4000000000004954   results in a charge with a risk_level of highest.
    4100000000000019   results in a charge with a risk_level of highest. The charge is blocked as it's considered fraudulent.
    4000000000000002   Charge is declined with a card_declined code.
    4000000000009995   Charge is declined with a card_declined code. The decline_code attribute is insufficient_funds.
    4000000000009987   Charge is declined with a card_declined code. The decline_code attribute is lost_card.
    4000000000009979   Charge is declined with a card_declined code. The decline_code attribute is stolen_card.
    4000000000000069   Charge is declined with an expired_card code.
    4000000000000127   Charge is declined with an incorrect_cvc code.
    4000000000000119   Charge is declined with a processing_error code.
    4242424242424241   Charge is declined with an incorrect_number code as the card number fails the Luhn check.
    
 Once the card number was used, a webhook handler would handle an error event, and send an email to admin and customer,
  informing them of this error.
 
 

 
 
   
  I tested my website on 5in and 6in phones, 10in tablet 18in laptop, and 22in desktop with good response from
  all of the devices.
  
   ## Version Control
   
   During development, I was naming my commits in a way, that it would make sense to any developer looking at 
   the work progress. ( hopefully...;-). At some instances where I could only see results of my fixes only 
   on the live server, mostly when testing webhooks from Stripe, the 
   commits might be a little bit vague...
   
   
  ## Deployment
  
  At the start of development, I created a GitHub repository and as I develop my app locally in PyCharm I 
  created a new Django Project in Pycharm, then I would use GitBash on my windows machine to cd into the
  project folder to initialize it.
  
  ```cl
   $ cd code/web-studio
   ```

  
  ```cl
   $ git init
   ```

Then I created remote to GitHub 
  
  ```cl
   $ git remote add origin-g https://github.com/marcelkolarcik/web-studio.git
   ```

Then I created a Heroku app by creating an account on Heroku first and then clicking on a new button in the top right corner
and selecting create a new app. Then I selected the app name (marcelli) and region Europe. Then I downloaded and installed the Heroku CLI. I set my environmental variables by clicking on settings in the top navigation and then on clicking on reveal config vars and I added my env variables like PORT, IP, SECRET_KEY, STRIPE KEYS, AMAZON KEYS, MAILGUN KEYS... 


I logged in using

 ```cl
   $ heroku login
   ```

Then I created a remote to Heroku using and from within my app folder I run

```cl
  $ heroku git:remote -a origin-h
```

Then I created requirements.txt by typing

 ```cl
  $ pip freeze --local >requirements.txt
   ```
So that Heroku knows what to install to run the app.

Then I created Procfile by 

```cl
  $ echo web:python app.py>Procfile
   ```

So that Heroku knows how to run my app.

To start dyno on Heroku I typed

```cl
  $ heroku ps:scale web=1 --app ( name of my app )
```

I also set Heroku to deploy from my GitHub repository. I first pushed my code to GitHub using GitHub remote, then I pushed code
to Heroku using Heroku remote and then in Heroku, I set the app to deploy from the master branch on GitHub, by clicking on deploy on Heroku app
and selecting deployment method as Github and by selecting repository I wanted to deploy from. And from this point, Heroku would
automatically deploy my app whenever I push new code to my master branch.

Heroku will also allow me to deploy apps from any branch I have created, which is very useful before merging a branch into the master to test it. I can do it by clicking on deploy in navigation and scrolling to the bottom of the page
and selecting the branch I want to deploy my app from.
 
Deploying to Heroku also allows me to test my application on multiple devices. 
  
#### Local Deployment

To locally run the code clone my repository

    $ git clone https://github.com/marcelkolarcik/web-studio.git

Install all packages from requirements.txt.

Make migrations with 

     manage.py makemigrations --dry-run
to see what migrations you are making, once everything is clear, run

    manage.py makemigrations
    
After that run 

    manage.py migrate --plan
    
To make sure, that you're doing what you want to do and then run

    manage.py migrate
    
Create superuser by

    manage.py createsuperuser
    
Add these products with prices into the products table from the admin section of the site
http://127.0.0.1:8000/admin/login

blog => 299

website => 999

online-store => 1999

If you want to be able to receive confirmation emails, you will need to set up an account with MAILGUN https://www.mailgun.com/ services
and follow easy instructions on how to use services. Set MAILGUN_KEY variable into environmental variables,
and use your test URL provided by MAILGUN.

You will need to create templates with templates_names and variables as per
checkout/views.py
appointments/views.py
freelancers/views.py

Please note that, when testing locally, you won't receive a confirmation email after purchase,
as the app is sending email after webhook from Stripe is sent, confirming the successful payment.

You will also need to mark appointment as paid for from within the admin, as we are marking
it as paid for after successful webhook from Stripe, and localhost is not receiving 
webhooks from Stripe.


    
To run the project run

    manage.py runserver
    
command
    
If you want to run tests run

    manage.py test
    
#### To fully experience the app, once you have all set-up ready you can follow these steps:
 
1. Create super user by running

        manage.py createsuperuser 
        
so that you can assign jobs to your freelancers.

2. Create an appointment as a client
3. Purchase any product with Project ID generated when you created an appointment, it will be in your dashboard
with your appointment. You won't be able to purchase anything without this appointment Project ID.
4. Log out, click on Freelancer? in the top navigation and create a freelancer account, by filling out 
freelancer registration form.
5. Log out.
6. log in as superuser by navigating to http://127.0.0.1:8000/admin/login
7. Find the order, copy its project number (a 32-bit string that will look something like this
'4AD953BCC9904D789DBE6E2DD700CAE6')
8. Paste it in the freelancer's Current project field and save.
9. Log in as a freelancer and you should see your client's information, job progress, and registration details.
10.  You can open a new private window by CTRL + SHIFT + N and log in as a client.
11. Now you can update job progress as a freelancer, and check progress as a client. You can also write some
messages back and forth through your notes text area as a freelancer and through your project text area as a client.

12. Until the job is done.



# Difficulties 
 Most challenges I encountered were with Stripe and testing the webhooks, as webhooks are sent to live site and not localhost,
 I had to push every little change to GitHub to see if my fix was working and that's why some of the commit messages 
 could be vague...

 
 # Future Features
 
As for the near future, I would like to implement a live link of the development site to clients, so that they can see 
their site being built, 
 
 # Browser support
   
   Currently supporting
   
   - Firefox
   - Chrome
   - Opera 
   - Edge   
  
 

# Acknowledgements

Thanks to my mentor Aaron Sinnott for support during my studies and for friendly advices...

I have used 
<a href="https://stackoverflow.com" title="https://stackoverflow.com">https://stackoverflow.com</a>
,<a href="https://stackoverflow.com" title="developer.mozilla.org">https://developer.mozilla.org</a> 
<a href="https://w3.org" title="w3.org">https://w3.org</a> 

for learning new things.

 
 
 





 



