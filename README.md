# Backup all your Github repos

This script downloads all of a user's Github repos (private and public)
and clone/fetch/pull all remote branches.

## Requirements:
* `PyGithub` Python module to access the Github API
* `GitPython` Python module to use `git`

## Example

1. Go to `github.com > Settings > Developer settings > Personal access tokens > Generate new token`. Make sure `repo`
is checked, and generate a token. Copy paste the token and keep it securely somewhere.
2. Install the dependencies
```
pip install PyGithub GitPython
```
3. Run 
```
python backup_github.py --token TOKEN --dest DEST
```
where TOKEN is your Github personal access token and DEST the location where you want your repos to be saved.
Acces to the git repo is done using SSH so you need to have SSH keys setup.
To restrict to backup to your repos (your account probably has access to your repos, but also repos from other collaborators) pass the `--user USER` argument to the script above to restrict the repos to `USER`'s repos.
