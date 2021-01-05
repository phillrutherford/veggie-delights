<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome phillrutherford,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!


# Veggie Delights

My data centric development project is called Veggie Delights. I am creating an app fro vegeterian meals, recipes and cooking methods. 
Users will be able to add, edit and delete meals. My goal for this app is to simply offer users creative alternative vegetarian meals whilst allowing
them to share their ideas and creations with others.

## UX

* I wanted to keep the layout design and colour scheme simple for this project. I didnt want to overwhelm the user so i stuck with the white background with dark green boxes. 
This helped me keep everything very clear and readable for all users. The layout makes it a very easy to use application allowing all users to view the meals on offer, quickly 
access all recipes and methods and of course sharing their own meals efficiently. 
I used the Langar font for this project. I felt it was a unique font that still kept things simple and clearly readable. 

* All of the meals submitted will be viewed on the initial homepage. From here the user will be able to access each meal with quick dropdown showing the recipes and cooking methods.
Next to each meal will be an edit and delete button clearly outlined in its own colour. Underneath all of the meals will be the "Add your meal" feature which will direct the users to a form
where they will be asked to fill out the meal name, ingredients and instructions. From there they will submit the meal and it will appear at the bottom of the list on the homepage.

* The main target audience is of course vegetarians, however this app is not strictly focused on that group. In this generation we are finding a lot more people are experimenting with vegetarian
and vegan meals on ocassion. This app will offer those people an insight into some of the options available to them to be creative with their cooking methods and maybe add some variety into their diets.

* For this project I wanted to ensure that the user felt the app was very simple to navigate, this was my top priority and I believe that shows in the final product. I did think about adding accounts, 
making adding/editing/deleting meals a function only members who were logged in could use. I chose not to do this on this ocassion but its certainly something that i would consider adding if I were 
to do this again. 

### Wireframes

The wireframes I created for this project can be found in the wireframes folder. For this project I used Marvel to create some mock designs.

## Features

For this project I used materialize quite often. They have alot of good features and colour schemes on offer that really allow you to be creative.

1. The collapsible feature is a huge part of this application. Each meal has a dropdown feature that shows the Ingredients and Instructions. I did this to reduce clutter on the page and keep it 
presentable. 

2. I also used the card feature from materialize for my "Add your meal" page. This allowed to have a clear layout form for users to fill out the information required to add their
meal to the site.

3. The edit and delete buttons were used to give the user flexibility. This allows them to change any errors or typing mistakes they may have made when adding a meal.

Other features I would have liked to introduce would be to have the ingredients be presented as a list vertically in a bullet point format. Unfortunatley I did not habve time to do this for this
project. With the impact of covid and being someone who lives in a campervan I found wifi access extremely difficult and often found myself working outside of a Starbucks in january in Canada. 
Not ideal circumstances but moving forward this would be a key feature that I would alter. 

## Technologies used

For this project I used several different technologies.

* jQuery
    I chose to use jQuery for this project because I felt this simplified javascript I was implementing.

* Font Awesome
    I used font awesome to assist me in adding icons into the site to improve presentation.

* Materialize
    As I discussed previously Materialize has been hugely effective in enabling me to use several features to ensure the site is easy to use the information is laid out in a clear and concise way.

* Google Fonts
    Google Fonts is a useful tool to change the fonts throughout the project.


## Testing

Throughout this project I encountered several issues which I had to tackle. 
As with every project my first response was trial and error. By opening the site in the browser I could see exactly what was not happening and what it was i was wanting to achieve. Furthermore from there 
I would open the google chrome dev tools to locate the error.

* One scenario I had was a failing with jquery linking to my base.html causing the collapsible feature to be ineffective. I simply could not find the problem myself and in the end I asked my tutor to 
scan my work to see if he could locate the issue. In the end it turned out to be a typo where I had http:// instead of https:// something so small and simple yet difficult to find. In this case a 
pair of fresh eyes was all there was required in order to resolve the problem.

* Furthermore I had issues linking my css file. Using the {{ url_for }} method for the first in practice had me struggling to begin with. It was not the way I was familiar with and took me somne time 
to get used to it and understand the process. To fix the problem I went back over the course module videos to ensure I was taking the correct steps and I finally managed to get my css link working correctly.

* As this was my first real time using python it took some time for get to get comfortable. My first attempt confused me so much I just restarted the project completely and used the experience to help keep
my code more organised and easy to follow. 

* Using the jinja format has proven to be extremely beneficial to this project but that did not come easily. Where I have currently {% for meal in meals %} it was initially {% for meals in meals%} as I was 
not 100% sure where the words had to match up to begin with. The way I resolved this was revisiting the course material, as has been one of my most useful methods for debugging my coding errors. Admittidley 
I watched the videos several times before fully grasping the concept, after that I was able to sucessfully code correctly and get my app up and running.  

* An issue I am facing currently is that the flash function is not working for me. When adding/editing/deleting a meal I want to display a message of confirmation to the user as is written in my app.py file
however this is not working for me. I have gone through the course material on the section, ensured I have the correct files installed on my project (requirements.txt) and I have looked through the chrome 
dev tools and I am yet to find the issue. I hope to resolve this before submitting the project. I was able to fix this issue late on, I hadn't rendered the message in my base.html. This was pointed out to me 
by my mentor and once it was mentioned I was able to resolve it immediatley.

As a user I want to be able to add/edit/delete meals quickly. I was constantly testing these functions out myself and I sent my site to my girlfriend also. Trial and error played a huge part in being able to
complete these tasks. Being thorough in reading the code and testing in an array of ways was key to ensuring these functions are working correctly.

As a user I would also like to be able to find new vegetarian meal ideas and view the ingredients required and cooking instructions quickly. To achieve this I altered my layout to have all meals on the initial 
home page instead of having them on their own individual page. Adding the collapsible function reduced clutter kept the site tidy and easy to navigate helping the user reach their goal.

Finally I ran my code through a validator to check for any issues. 
For my app.py file I used http://pep8online.com/ and they found 4 errors in line spacing which I fixed and it now shows 0 errors.
My html I used https://validator.w3.org/ which found 7 errors but I was unable to understand what it was asking to change specifically.
For my CSS file I used https://jigsaw.w3.org/css-validator/validator and found 0 errors.
Furthermore I ran the lighthouse in the chrome dev tools. This gave me a score of 91.

## Deployment

For this project I deployed my app through Heroku. These are the steps I followed:
    1. Sign in to Heroku.
    2. Add a new app named "veggie delights"
    3. Under deployment method select "connect to github".
    4. Link the specifc github repo to the heroku app.
    5. Go to settings and then reveal config vars.
    6. Add the information from the env.py file.
    7. Scroll down to domain.
    8. You will see this message. Your app can be found at https://flask-veggie-delights.herokuapp.com/

To run this file locally:
    1. Follow this link to the github repository https://github.com/phillrutherford/veggie-delights
    2. Select code.
    3. Copy the url for the repository.
    4. In your chosen development environment open the terminal.
    5. Type git clone and then paste the url from step 3.


## Code

* The collapsible function for the meals is from Materialize - Javascript - collapsible.
* All of the colours are from Materialize - CSS - colour.
* The Buttons for adding/editing/deleting meals are from Materialize - Components - Buttons.
* I used jquery which was found alongside each function I used from Materialize.
* Several recipes and instructions were taken from an app called Centr.
* To build the input fields for users to add meals I used the text fields from Materialize - Forms - Text input.
* To build the database for the information stored for each meal/ingredients/instructions I used the mongo database.
* I added icons to the site from font awesome.
* I used a font from google fonts.


## Credits

### Content

The meal ideas came from a combination of my own personal likes and also from the centr app. 
The colour scheme was a design mix between myself and my girlfriend Kristin.


### Media

The icons featured are from Font awesome.

### Acknowledgements

Inspiration for this project initially stemmed from my personal enjoyment of cooking and creating new meals. From here I used the centr app to bulk up the content. The layout was inspired by the course material where I felt the layout and readability
were extremely clear and presentable. With the help of my mentor Jonathon on the coding side of the project and my girlfriend Kristin on the presentation side I was able to come up the end product as you see it.
