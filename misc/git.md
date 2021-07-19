Download a repository with `git clone <URL>`

List all branches available to you locally with `git branch`

List all branches (local and remote) with `git branch -a`

Create a new branch with `git branch <BRANCH_NAME>`

Delete a branch with `git branch -d <BRANCH_NAME>`, this is "safe" and won't delete a branch with uncommited changes

Change to a branch with `git checkout <BRANCH_NAME>`

Add files you want to commit with `git add <FILE_NAME>`

Do a commit with `git commit -m "<MESSAGE>"`

Push with `git push` 

If you want to switch branches without commiting, `git stash`

Want to merge your branch with a master that has been updated so you can't automatically merge?
- `git checkout your_branch`
- `git fetch origin`
- `git merge origin/master`
- will tell you which files have merge conflicts
  - `<<<<<<<` indicates your branch edits
  - `=======` indicates end of the end of this section and beginning of edits from attempted merge
  - `>>>>>>>` end of attempted merge section
- fix merge conflicts and then add, commit and push

### Resources

- http://blog.danieljanus.pl/2021/07/01/commit-groups/
- https://sethrobertson.github.io/GitBestPractices/
- https://missing.csail.mit.edu/2020/version-control/