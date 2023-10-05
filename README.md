# Lebaneats | Lebanese Food Blog

![Am I responsive](Image here)

**Developer: Mustafa Habet**

[Visit live website](Link goes here)

## Table of Contents
 - [About](#about)
 - [User Goals](#user-goals)
 - [Site Owner Goals](#site-owner-goals)
 - [User Experience](#user-experience)
 - [User Stories](#user-stories)
 - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
- [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

### About
Lebaneats Food Blog is a fictional blog dedicated to Lebanese Food. Users can view other user's recipes and can create their own account to share a recipe of their own.
<hr>

### User Goals

- To explore Lebanese cuisine in the hope of trying new flavours.
- To find a new recipe or to find a variation of a recipe.
- To know what ingredients are used for a specific recipe.
- To see how a specific dish was made.
- To see how easy or hard a dish is to prepare.
- To see how long a dish will take to prepare.
- To be able to see other users reviews or comments on a specific recipe.
- To be able to share a recipe with others.

### Site Owner Goals
- Fully responsive.
- To provide a easy to navigate through blog.
- To share my own recipes.
- To allow users to share their own recipes.
- To allow users to review or comment on the different recipes.
<hr>

## User Experience

### Target Audience
- Users who enjoy cooking and experimenting with recipes at home.
- Users who are new to cooking or less experienced in the kitchen.
- Users who enjoy trying new foods, cuisines and unique recipes.
- Users who like to share their own variations of recipes.

### User Requirements and Expectations
- Fully responsive
- A welcoming design
- Simple to use and navigate through
- Social media

##### Back to [top](#table-of-contents)
<hr>

## User Stories

### Users

### Admin / Authorised User

### Site Owner

### Kanban & User Stories

<details><summary>Kanban</summary>
[images go here]
</details>

<details><summary>User Stories</summary>
[images go here]
</details>

##### Back to [top](#table-of-contents)
<hr>

## Design

### Colors
I chose the colors of the Lebanese flag as I thought this would compliment a Lebanese food blog which should be bright and colorful.
<details><summary>See color pallet and flag</summary>
<img src="">[Add image here]
<img src="">[Add image here]
</details>

### Fonts

### Structure

#### Site Pages
- The site consists of the following pages:
  - A Home page that is supposed to look like the Lebanese flag with a welcome message.
  - An About page that tells users what the blog is about and what to expect when it comes to Lebanese cuisine.
  - A blog page where recipes for different Lebanese dishes can be found. Registered users can also create, edit, and delete their recipes.
  - A Share a Recipe page where registered users can share their own recipes.
  - A Edit Recipe page where recipe owners can edit their posts.
  - A Register page where users can register to be able to access all functionality of the site.
  - A login page where registered users can login.
  - A logout page for users to logout from site once they are done. 

#### Database

- When creating the database structure schema for this project, I made use of the [dbdiagram.io](https://dbdiagram.io/) website. This online tool provided me with a visual platform to create and document the database schema, streamlining the planning and implementation process for the blog application's database.
<details><summary>Database Schema</summary>
<img src="">[Add image here]
</details>

#### User Model
The User Model is a builtin Django model which contains the following.
- user_id
- first_name
- last_name
- email
- password
- groups
- user_permission
- is_staff
- is_active
- is_superuser
- last_login
- date_joined

#### Post Model
The Post Model contains the following:
- title
- slug
- author(ForeignKey)
- updated_on
- instructions
- featured_image
- exerpt
- created_on
- status
- likes
- recipe_length
- recipe_difficulty
- ingredients
- is_approved

#### Comment Model
The Comment Model contains the following:
- post(ForeignKey)
- name
- email
- body
- created_on
- approved

### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="">[insert image here]
</details>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

##### Back to [top](#table-of-contents)
<hr>

## Features

### Home page

### Logo & Navigation

### Footer

### Sign up / Register

### Login

### Logout

### Posts

### Create Post

### Edit Post

### Delete Post

### Like

### Comment

### Social Media Links

### Pagination

## Validation

### Lighthouse

## Testing

### Manual Testing

### Device Testing & Browser Compatibility

## Bugs

### Heroku Deployment

### Fork Repository

### Clone Repository

## Credits

### Images

### Code

## Acknowledgements