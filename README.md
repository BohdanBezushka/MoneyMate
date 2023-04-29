# **MoneyMate** 💰 🟪

[*Link to the live website.*](https://moneymate.herokuapp.com/)

MoneyMate is a full-stack, responsive website built for users who want to keep track of their expenses

This project focuses on providing users with an application for recording their expenses and saving money. To add a new expense or income, the user enters the date, amount, category or source, and can optionally add a description. The app constantly displays the user's total expenses, income, and balance.

![Responsive Design MoneyMate](https://user-images.githubusercontent.com/94321555/234986885-6fb6f418-0550-4325-8bd8-11a01982f2f5.png)
_________
## Table of Contents
* [Agile Methodology](#agile-methodology)
* [User Experience - UX](#User-Experience---UX)
  * [Site Goals](#Site-goals)
  * [User Stories](#User-Stories)
  * [Design](#Design)
    * [Colour Scheme](#Colour-Scheme)
    * [Icons](#Icons)
    * [Typography](#Typography)
    * [Wireframes](#Wireframes)
    * [Flowchart](#Flowchart)
    * [Database Schema](#Database-Schema)
* [Features](#Features)
  * [Favicon](#Favicon)
  * [Introduction page](#Introduction-page)
  * [Option 2](#Option-2)
  * [Features Left to Implement](#Features-Left-to-Implement)
* [Technologies Used](#Technologies-Used)
  * [Languages](#Languages)
  * [Software](#Software)
  * [Imported Libraries and Packages](#Imported-Libraries-and-Packages)
* [Testing and Validation](#Testing-and-Validation)
* [Bugs](#Bugs) 
* [Unfixed Bugs](#Unfixed-Bugs)
* [Deployment](#Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Heroku Deployment](#Heroku Deployment)
* [Credits](#Credits)
  * [Information Resources](#Information-Resources)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

_______
## Agile Methodology
The plan for this project was carried out using Agile Methodology. GitHub Issues, which can be viewed [here](https://github.com/BohdanBezushka/MoneyMate/issues), were used to record the User Stories, Bugs and Developer Task. These were categorised into 5 Epics/Milestones and organized into 3 Projects/Sprints.

Each User Story includes Acceptance Criteria and Tasks that are necessary for a clear and effective approach to the project, ensuring that the minimum project requirements are met.

The MoSCoW Method of Prioritisation was also used, classifying each User Story as a "Must Have", "Should Have", "Could Have" and "Wont't have". Also, the labels "Fix bug" and "Project Task" were added for better organization.

<details>
<summary>Screenshot Images of Issues, Labels, Milestones/Epics, and Projects/Sprints.</summary>

        Open Issues
![Open Issues](https://user-images.githubusercontent.com/94321555/234987534-e13f49d4-16f4-4653-8edc-89ef1ac87626.png)

        Closed Issues
![Closed Issues](https://user-images.githubusercontent.com/94321555/234987740-2349ded4-d0bf-44b7-8d61-5104f3c86b82.png)

        Labels
![Labels](https://user-images.githubusercontent.com/94321555/234987891-4fd4ad5b-5df7-409b-a836-ab771a936b88.png)

        Open Epics
![Open Epics](https://user-images.githubusercontent.com/94321555/234988023-4d97b590-d207-49d2-8c5a-e983750ab56e.png)

        Closed Epics
![Closed Epics](https://user-images.githubusercontent.com/94321555/234988175-7cb69ee7-05ca-4ca0-8ce7-e44b059d3927.png)

        Add Issue
![Add Issue](https://user-images.githubusercontent.com/94321555/234988581-3d650982-e411-433b-912f-30eb81fc5780.png)

        Sprints
![Sprints](https://user-images.githubusercontent.com/94321555/234988829-01605087-3bc4-47bd-981c-45c1a556ae94.png)

        Sprint 1
![Sprint 1](https://user-images.githubusercontent.com/94321555/234989224-47e45377-6c39-41f9-9dda-acde28343c5d.png)

        Sprint 2
![MoneyMate](https://user-images.githubusercontent.com/94321555/234989340-b2286cee-ec55-4a6a-b4ad-abb9f12e026f.png)

        Sprint 3
![Sprint 3](https://user-images.githubusercontent.com/94321555/234989663-5ca3823c-af8b-49b6-b62d-f3b652da5204.png)

</details>

I am new to using Agile methodology, and I have a positive opinion of it. The detailed and organized approach to completing tasks in order to achieve a minimum viable product is particularly helpful in speeding up work and reducing confusion when feeling disoriented. However, upon reflection, I realized that I need to improve the clarity of my User Stories and make them more concise. Additionally, for future projects, I intend to establish Milestones/Epics better and break them down into more detailed actions with tighter time constraints.

[Back To Top](#table-of-contents)
_______

## User Experience - UX

### Site Goals

MoneyMate aims to help users manage their finances effectively. It provides users with detailed information about their spending habits and helps improve their overall financial health. With MoneyMate, users can easily track their expenses and income.The target audience for MoneyMate is any user looking for a simple and efficient way to manage their finances. It is particularly suited for individuals who want to improve their financial literacy and learn more about managing their money effectively.

### User Stories

This section aims to determine what a user would expect from interacting with the website. Each User Story was recorded in [GitHub Issues](https://github.com/BohdanBezushka/MoneyMate/issues). Scenarios of actions each type of user, including the business owner, wishes to take are listed below.

**As a Business Owner:**
* I would like the user to have a homepage to understand what our application is about.
* I would like the user to be able to read reviews from other users.
* I would like the user to have a contact section so that they can get in touch with us.
* I would like the user to know about our customer service.
* I would like the user to have access to our social media so that they can stay informed about the latest news.
* I would like the user to be able to create an account to save their records of expenses and incomes.
* I would like to provide the user with the ability to register, view, edit, and delete their expenses.
* I would like to provide the user with the ability to register, view, edit, and delete their incomes.
* I would like the user to be able to view, create, edit, and delete their categories and sources.
* I want to provide the user with the ability to view the total expenses, incomes, and balance in real-time.

**As a User**
* I can see the website's logo and links at the top of the page so that I can easily navigate to other parts of the website.
* I have access to the company's phone and email contacts, as well as their public opening hours, so that I can easily reach out to them for assistance, queries, or feedback.
* I have the option to follow the company's social media accounts, which allows me to stay informed about their latest news and updates.
* I can create an account to start recording my expenses and savings.
* I can add new expenses and incomes, as well as view, edit, and delete them as needed.
* I have access to pre-established categories and sources for recording my expenses and incomes.
* I can view, edit, delete, and add new categories and sources as needed.
* I can check my total expenses, incomes, and balance in real-time whenever I need to.
* I can log out and when I log back in, my saved data will still be there.
* I can use my username and password so that I can login to my user account.
* I can log in to my profile so that I can access my information and view my details.

**As a Developer**
* I can add a favicon to the tab with website's title so that it gives users more visual feedback when looking at their tabs on their browser.
* I can automate user profile creation upon registration so that the admin doesn't have to do it manually every time a new user is registered.
* I can have placeholder text in the profile form so that users have a better experience filling in their forms.
* I can choose to enable the 'remember me' option, which allows the user to stay logged in without having to enter their login details every time.
* I am able to give the user the ability to view, edit, delete, and add expenses, incomes, categories, and sources.
* I have the ability to establish categories and sources for every new user that registers in the application.

[Back To Top](#table-of-contents)

### Design

#### Colour Scheme

![MoneyMate Colors](https://user-images.githubusercontent.com/94321555/235207100-a1a4a31d-9a59-4caf-af17-1ee9992c4db1.png)

* The color `#5D21D5` is the main color of the project, and we want the user to identify it as the brand's own color. It is predominantly used on the first page that the user sees to add color to the backgrounds, text, and buttons. It is also used for the login, logout, and new account pages. Lastly, for the dashboard, I have reduced the use of this color and limited it only to certain buttons and the logo.
* The color `#FFD700` has little presence, only being used for the dashboard menu bar on the CSS hover effect.
* The color `#212529` has been used to provide a background for the sections of the dashboard. It is a color that helps the text and buttons stand out.
* The color `#228B22` is used for the '+' button and added as the background for the button that displays the total income.
* The color `#DC143C` is used for the '-' button and is also added as a background for the button indicating the total expenses.

#### Typography

The typography used throughout the project is 'Sen' because it is a versatile typeface that works well for both display and body text. Different weights and styles of 'Sen' are used in the project to distinguish more important parts from others or to highlight specific text.

![Google Fonts](https://user-images.githubusercontent.com/94321555/235213496-d0ddc9e5-20df-4927-9211-a8b866f3889e.png)

#### Icons

[Font Awesome](https://fontawesome.com/) social media icons were used for the Footer. They are used as interactive links and have an aria-label which gives the relevant information to screen readers to read out to the users. 

#### Wireframes

Below you can see the wireframes for the project. I decided to add corresponding styles and text to the wireframes, which made it quicker to write the HTML and CSS. The wireframes correspond to a laptop screen, and thanks to Bootstrap, it was almost unnecessary to write code for the different media queries.


<details>
<summary>MoneyMate Wireframes</summary>

        MoneyMate introduction page
![MoneyMate-PC](https://user-images.githubusercontent.com/94321555/235217241-13b415c1-1c6b-4736-a0c5-3e7f166fd44e.png)

        Login
![MoneyMate-Login](https://user-images.githubusercontent.com/94321555/235217717-30983e91-a681-4131-ac75-79565337e4bc.png)

        Sign up
![MoneyMate-Sign-up](https://user-images.githubusercontent.com/94321555/235217868-ad533bc0-f3e0-4e33-b2f0-bff1d58de22a.png)

        Dashboard
![MoneyMate-Panel](https://user-images.githubusercontent.com/94321555/235217976-cda912c2-76e2-42d4-b07e-324cfde8d0d8.png)

</details>

#### Flowchart

I created this flowchart prior to writing my code to have a clear understanding of the necessary implementation while programming. It effectively outlines the program's layout and structure, including where user input is required, where input validation occurs, and how to handle invalid input. The flowchart was created usingg [Miro](https://miro.com/). Next, you can go directly to Miro and view the diagram. I haven't included a screenshot because the free version doesn't allow downloading high-resolution files: [MoneyMate Flowchart](https://miro.com/app/live-embed/uXjVMOsZVtI=/?moveToViewport=-4505,-2258,8056,3786&embedId=182857515834)

#### Database Schema
I had trouble creating the database in this part because I wasn't sure what I would need for the project. In the following lines, a screenshot of the previous database schema will be shown, and then the current database will be displayed.

![MoneyMate database schema](https://user-images.githubusercontent.com/94321555/235221786-eb5010a1-fb0f-407a-a671-ed7e1539ea19.png)

The current Database Schema used for this project, four custom models have been implemented:

**The Expense Model** has a one-to-one relationship with the Django's User Model and consists of:

    - user
    - date
    - amount
    - category
    - description

**The Income Model** has a one-to-one relationship with the Django's User Model and consists of:

    - user
    - date
    - amount
    - origin
    - description
    
**The Category Model** has a one-to-one relationship with the Django's User Model and consists of:

    - name
    - user

**The Origin Model** has a one-to-one relationship with the Django's User Model and consists of:

    - name
    - user

**The Currency Model** has a one-to-one relationship with the Django's User Model and consists of (not currently used due to a bug issue):

    - user
    - currency
    - abbreviation
    - symbol
    
  [Back To Top](#table-of-contents)
  
  ## Features
  
  ### Favicon
  
Our favicon works to visually identify the webpage and help the user recognize it more easily when they have multiple tabs open in the browser. Additionally, it improves the image and branding of a webpage.

<details>
<summary>MoneyMate Favicon</summary>

        Favicon
![Favicon](https://user-images.githubusercontent.com/94321555/235268897-f527c2f9-d8a7-4cf7-a69f-2a4fc548b535.png)

</details>
  
### Introduction page

The navigation bar of our website is composed of a logo that serves as a link to the homepage. Below it are sections that provide information on how the website works, user reviews, and contact details. On the right side, there are two buttons, one for logging in and the other for registering in case the user doesn't have an account. Lastly, the footer provides quick access to the project's social media pages.
  
  <details>
<summary>Screenshots of the introduction website</summary>

        Navigation bar
![Navigation bar](https://user-images.githubusercontent.com/94321555/235269809-3abe8040-c97c-47f2-838d-6504093592d9.png)

        Call to action Part 1
![Call to action Part 1](https://user-images.githubusercontent.com/94321555/235270144-0efaa993-a4d2-4322-b3f6-a31d5f3a3818.png)

        Call to action Part 2
![Call to action Part 2](https://user-images.githubusercontent.com/94321555/235270261-c91437e4-7fb3-4169-aa34-85f1dac32eb7.png)

        How it works Section Part 1
![How it works Section Part 1](https://user-images.githubusercontent.com/94321555/235270381-2e12e691-7196-41d7-8f94-8a24894aae7c.png)

        How it works Section Part 2
![How it works Section Part 2](https://user-images.githubusercontent.com/94321555/235270439-7e215449-c496-468d-829c-8dd1a83b1e45.png)

        How it works Section Part 3
![How it works Section Part 3](https://user-images.githubusercontent.com/94321555/235270537-dec7aaed-62b7-4282-9baf-829bcb378794.png)

        Reviews Section
![Reviews Section](https://user-images.githubusercontent.com/94321555/235270690-7761f215-c321-4568-b8de-12a951bd0933.png)

        Contact Section
![Contact Section](https://user-images.githubusercontent.com/94321555/235270819-185ebaae-3309-4d27-9a90-3c7991f1d3ff.png)

        Footer
![Footer](https://user-images.githubusercontent.com/94321555/235270914-db842c6d-a81d-413f-8adc-2fd875ecb8ef.png)

        Copyright
![Copyright](https://user-images.githubusercontent.com/94321555/235271036-5af640e6-33c7-416a-9c04-3eb1515bb195.png)

</details>

### Dashboard

The dashboard is what the user will see when they log in or register as a new user. The user has a navigation bar at the top with the logo that links to the dashboard homepage. Then we have the option of "Menu" that also directs the user to the dashboard homepage, the "Expenses" option directs to the list of expense records that the user has added, the "Incomes" option directs the user to the list of income records that the user has added, the "Category" option directs the user to the list of categories used to categorize the expenses, and the "Origin" option directs the user to the list of origins used to categorize the incomes. Finally, on the right side, there is a button to log out. Below the navigation bar, there is a container that welcomes the user, but the text will change to indicate the user's current location based on the navigation bar options. On the right side, we have the "_" and "+" buttons for adding expenses or income. The buttons to add an expense or income will be available in the "Menu", "Expenses", and "Incomes" sections. Next, there is a container that reminds the user to register their own categories and origins, although there are pre-established categories and origins available when a new user registers. Finally, we have a container that is present in every section of the dashboard and displays the total sum of expenses, incomes, and balance.

<details>
<summary>Screenshots of the Dashboard/Menu</summary>

        Navigation bar
![Navigation bar](https://user-images.githubusercontent.com/94321555/235272777-8868a603-93f5-45fc-a5dd-e4e3c65949ee.png)

        Welcome, add expense or income Section
![Welcome, add expense or income Section](https://user-images.githubusercontent.com/94321555/235272856-7deb0b41-462f-4210-92eb-42e48e0302a9.png)

        Information Section
![Information Section](https://user-images.githubusercontent.com/94321555/235272885-1a80cc7d-9114-401a-b364-30cea82a6c33.png)

        Results
![Results](https://user-images.githubusercontent.com/94321555/235272937-061873d1-8fb1-4729-ad8c-2a27a8d3baa1.png)

</details>


<details>
<summary>Screenshots of the Dashboard/Expenses</summary>

        Without expenses
![Without expenses](https://user-images.githubusercontent.com/94321555/235273123-4a37b3b8-9973-46df-a763-5384eed205db.png)

        With expenses
![With expenses](https://user-images.githubusercontent.com/94321555/235273212-8797a9ff-b9ab-41e7-acfa-88cbf8024b37.png)

        Add expense
![Add expense](https://user-images.githubusercontent.com/94321555/235273368-9847d0d9-ba5c-4dda-a1de-c2ac5c7c8afd.png)

        Edit expense
![Edit expense](https://user-images.githubusercontent.com/94321555/235273443-7e64d671-b3c6-4a21-b827-9acb91bcdc0a.png)

</details>


<details>
<summary>Screenshots of the Dashboard/Incomes</summary>

        Without incomes
![Without incomes](https://user-images.githubusercontent.com/94321555/235273619-91b82690-1165-46f4-9686-1d24959313b2.png)

        With incomes
![With incomes](https://user-images.githubusercontent.com/94321555/235273721-224067b1-356c-4668-8462-6e6059d58ed4.png)

        Add income
![Add income](https://user-images.githubusercontent.com/94321555/235273753-3a16c033-5c1f-48f9-95f2-636ed3379c47.png)

        Edit income
![Edit income](https://user-images.githubusercontent.com/94321555/235273807-cf76c797-31ce-4a8b-a1d4-18f24e2790bb.png)

</details>


<details>
<summary>Screenshots of the Dashboard/Category</summary>

        Without categories
![Without categories](https://user-images.githubusercontent.com/94321555/235273977-d06e3056-4f48-4346-b80d-d637406185e4.png)

        With categories
![With categories](https://user-images.githubusercontent.com/94321555/235273866-e1cfd712-f857-45ed-8c29-988a0b9ef43d.png)

        Add category
![Add category](https://user-images.githubusercontent.com/94321555/235273893-e8689e1e-8f27-4114-a70d-43bc2b30bd73.png)

        Edit category
![Edit category](https://user-images.githubusercontent.com/94321555/235273922-6e86932a-9e3e-4add-a75c-01a94148d922.png)

</details>

