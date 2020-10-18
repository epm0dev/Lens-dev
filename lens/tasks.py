from background_task import background
from github import Github
from projects.models import GithubContent
from pathlib import Path
from json import dump, load
from datetime import datetime, timedelta


# Specify the directory where repositories are cached as json files.
CACHE_DIR = Path(__file__).resolve().parent / 'cached'

# Specify the datetime format to use when caching and loading cached repositories.
DATETIME_FMT = '%x %X'


# A function which updates the cached data for the specified github repository.
def update_cached_repo(filepath: str, repo_url: str):
    # Open the file containing the repository's information.
    with open(filepath, 'w') as json_file:
        # Create a github object from the github package to access github repositories via the github api.
        g = Github('4374b8e478a0610e2cb184df85808137aee520c7')

        # Get the repository from the specified URL.
        repo = g.get_repo(repo_url[repo_url.index('epm0dev'):])

        # Store the contents of the repository.
        contents = repo.get_contents("")

        # Create a list to store the items in the root directory of the repository.
        root_dir = []

        # Iterate through all of the items in the repository contents.
        for item in contents:
            # Append a dictionary to the list of repository root directory items with the current item's type, path and
            # URL.
            root_dir.append({
                'type': item.type,
                'path': item.path,
                'url': item.html_url,
            })

        # Sort the contents of the root directory by type.
        root_dir.sort(key=lambda x: x['type'])

        # Get the latest commit to the repository.
        commit = repo.get_branch('master').commit

        # Build the final dictionary which contains all of the repository information to cache.
        repo_dict = {
            # Add the date and time when the repository was last cached (now).
            'last_cached': datetime.now().strftime(DATETIME_FMT),
            # Add the repository's URL.
            'url': repo_url,
            # Add the list of items in the repository's root directory.
            'root_dir': root_dir,
            # Add information about the latest commit to the repository.
            'latest_commit': {
                # Add the author, date, message, sha checksum and URL of the latest commit.
                'author': commit.commit.author.name,
                'date': commit.commit.author.date.strftime(DATETIME_FMT),
                'message': commit.commit.message,
                'sha': commit.commit.sha,
                'url': commit.html_url
            }
        }

        # Dump the dictionary containing the repository's information to the cache file.
        dump(repo_dict, json_file)


# An asynchronous background task which is executed every time the projects page is requested. When the method is first
# called, it is scheduled to be executed 5 seconds later.
@background(schedule=5)
def check_cached_repos():
    # Iterate through all of the github content items stored in the database.
    for repo in GithubContent.objects.all():
        # Store the URL of the repository.
        repo_url = repo.repository_url

        # Build the path of the json file where the repository is cached with the base cache directory and the end of
        # the repository URL (everything after the last forward slash in the URL).
        json_path = CACHE_DIR / f'repository/{repo_url[repo_url.rindex("/") + 1:]}.json'

        # Open the json file containing the github repository's information.
        with open(json_path, 'r') as json_file:
            from json import JSONDecodeError
            try:
                # Try to load the github repository information from the json file.
                repo_json = load(json_file)
            except JSONDecodeError as jde:
                # If there was an error when decoding the json file, print a message to standard output.
                print(f'Error when decoding JSON file {json_path}')
                print(jde.msg)
            else:
                # If the json file was successfully decoded, check when it was last cached.
                if 'last_cached' in repo_json:
                    # Add 30 minutes to the time when the repository was last cached. The repository should only be
                    # cached again if this time has passed.
                    update_cache_time = datetime.strptime(
                        repo_json['last_cached'],
                        DATETIME_FMT
                    ) + timedelta(minutes=30)

                    # If it has not yet been 30 minutes since the repository was last cached, skip updating the cached
                    # information.
                    if update_cache_time > datetime.now():
                        # Print a note to standard output and continue to the next iteration of the loop to skip
                        # updating its cached information.
                        print(f'Repository at {repo_url} was last cached less than 30 minutes ago, skipping')
                        continue

        # If the repository was last cached over 30 minutes ago, this function call will not be skipped and the json
        # file where the repository's information is stored is updated.
        update_cached_repo(json_path, repo_url)


# A function which returns all of the cached repositories in the cached repository directory.
def get_repos():
    # Create an empty list to store the repositories.
    repos = []

    # Iterate through all of the github content items stored in the database.
    for repo in GithubContent.objects.all():
        # Store the full url of the current repository.
        repo_url = repo.repository_url

        # Build the path of the json file where the repository is cached with the base cache directory and the end of
        # the repository URL (everything after the last forward slash in the URL).
        json_path = CACHE_DIR / f'repository/{repo_url[repo_url.rindex("/") + 1:]}.json'

        # Open the json file containing the github repository's information.
        with open(json_path, 'r') as json_file:
            from json import JSONDecodeError
            try:
                # Try to load the github repository information from the json file.
                repo_json = load(json_file)
            except JSONDecodeError as jde:
                # If there was an error when decoding the json file, print a message to standard output.
                print(f'Error when decoding JSON file {json_path}')
                print(jde.msg)
            else:
                # If the json file was successfully decoded, append the object to the list of repositories.
                repos.append(repo_json)

    # Return the list of repository objects.
    return repos
