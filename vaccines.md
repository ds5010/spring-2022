
# Vaccines

Example notes for git usage in the vaccine collaborative-development project

## Workflow

```
git clone https://github.com/ds5010/vaccines.git
```
* Changes were made to `main` -- the main branch
* I need to sync my branch with the main branch
* First, find out which branch I'm on, and list all the others with the `-a` flag
```
git branch -a
```
* This indicates that I'm on the main branch
* I'd like to synchronize my personal branch with the main branch...
```
git pull
git checkout my_dev
git merge master
```
* The first line assures that the main branch is "up to date" (i.e., in sync with the repository)
* The second line puts me in the `my_dev` branch
* The third line merges the master into my local branch
  * this command asks me to add a merge message
  * there are no conflicts, so I proceed
* I made changes to the TODO list, which I'd like to propose to the group
```
git add .
git commit -m "Updating the todo list"
git push
```
* I commited the changes to the my_dev branch and pushed to the remote repository
* When I go to the github site, I see a yellow button that reads: "Compare & pull request"
