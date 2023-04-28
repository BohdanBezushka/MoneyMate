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
* [Flowchart](#Flowchart)
* [Colour Scheme](#Colour-Scheme)
* [Database structure](###Database-structure)
* [Features](#Features)
  * [Menu](#Menu)
  * [Option 1](#Option-1)
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


