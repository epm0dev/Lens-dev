# Lens - Take a Look!

My personal resume and portfolio website written with HTML, CSS, JavaScript and Python/Django. It is hosted on an AWS EC2 instance at [epm0dev.me](https://epm0dev.me). Static files are served from a AWS S3 bucket via AWS Cloudfront.

---

### Current Tasks
- Unit tests
    + lens/
- Finalize code documentation
    + lens/
- Replace filler text with final content
    + Home Page


### Known Bugs
- Some issues with animation timing on projects page when detail column needs to expand
    + When the window is already at the correct position for a project once the detail column is expanded and that project card's see more button is clicked, the subsequent animations are delayed.
    + When clicking the see more button in a project card near the bottom of the page, the window jumps slightly then scrolls rather than staying put
    + When clicking the see more button in a project card otherwise, there is a small stutter in the scroll animation

- When creating new projects via the admin page, you must first save the new project to the database before saving an associated content item to the database (i.e. you cannot save a new project and github content item at the same time, even though the github content item is displayed on the projects admin page via a stacked inline)


### Future Changes/Additions
- Add an 'old' or 'archived' field to the project model; when the field contains a value of true, the full project card is not displayed, but the user can still expand the detail column to see it's full details
- Create a blog page
- Create a photography page (or a way to post photographs in blog posts)


### Complete Before Deployment
- Setup email DKIM for django-ses (https://github.com/django-ses/django-ses)
- AWS IAM Setup
- Complete Django deployment checklist
- Migrate to PostgreSQL database backend
- Set up CRON job for github repo caching with django-background-tasks


### Complete After Deployment
- Update portrait
- Populate database with projects
