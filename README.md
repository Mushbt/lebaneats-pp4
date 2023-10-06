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
- Home page includes a navbar, main body and a footer.

<details><summary>See feature image</summary>

![Homepage](insert image here)
</details>

### Logo & Navigation
- Blog Logo.
- Fully Responsive.
- Switches to hamburger menu on small screens.
- Displayed on all pages.

<details><summary>See feature images</summary>

![Logo](insert image here)
![Navbar](insert image here)
![Hamburger Menu](insert image here)
</details>

### Footer
- Contains social media links and copyright.
- Displayed on all pages.

<details><summary>See feature images</summary>

![Footer](insert image here)
</details>

### Sign up / Register
- Allows users to register an account.
- Username and password are required but email is optional.

<details><summary>See feature images</summary>

![Register](insert image here)
</details>

### Login
- Users can login to create a recipe, edit their recipe, delete their recipe, like and comment on all recipes on the blog page.

<details><summary>See feature images</summary>

![Login](insert image here)
</details>

### Logout
- Allows the user to securely log out.
- Asks the user if they are sure they want to logout.

<details><summary>See feature images</summary>

![Logout](Insert image here)
</details>

### Blog
- The blog displays each post that has been created by the admin or user.
- Pagination is used to display 6 posts per page.

<details><summary>See feature images</summary>

![Blog](Insert image here)
</details>

### Create Post
- Allows registered users to create recipe posts that will be viewed on the blog page once the admin has authorized it.
- User will add the recipe name, difficulty, length, ingredients and instructions.

<details><summary>See feature images</summary>

![Post](Insert image here)
</details>

### Edit Post
- Allows registered users to edit their own recipe posts incase they have forgotten anything or want to just remove something.

<details><summary>See feature images</summary>

![Edit](Insert image here)
</details>

### Delete Post
- Allows registered users to delete their own recipe posts incase they don't want it on the blog anymore.

<details><summary>See feature images</summary>

![Delete](Insert image here)
</details>

### Like
- Allows registered users to like any recipe posts they see on the blog page.

<details><summary>See feature images</summary>

![Like](Insert image here)
</details>

### Comment
- Allows registered users to comment on any recipe posts they see on the blog page.
- All comments must be authorized by the Admin to avoid any negativity.

<details><summary>See feature images</summary>

![Comment](Insert image here)
</details>

### Social Media Links
- A clickable logo for all the social media platforms provided.
- All links open in a new tab for better user experience.
- Displayed on all the pages of the site.

<details><summary>See feature images</summary>

![Social Media](Insert image here)
</details>

### Pagination
- Pagination is used on the blog page
- It ensures the page is kept tidy as it only allows for 6 recipe posts per page.

<details><summary>See feature images</summary>

![Pagination](Insert image here)
</details>

##### Back to [top](#table-of-contents)
<hr>

## Validation

### HTML Validation
The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="insert image here">
</details>

<details><summary>About</summary>
<img src="insert image here">
</details>

<details><summary>Blog</summary>
<img src="insert image here">
</details>

<details><summary>Share a recipe</summary>
<img src="insert image here">
</details>

<details><summary>Register</summary>
<img src="insert image here">
</details>

<details><summary>Login</summary>
<img src="insert image here">
</details>

<details><summary>Logout</summary>
<img src="insert image here">
</details>

<details><summary>Add recipe</summary>
<img src="insert image here">
</details>

<details><summary>Edit recipe</summary>
<img src="insert image here">
</details>

<details><summary>Delete recipe</summary>
<img src="insert image here">
</details>

### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="insert image here">
</details><hr>

### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle as PEP8online was down

<details><summary>Tool used: Pycodestyle</summary>
<img src="insert image here">
</details>

<hr><summary>Lebaneats</summary><hr>

<details><summary>urls.py</summary>
<img src="Insert image here">
</details>

<hr><summary>Blog</summary><hr>

<details><summary>admin.py</summary>
<img src="Insert image here">
</details>

<details><summary>forms.py</summary>
<img src="Insert image here">
</details>

<details><summary>models.py</summary>
<img src="Insert image here">
</details>

<details><summary>urls.py</summary>
<img src="Insert image here">
</details>

<details><summary>views.py</summary>
<img src="Insert image here">
</details>

### Lighthouse

Performance, best practices, and SEO were tested using Lighthouse.

#### Desktop

<details><summary>Index</summary>
<img src="insert image here">
</details>

<details><summary>About Us</summary>
<img src="insert image here">
</details>

<details><summary>Blog</summary>
<img src="insert image here">
</details>

<details><summary>Register</summary>
<img src="insert image here">
</details>

<details><summary>Login</summary>
<img src="insert image here">
</details>

<details><summary>Logout</summary>
<img src="insert image here">
</details>

<details><summary>Create recipe</summary>
<img src="insert image here">
</details>

<details><summary>Edit recipe</summary>
<img src="insert image here">
</details>

#### Mobile

<details><summary>Index</summary>
<img src="insert image here">
</details>

<details><summary>About Us</summary>
<img src="insert image here">
</details>

<details><summary>Blog</summary>
<img src="insert image here">
</details>

<details><summary>Register</summary>
<img src="insert image here">
</details>

<details><summary>Login</summary>
<img src="insert image here">
</details>

<details><summary>Logout</summary>
<img src="insert image here">
</details>

<details><summary>Create recipe</summary>
<img src="insert image here">
</details>

<details><summary>Edit recipe</summary>
<img src="insert image here">
</details>

##### Back to [top](#table-of-contents)
<hr>

## Testing

### Manual Testing

1. As a Site User I can view a list of posts so that I can select one to read

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

2. As a Site User I can click on a post so that I can read the full text

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

3. As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

4. As a Site User / Admin I can view comments on an individual post so that I can read the conversation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

5. As a Site User I can register an account so that I can create, edit, delete a post as well as liking and commenting on other posts

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

6. As a Site User I can leave comments on a post so that I can be involved in the conversation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

7. As a Site User I can like or unlike a post so that I can interact with the content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

8. As a Site Admin I can approve or disapprove user posts so that I can manage my blog content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

9. As a Site Admin I can create draft posts so that I can finish writing the content later

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

10. As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

11. As a Site User I can create a post so that other site users can view it

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

12. As a Site User I can edit my post that I have created so that I can add or remove anything I have forgotten or added by accident

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

13. As a Site User I can delete my post so that other site users cannot see it

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

14. As a Admin I can approve posts so that I can manage by blog content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

15. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

16. 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

17. As a Site Owner I can provide pagination so that users have better user experience while on the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

18. As a Site Owner I can provide an about us page so that the user can get information on what the site or content is about

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

19. As a Site Owner I can provide a fully responsive site so that users have a good user experience

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

20. As a Site User I am notified when I post, edit and delete a post or when I register, login or logout of my account so that I know if my intended action was successful

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

21. As a Site User I can login so that I can have access to all functions of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

22. As a Site User I can logout so that I can secure my account on the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>

23. As a Site User I can navigate easily through the site so that I can move between the different features of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Blog' link in the navigation bar | Blog will load| Works as expected |
| Click on any 'Post' on the blog page | Post will open up| Works as expected |

<details><summary>See feature images</summary>

![](Insert image here)
</details>


### Device Testing & Browser Compatibility

## Bugs

### Heroku Deployment

### Fork Repository

### Clone Repository

## Credits

### Images

### Code

## Acknowledgements