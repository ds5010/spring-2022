
# git workflow

Example git usage in the vaccine collaborative-development project

## Workflow

```
git clone https://github.com/ds5010/vaccines.git
```
* First, change to the vaccines repo, then find out which branch I'm on and list all the others with the `-a` flag
```
cd vaccines
git branch -a
```
* This indicates that I'm on the main branch
* I'd like to synchronize my personal branch with the main branch...
```
git pull
git checkout my_dev
git merge main
```
* The first line assures that the main branch is "up to date" (i.e., in sync with the repository)
* The second line puts me in the `my_dev` branch
* The third line merges the main branch into my local branch
  * this command asks me to add a merge message
  * if there are no conflicts, I proceed
* Suppose I made changes to the TODO.md, which I'd like to propose to the group. 
  * I commit, push, then create a pull request.
```
git add .
git commit -m "Updated the todo list"
git push
```
* I commited the changes to the my_dev branch and pushed to the remote repository
* When I go to the github site, I see a yellow button that reads: "Compare & pull request"
