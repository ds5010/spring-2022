
# git

Updating a repository from the command-line.

## References

* [github starter course](https://github.com/education/github-starter-course)
* [github cli](https://docs.github.com/en/github-cli) -- this ("gh") is not the same as "git"
  * if you're on a Mac, "git" should already be installed

## Cloning a repo

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

References: 

* [Clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Commits

After you make a change in to your local repository, you commit the changes and add a message

```
$ git commit . -m "I made a small but super-important change to such and such."
```
To check the status of current repo
```
$ git status
```
To review the commit history
```
$ git log 
```
To checkout a previous commit
```
$ get checkout <tag/branch/commit id>
```
To reset to a previous commit (and lose everything since then!)
```
$ get reset --hard <tag/branch/commit id>
```

References:

* [About commits](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits)
* [git-reset](https://git-scm.com/docs/git-reset)

## Branches

Branches allow you to develop outside the main branch.  This is good for experimenting and/or collaborating.

* `$ git branch`
  * list branches, including current branch
  * default branch is usually "main"
  * if you haven't created any branches, that'll be the only one
* `$ git branch demo`
  * create the "demo" branch
* `$ git checkout demo`
  * switch to the demo branch
* You need to specify the upstream for the branch before you can "push" or "pull"
* We're not going to be using the workflow for branches, at least not now.
* To merge a branch
  ```
  $ git commit . -m "I made a such-and-such a change"
  $ git checkout main
  $ git merge demo
  ```
* To delete a branch after merging
  * `$ git branch -d branch`
* To delete a branch without merging
  * `$ git branch -D branch`

References: 

* [git branch](https://git-scm.com/docs/git-branch) -- git-scm.com
* [Git branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) -- git-scm.com
* [About branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
* [Working with branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#working-with-branches)

## Update repository

You update the repository by "pushing to origin". This is okay if you're the only one working on the project.

```
$ git push origin main
```
If you've made a change, then you need first to commit
```
$ git commit . -m "I've made a such-and-such a change"  
$ git push origin main
```

## Pull requests

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
