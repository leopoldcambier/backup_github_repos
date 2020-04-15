import github
import git
import os.path
import argparse

# Backup all of a user's Github repos
# It uses an access token to access a Github user git repos
# Then backup (clone + fetch + checkout/pull all branches on the remote) all repos in a given directory
#
# [1] `token` should be a Github Personal access token. Those tokens can be created in
#     Github.com > Settings > Developer settings > Personal access tokens > Generate new token
#     Enter a name, Make sure the `repo` scope is checked and save the token
#     Make sure you store your token securely. It gives access to all your private repos.
#
# [2] `dest` is the folder where all repos will be cloned and backed up.
#
# A given Github user can access a number of repos like
# user/repo1
# user/repo2
# ...
# friend1/repo1
# friend1/repo2
# ...
# friend2/repo1
# friend2/repo2
# This function will clone them under dest
#
# Example:
#
# $ python backup_github_repos --token ${token} --dest ${HOME}/backup/
#
# Will create (or update) repos at
#
# ${HOME}/backup/user/repo1
# ${HOME}/backup/user/repo2
# ${HOME}/backup/friend1/repo1
# ${HOME}/backup/friend1/repo2
# ${HOME}/backup/friend2/repo1
# ${HOME}/backup/friend2/repo2
def backup_github_repos(token, dest):

    print("Backuping all repos to {}".format(dest))

    # Access Github using the token
    g = github.Github(token)
    
    # Go through all private and public repos
    for repo in g.get_user().get_repos():
    
        # Fetch full name (user/repo) and ssh url
        url = repo.ssh_url
        name = repo.full_name
        directory = os.path.join(dest, name)
          
        # Initialize the git repo
        repo = git.Repo.init(directory)
    
        # If origin doesn't exist, create it
        if not ('origin' in repo.remotes):
            print("Creating origin remote from {}".format(url))
            origin = repo.create_remote('origin', url)
    
        # Fetch
        origin = repo.remotes.origin
        origin.fetch()
    
        # Go through all branches, checkout and pull
        for ref in origin.refs:
            branch_name = str(ref)[7:] # origin/branch/name
            print("Pulling branch {}".format(branch_name))
            head = repo.create_head(branch_name, ref)
            head.set_tracking_branch(ref)
            head.checkout()
            origin.pull()

# Usage: ./backup.py --token $GITHUB_TOKEN --dest ${HOME}/path/to/backup/dir
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backup Github Git repos.')
    parser.add_argument('--token', type=str, help='A Personal access token with repo scope at least')
    parser.add_argument('--dest', type=str, help='A directory where to store backup the repos')
    args = parser.parse_args()
    backup_github_repos(args.token, args.dest)
    
