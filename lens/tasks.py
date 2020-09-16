from background_task import background
from projects.models import GithubContent
from pathlib import Path
from json import dump, load
from datetime import datetime, timedelta


# TODO Description
CACHE_DIR = Path(__file__).resolve().parent / 'cached'
DATETIME_FMT = '%x %X'


# TODO Description, Github API implementation
@background(schedule=5)
def check_cached_repos():
    for repo in GithubContent.objects.all():
        json_path = CACHE_DIR / f'repository/{repo.repository_url[repo.repository_url.rindex("/") + 1:]}.json'
        with open(json_path, 'r') as json_file:
            from json import JSONDecodeError
            try:
                repo_json = load(json_file)
            except JSONDecodeError as jde:
                print(f'Error when decoding JSON file {json_path}')
                print(jde.msg)
            else:
                if 'last_cached' in repo_json:
                    update_cache_time = datetime.strptime(repo_json['last_cached'], DATETIME_FMT) + timedelta(minutes=5)
                    if update_cache_time > datetime.now():
                        print(f'Repository at {repo.repository_url} was last cached less than 5 minutes ago, skipping')
                        continue

        with open(json_path, 'w') as json_file:
            repo_dict = {
                'last_cached': datetime.now().strftime(DATETIME_FMT),
                'url': repo.repository_url,
            }
            dump(repo_dict, json_file)
            print(f'Dumped {repo.repository_url} to JSON file {json_path}')
