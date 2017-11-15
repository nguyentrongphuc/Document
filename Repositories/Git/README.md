# GIT commands

## Clone repository
    git clone <url>

## Branches
    list all branch: git branch -a
    delete local branch: git branch -d <branch name>
    Create local branch: git checkout -b <branch_name>
    Push local branch to server: git push -u origin <branch_name>
    
    Checkout remote branch: git checkout -b <branch_name> --track origin/<branch_name>
    Change to another local branch: git checkout <branch name>
## GitK
    Use gitk to open external tools to review the changes, histories, ...
    
## State files
    *State a new file:*
        git add <file name>
    *State all the files:*
        git add .
    *Adds content from all *.txt files under Documentation directory and its subdirectories:*
        git add Documentation/\*.txt
        Note that the asterisk * is quoted from the shell in this example; 
        this lets the command include the files from subdirectories.
    *Considers adding content from all git-*.sh scripts:*
        git add git-*.sh
    *Commit files*
        git commit -m "Example commit message"
    *Rename a file*
        git mv file-one.html file1.html
    *Deleting files*
        git rm <file name>
        *example*
        remove 3 files: git rm --cached file1.txt file2.txt file3.txt
        remove folder: git rm --cached foldername
        remove folder with recursively: git rm --cache foldername -r
        make sure run git commit -m 'comments..' & git push after that
    *Push committed files*
        git push
    *Revert a file*
        git checkout -- <file name>
    *Unstage a file*
        git reset HEAD -- <file name>
        git checkout HEAD -- <file name>
    *Remove untracked files*
        git clean -f -x
    *Undo a commit*
        git reset --soft HEAD^
    *Edit last commit message*
        git commit --amend -m "<new message>"
    
## View commit log
    git log
    
## Back out of a merge ???
    git reset --merge ORIG_HEAD
    
## Resolve merge conflicts with tool
    git mergetool
    
## Fetch & Pull
    git fetch origin
    git pull --no-commit --rebase origin develop

## Merge changes from other branch (e.g. merge from master)
	  A---B---C topic ==> your current branch
	 /
    D---E---F---G master
    
    $ git fetch
    $ git merge origin/master

## Pull request on GitHub
    https://help.github.com/articles/creating-a-pull-request/
    https://help.github.com/articles/merging-a-pull-request/

    
## Stash files
    git stash list [<options>]
    git stash show [<stash>]
    git stash drop [-q|--quiet] [<stash>]
    git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
    git -c diff.mnemonicprefix=false -c core.quotepath=false stash save phuclocal
    git -c diff.mnemonicprefix=false -c core.quotepath=false stash apply stash@{0}
    
## config mergetool global
	git config --global --add merge.tool kdiff3
	git config --global --add mergetool.kdiff3.path "C:/Program Files/KDiff3/kdiff3.exe"
	git config --global --add mergetool.kdiff3.trustExitCode false

	git config --global --add diff.guitool kdiff3
	git config --global --add difftool.kdiff3.path "C:/Program Files/KDiff3/kdiff3.exe"
	git config --global --add difftool.kdiff3.trustExitCode false
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
