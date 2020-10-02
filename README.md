# Lens - Take a Look!

My personal resume and portfolio website.

---

### Main Tasks
- Finalize project model
- Finalize page structure, CSS styling and animations
    + Home
    + Resume
    + Projects
    + Contact
- Finalize code documentation
    + lens/
    + contact/
    + projects/
    + resume/
    + static/css/
    + static/javascript/
- Replace filler content with final content
    + Home Page
    + Projects Page

### Tasks
- Update projects.admin models to allow for more intuitive project creation and editing (inlines for content models in change project view), use AdminPlus functionality
- Fix project page scroll padding so that the bottom of the project card above is not in view when a card's see more button is clicked
    + When project details opened, resize shadow box to fit new height of document
    + When project details opened, set z-index of repo items to be below shadow box so hover animation stops working
- Add button to download resume on resume page (and on home page?)
- Add portrait to home page


### Future Tasks
- Create a blog page


### Complete Before Deployment
- Serve static files with a CDN
- Optimize CSS and HTML
- Optimize JavaScript
- Extensive unit tests
- Black box tests
- Double check padding and margins to ensure proper alignment and size of content
- Setup email DKIM for django-ses (https://github.com/django-ses/django-ses)
- AWS IAM Setup
- Complete Django deployment checklist
- Create deployment script
- Set up django-background-tasks service for github repo caching
