# Backup all your Github repos

This script download all of a user's Github repos (private and public)
and clone/fetch/pull all branches.

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
