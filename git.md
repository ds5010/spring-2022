
# git

Version control for a software repository -- from the command-line.

## References

* [github starter course](https://github.com/education/github-starter-course)
* [github cli](https://docs.github.com/en/github-cli) -- this ("gh") is not the same as "git"
  * if you're on a Mac, "git" should already be installed

## Tags

Create tags on the command line or with the GUI -- you can diff tags

 | command | action |
 | ---     | ---    |
 | `git tag <tagname>` | Create a local tag on the current branch |
 | `git tag <tagname> -a` | Create a local annotated tag on the current branch |
 | `git push origin --tags` | Tags don't get pushed by default |
 | `git diff <tagname> | Line-by-line comparison: tag and current branch |

## Branches

* Branches allow you to develop outside of "main" (the main branch).
* Branches are good for experimenting and/or collaborating.
* Note: in the old days (last year), "main" was called "master"; you'll see docs refer to "master" instead of "main".

 | command | action |
 | ---     | ---    |
 | `git branch` | List and highlight the current branch (and any others you're working on) |
 | `git branch -a` | List **all** the branches (even those you're not working on) |
 | `git branch newb` | Create a new branch called "newb" (from whatever branch you're in) |
 | `git checkout demo` | Switch to the branch called "demo" (you'll get a "filespec" error if "demo" doesn't exist) |
 | `git branch -d newb` | Delete the "newb" branch (after merging any commits) |
 | `git branch -D newb` | Delete the "newb" branch (discarding any unmerged commits) |

* Ref: [Basic branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) -- git-scm.com

## Changes

 | command | action |
 | ---     | ---    |
 | `git diff` | Report line-by-line changes since last commit |
 | `git diff --name-status main` | Report differences (filenames only) between current branch and "main" |
 | `git diff main...newb` | Report differences between the "main" and "newb" branches |
 | `git diff newb main -- README.md` | Report differences for one file only: README.md |
 | `git log` | List commit history (these include the hashes that uniquely identify each commit) |
 | `git merge-base main newb` | Get point where the "newb" branch was created from the main (or best common ancestor) |

* ["Revert to a previous commit"](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit)
  * This is an old but very popular and informative stackoverflow post
  * github may have changed since then, but not so much for git
  * 11K upvotes for the answer
* ["Undo the most recent local commit"](https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git)
  * Also old (12 years)
  * 26K up votes
  * Discussion of HEAD

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

* `$ git checkout demo`
  * switch to the demo branch
* You need to specify the upstream for the branch before you can "push" or "pull"
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
These examples assume you're in the "main" branch.  Otherwise, replace "main" with the branch name.

```
git push origin main
```
If you've made a change, then you need first to commit
```
git commit . -m "I've made a such-and-such a change"  
git push origin main
```
If you've added a file (and maybe done other things), first stage, then commit
```
git add .
git commit -m "I've made a such-and-such a change"  
git push origin main
```

## Pull requests

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

## Clone a repo

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

References: 

* [Clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
