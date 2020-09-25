# Lens - Take a Look!

My personal resume and portfolio website.

---

### Main Tasks
- Finalize project description design
- Finalize project model
- Finalize page designs
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

### Tasks
- Update projects.admin models to allow for more intuitive project creation and editing (inlines for content models in change project view), use AdminPlus functionality
- Fix project page scroll padding so that the bottom of the project card above is not in view when a card's see more button is clicked
- Add button to download resume on resume page (and on home page?)


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
