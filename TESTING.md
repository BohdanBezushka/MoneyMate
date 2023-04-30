
# Table of Contents

* [Code Validation](#Code-Validation)
  * [HTML](#HTML)
  * [CSS](#CSS)
  * [Python](#Python)
* [Lighthouse Testing](#Lighthouse-Testing)
* [Responsiveness Testing](#Responsiveness-Testing)
* [Browser Compatibilty Testing](#Browser-Compatibilty-Testing)
* [User Story Testing](#User-Story-Testing)
* [Features](#features-testing)

_____

## Code Validation

### HTML

HTML code was tested using the [W3C Validator](https://validator.w3.org/) via text input.  The HTML code was copied and pasted in from each page of the website's source code.In all templates, it has been indicated that there are errors related to Django's functionalities, therefore these errors have not been corrected as they are part of the code to make it work. The validator also indicates that links cannot be on top of buttons, but this error has not been corrected because we believe it is better for the user to be able to click anywhere on the button

<details>
<summary>Screenshots of errors:</summary>

        Django error:

![Django error](https://user-images.githubusercontent.com/94321555/235326159-7589f1a0-1073-4e78-bc87-5f06e33e47f8.png)

        Link error:

![Link error](https://user-images.githubusercontent.com/94321555/235326196-fe9f653f-2940-40d1-abf0-d26d1778821c.png)

</details>

[Back To Top](#table-of-contents)
_____

### CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via text input. 

<details>
<summary>Screenshot with results for the style.css file</summary>

      style.css:
![No Error Found](https://user-images.githubusercontent.com/94321555/235326346-d919b699-d200-4466-8a31-b0c4991b5cf0.png)

      Warnings:
![Warnings](https://user-images.githubusercontent.com/94321555/235326408-efa20c91-8a5f-4632-8b80-38749ec165c5.png)
</details>

[Back To Top](#table-of-contents)
______

### Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

<details>

<summary>Screenshots and results for all python files</summary>

Long lines in `settings.py` and `env.py` were cleared using `# noqa`. These were values by the Django generated AUTH_PASSWORD_VALIDATORS and the values for STATICFILES_STORAGE which were giving errors when separated into two lines.

**expensesapp**

      asgi.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235326706-326ddf9e-cf08-4a0d-8f9b-783d1b47cce2.png)
  
      settings.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235327855-32af1cdb-4291-4045-adfe-d1fedc4c3bf7.png)
  
       urls.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235327914-f5b25a5a-f92d-4837-9e77-c33b4c708fec.png)

       wsgi.py 
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235327968-eb5aa4db-ca7d-4802-aa4c-b12efdf40259.png)


**moneymate**
  
      admin.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328030-f96c34de-9c37-4d92-b725-8fde8d736e31.png)

      apps.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328084-e64dc6b9-ebcc-4332-be73-68c7bd8b34da.png)
  
      models.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328122-d4aa27e9-1bfd-4514-8971-30e0ea5243c5.png)

  
       signals.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328155-4d327143-6171-4969-a85e-95c7742281ea.png)
  
       views.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328203-06049a00-f993-4652-a04d-564fc8550a1e.png)


**manage.py**
  
      manage.py
  ![All clear, no errors found](https://user-images.githubusercontent.com/94321555/235328333-9f872195-4612-45e3-9403-b09430c30459.png)
</details>

[Back To Top](#table-of-contents)
_____

## Lighthouse Testing

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO.  This was run in Chrome DevTools in incognito mode. 

<details>
<summary>Screenshots and results for all pages</summary>

**Homepage**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329179-52439da0-7244-4457-9b65-dceb795afb5a.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329296-5b6b1417-c3b0-4643-b964-177a35aac577.png)

**Login**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329468-e05738f3-5234-4c2c-8c3f-dfe1d3279421.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329546-677f935a-d127-4938-ae48-b9d9ca00500c.png)

**Sign up**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329577-e68ff818-2efb-4d38-ab19-498ba66754fc.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329601-31686f1a-d72d-4809-ad8a-8d4e2fcc6717.png)

**Sign out**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329653-3d6f5ee8-3a53-4bd2-9836-42606ddc7107.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329682-b944485d-6d8c-4dbe-ac2c-a23d54df2ccf.png)

**Dashboard/Menu**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329741-1a722e08-70b2-4d17-8015-3f571d28d493.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329793-8d8aded8-2c1d-41ef-92de-002bede28380.png)

**Dashboard/Expenses**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329836-080a484b-1785-404b-90e2-6700c2180252.png)

    Desktop
 ![Passed](https://user-images.githubusercontent.com/94321555/235329878-f7a76b62-8851-4b5e-9218-d2b6af904fe0.png)
 
**Dashboard/Edit Expense**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235329948-65023b93-edb6-4086-b931-b7f260af8686.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235329968-7ca64238-1e69-4792-89d8-c7dd462946cd.png)

**Dashboard/Add Expense**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330010-b2ed52ae-af38-45e2-9687-be207e71653a.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330044-c47a1fbf-570f-44a5-a417-be070d96dcb2.png)
 
  **Dashboard/Incomes**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330107-83daed4f-7c16-4966-854e-d667d0f2a3c1.png)

    Desktop
 ![Passed](https://user-images.githubusercontent.com/94321555/235330124-ef435d53-f545-4b0e-a9b2-efcfec343dd5.png)

**Dashboard/Edit Income**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330155-92cc13b9-418d-422f-ad43-b09009c449c4.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330191-0ca00047-83fc-4b9e-a382-6111c39cd0ac.png)

**Dashboard/Add Income**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330227-0dcf5c87-e3fe-4dcf-bcb4-a437063c5223.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330258-b65e7412-7d12-4722-b0fa-cfe03b0e702d.png)
  
  **Dashboard/Category**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330335-56cd1daf-2bb6-4d6c-9142-9e78c7c7402b.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330366-d00ff3e4-7e2e-4da4-904d-7e24dd122da2.png)
  
**Dashboard/Edit Category**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330384-63d548e0-14ae-413a-9dcc-be8a9e9d3f2d.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330427-b79e0666-3b16-4708-be57-67f87483d9c2.png)

**Dashboard/Add Category**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330472-5dbc1194-c9a8-44e2-8510-519d0875fb5d.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330518-2c68d1c1-1ba5-41b1-af23-9aeaba6a880a.png)
  
    **Dashboard/Origin**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330581-bde0a0b6-7cac-4e24-99a9-de2e3ad86121.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330622-e2eceb43-375e-4987-94e8-c06eaa2a6070.png)

**Dashboard/Edit Origin**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330660-6c461e7e-1bf7-4288-959b-14b099eaff2d.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330682-49755e6e-ca85-4fcf-9a4f-9295989ac267.png)

**Dashboard/Add Origin**

    Mobile
![Passed](https://user-images.githubusercontent.com/94321555/235330718-44a5656a-a59f-45dc-a361-a02b35bf3f4d.png)

    Desktop
![Passed](https://user-images.githubusercontent.com/94321555/235330746-8f10405b-b1af-4817-83c6-cde6fe4e7538.png)

  
The following are the results for all pages:

| Page | Device | Performance | Accessibility | Best Practice | SEO |
| ---- | ------ | ----------- | ------------- | ------------- | --- |
| Homepage | mobile  |  95 | 95 | 83 |  100 |
|                               | desktop | 92 | 95 | 83 | 100 |
| Login | mobile  |  92 | 100 | 92 |  100 |
|                          | desktop | 88 | 100 | 92 | 100 |
| Sign up             | mobile  |  95 | 100 | 92 |  100 |
|                          | desktop | 100 | 100 | 92 | 100 |
| Sign out     | mobile  |  85 | 100 |  92 |  100 |
|                          | desktop | 100 | 100 |  92 | 100 |
| Dashboard/Menu        | mobile  |  90 | 87 | 92 |  100 |
|                          | desktop |  99 | 97 | 92 | 100 |
| Dashboard/Expenses      | mobile  |  95 | 82 | 92 |  100 |
|                          | desktop | 95 | 82 | 92 | 100 |
| Dashboard/Edit Expense       | mobile  |  95 | 85 | 92 |  100 |
|                          | desktop |  100 | 84 | 92 | 100 |
| Dashboard/Add Expense       | mobile  |  95 | 85 | 92 |  100 |
|                          | desktop |  99 | 85 | 92 | 100 |
| Dashboard/Incomes       | mobile  |  95 | 82 | 92 |  100 |
|                          | desktop |  100 | 82 | 92 | 100 |
| Dashboard/Edit Income       | mobile  |  95 | 85 | 92 |  100 |
|                          | desktop |  99 | 85 | 92 | 100 |
| Dashboard/Add Income       | mobile  |  95 | 85 | 92 |  100 |
|                          | desktop |  99 | 85 | 92 | 100 |
| Dashboard/Category      | mobile  |  95 | 95 | 92 |  100 |
|                          | desktop |  99 | 95 | 92 | 100 |
| Dashboard/Edit Category      | mobile  |  95 | 98 | 92 |  100 |
|                          | desktop |  98 | 98 | 92 | 100 |
| Dashboard/Add Category       | mobile  |  95 | 98 | 92 |  100 |
|                          | desktop |  100 | 98 | 92 | 100 |
| Dashboard/Origin     | mobile  |  93 | 98 | 92 |  100 |
|                          | desktop |  99 | 98 | 92 | 100 |
| Dashboard/Edit Origin      | mobile  |  94 | 98 | 92 |  100 |
|                          | desktop |  99 | 100 | 100 | 100 |
| Dashboard/Add Origin       | mobile  |  95 | 98 | 92 |  100 |
|                          | desktop |  98 | 98 | 92 | 100 |

</details>

[Back To Top](#table-of-contents)

_____

## Responsiveness Testing

The website is responsive for screens with a mininum width of 320px and a maximum width of 2560px. Friends and family tested the website on their devices and all reported no issues with responsiveness.  Further manual tests were done using Chrome's DevTools.

<details>

<summary>Screenshots of website at different screen sizes.</summary>

**Homepage**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235331847-a67d50ff-7da7-4951-ac4c-1733d0233275.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235331890-472bf0b9-7c4b-4d47-b005-b9c8ecfeae92.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235331976-970cf6f5-c050-4ec8-bdcd-b48ea4f7f597.png)

**Login**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332017-2f5f6296-b9c4-4094-9dcd-a49e3ef67a5f.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332040-36e1dcb3-4c94-4fde-8332-a5c668f6fd1f.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332052-acc03733-8e89-4375-b0fa-0df57aa996a2.png)

**Sign up**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332101-944e8939-0334-46f8-8c64-1aa455d05efc.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332118-2a5d473c-afab-4566-a306-60b690f30cd5.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332128-efd95110-5fe1-4541-8c41-6d8bfe2e5970.png)

**Sign out**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332145-38f1a307-67d7-4143-b97a-2e99b09cbcf9.png)


        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332156-035acb67-7b49-4b51-ba85-baedb5b84425.png)


        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332165-93d4c64e-af51-4492-9e20-e265b74852fa.png)

**Dashboard/Menu**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332199-759122c4-d676-4374-b1b7-ba0130c38c54.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332220-61da860f-0a64-46f1-9a62-9e0faef7d517.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332232-53510f65-3e28-4ef7-aec6-2433bd93290d.png)

**Dashboard/Expenses-Incomes**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332280-142978ec-33ff-4a33-a281-08efafb17438.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332294-2c025cec-6aca-4bae-9839-6c3bfa4f710e.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332301-62be7ffc-83ad-44d1-af65-6bb6237879a8.png)

**Dashboard/Category-Origin**

        Mobile 320px
![Mobile 320px](https://user-images.githubusercontent.com/94321555/235332336-e5fe5fe8-2baa-4b24-91b1-b5a8bdb01226.png)

        Tablet 768px
![Tablet 768px](https://user-images.githubusercontent.com/94321555/235332346-8fb93603-4db8-41d7-ba58-c1d0b0857582.png)

        Desktop 1200px
![Desktop 1200px](https://user-images.githubusercontent.com/94321555/235332358-83a6055b-8674-4720-afac-063fe1d1ed28.png)

</details>
[Back To Top](#table-of-contents)

_____

## Browser Compatibilty Testing

Website was tested on current Chrome, Firefox and Microsoft Edge for compatibility.

<details>

<summary>Table of the results:</summary>

| Intended      | Chrome | Firefox | Edge | Brave |
| ------------- | ------ | ------- | ---- | ----- |
| Appearance    | Good   | Good    | Good | Good  |
| Responsiveness| Good   | Good    | Good | Good  | 

</details>

[Back To Top](#table-of-contents)

_____



[Back To Top](#table-of-contents)

[Back to README.md](README.md)
