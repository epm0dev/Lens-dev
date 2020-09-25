from background_task import background
from github import Github
from projects.models import GithubContent
from pathlib import Path
from json import dump, load
from datetime import datetime, timedelta


# TODO Documentation
CACHE_DIR = Path(__file__).resolve().parent / 'cached'
DATETIME_FMT = '%x %X'


# TODO Documentation
def update_cached_repo(filepath: str, repo_url: str):
    with open(filepath, 'w') as json_file:
        g = Github('dc511c2abf43f2d17721c8f49433cec8e3f20386')
        repo = g.get_repo(repo_url[repo_url.index('epm0dev'):])
        contents = repo.get_contents("")
        root_dir = []
        for item in contents:
            root_dir.append({
                'type': item.type,
                'path': item.path,
                'url': item.html_url,
            })
        root_dir.sort(key=lambda x: x['type'])
        commit = repo.get_branch('master').commit
        repo_dict = {
            'last_cached': datetime.now().strftime(DATETIME_FMT),
            'url': repo_url,
            'root_dir': root_dir,
            'latest_commit': {
                'author': commit.commit.author.name,
                'date': commit.commit.author.date.strftime(DATETIME_FMT),
                'message': commit.commit.message,
                'sha': commit.commit.sha,
                'url': commit.html_url
            }
        }
        dump(repo_dict, json_file)


# TODO Documentation
@background(schedule=5)
def check_cached_repos():
    for repo in GithubContent.objects.all():
        repo_url = repo.repository_url
        json_path = CACHE_DIR / f'repository/{repo_url[repo_url.rindex("/") + 1:]}.json'
        with open(json_path, 'r') as json_file:
            from json import JSONDecodeError
            try:
                repo_json = load(json_file)
            except JSONDecodeError as jde:
                print(f'Error when decoding JSON file {json_path}')
                print(jde.msg)
            else:
                if 'last_cached' in repo_json:
                    update_cache_time = datetime.strptime(repo_json['last_cached'], DATETIME_FMT) + timedelta(hours=1)
                    if update_cache_time > datetime.now():
                        print(f'Repository at {repo_url} was last cached less than an hour ago, skipping')
                        continue
        update_cached_repo(json_path, repo_url)


# TODO Documentation
def get_repos():
    repos = []
    for repo in GithubContent.objects.all():
        repo_url = repo.repository_url
        json_path = CACHE_DIR / f'repository/{repo_url[repo_url.rindex("/") + 1:]}.json'
        with open(json_path, 'r') as json_file:
            from json import JSONDecodeError
            try:
                repo_json = load(json_file)
            except JSONDecodeError as jde:
                print(f'Error when decoding JSON file {json_path}')
                print(jde.msg)
            else:
                repos.append(repo_json)
    return repos
