# Lens - Take a Look!

My personal resume and portfolio website written with HTML, CSS, JavaScript and Python/Django. It is hosted on an AWS EC2 instance at [epm0dev.me](https://epm0dev.me). Static files are served from a AWS S3 bucket via AWS Cloudfront.

---

### Main Tasks
- Add full project details to project model to be displayed in the detail column on the projects page
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

### Known Bugs
- When clicking the see more button in a project card near the bottom of the page, and when the detail column is not yet expanded, the window jumps slightly due to the height of the page resizing.


### Future Changes/Additions
- Add an 'old' or 'archived' field to the project model; when the field contains a value of true, the full project card is not displayed, but the user can still expand the detail column to see it's full details
- Create a blog page
- Create a photography page (or a way to post photographs in blog posts)


### Complete Before Deployment
- Add portrait to home page
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
