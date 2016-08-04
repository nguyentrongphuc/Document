# GIT commands

## Clone repository
    git clone <url>

## Create branch
    *Create local branch:*
        git checkout -b <branch_name>

    *Push local branch to server:*
        git push -u origin <branch_name>
## State files
    *State a new file:*
        git add <file name>
    *State all the files:*
        git add .
    *Adds content from all *.txt files under Documentation directory and its subdirectories:*
        git add Documentation/\*.txt
        Note that the asterisk * is quoted from the shell in this example; this lets the command include the files from subdirectories of Documentation/ directory.

    *Considers adding content from all git-*.sh scripts:*
        git add git-*.sh


## Commit files
    git commit -m "Example commit message"

## Rename a file
    git mv file-one.html file1.html

## Deleting files
    git rm <file name>
    *example*
    remove 3 files: git rm --cached file1.txt file2.txt file3.txt
    remove folder: git rm --cached foldername
    remove folder with recursively: git rm --cache foldername -r
    make sure run git commit -m 'comments..' & git push after that
## Push committed files
    git push

## Merge in changes in the same branch
    git pull --no-edit

## Merge in changes from other branch (e.g. merge from master)
    git pull origin master --no-edit

## Open a pull request on GitHub
    https://help.github.com/articles/creating-a-pull-request/

## Merge pull request
    https://help.github.com/articles/merging-a-pull-request/
## See list of remote branches
    git branch -a
    git branch -all
## Delete local branch
    git branch -d <branch name>
## Revert a file
    git checkout -- <file name>
## Unstage a file
    git reset HEAD <file name>
## Undo a commit
    git reset --soft HEAD^
## Edit last commit message
    git commit --amend -m "<new message>"
## View commit log
    git log
## Change to another branch (equivalent to "Update" action in Mercurial)
    git checkout <branch name>
## Back out of a merge ???
    git reset --merge ORIG_HEAD
## Resolve merge conflicts with tool
    git mergetool

## gitignore
    1. Create .gitignore file in your working directory
    2. copy text below into the file (just example)
        #OS junk files
        [Tt]humbs.db
        *.DS_Store

        #Visual Studio files
        *.[Oo]bj
        *.user
        *.aps
        *.pch
        *.vspscc
        *.vssscc
        *_i.c
        *_p.c
        *.ncb
        *.suo
        *.tlb
        *.tlh
        *.bak
        *.[Cc]ache
        *.ilk
        *.log
        *.lib
        *.sbr
        *.sdf
        ipch/
        obj/
        [Bb]in
        [Dd]ebug*/
        [Rr]elease*/
        Ankh.NoLoad
        Tracotour/node_modules/

        #Tooling
        _ReSharper*/
        *.resharper
        [Tt]est[Rr]esult*

        #Project files
        [Bb]uild/

        #Subversion files
        .svn

        # Office Temp Files
        ~$*

# References
    *Git official docs - https://git-scm.com/doc
    *Git workflow - https://www.atlassian.com/git/tutorials/comparing-workflows
    *Pull request - https://help.github.com/articles/using-pull-requests/
    *Git cheatsheet - git-cheatsheet-EN-white.pdf (https://www.git-tower.com/blog/git-cheat-sheet/)
