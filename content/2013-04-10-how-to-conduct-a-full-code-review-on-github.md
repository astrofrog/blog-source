Title: How to conduct a full code review on GitHub
Date: 2013-04-10 13:38
Category: Coding
Tags: Git, GitHub, Code Review
Author: Thomas Robitaille
Slug: how-to-conduct-a-full-code-review-on-github

Why we might want to do it
--------------------------

I think it's fair to say I'm addicted to using
[GitHub](http://www.github.com). I've used it so much in the last couple of
years that I don't understand/remember how we got any serious collaborative
coding done before. In particular, the ability to comment on code
line-by-line, having conversations, updating the pull requests, and merging
them with a single click is in my mind so much more rewarding and productive
than having to comment on a patch in an email discussion.

However, I occasionally want to do a full review of a package that someone
else has written, and comment on various parts of the code. While it is
possible to leave line-by-line comments on a commit-by-commit basis, GitHub
does not provide an official way to review the latest *full* version of a file
or package.

<!-- more -->

There are a few ways to conduct a full code review that I can think of:

1. Browse through the files, on GitHub or locally, and open new issues
  for anything we would like to comment on, copying and pasting the relevant
  code. Not ideal if we want to comment on 20-30 chunks of code or more!

2. Browse through the files on GitHub, and if we see a line we want to comment
  on, we can go to the *Blame* tab, and then find the last commit that
  modified that line, and comment on it. The issue with this is that we might
  want to comment on a chunk of code that was the result of several commits in
  which case this method breaks down.

3. Leverage the [pull request](https://help.github.com/articles/using-pull-requests)
  interface, with a little git-*fu*, to conduct a proper full code review.
  This is in my opinion the best approach, and in this post, I describe one
  way to do this. There may be more elegant ways, so please let me know if you
  have any suggestions!

How to do it
------------

Ideally, one could simply create an empty branch on GitHub, then set up a pull
request from ``master`` (or whatever branch you want to review) onto the empty
branch. However, as far as I can tell, you can't create completely empty
branches on GitHub - instead, we need our empty branch to have at least one
commit, which needs to match the first commit of the branch we want to review
(otherwise GitHub will complain that there is no common history).

So how we proceed depends on whether the first commit contains code that needs
to be reviewed, or if it is unimportant (for example, a lot of repositories
start with the addition of an empty README file).

### If the first commit is unimportant...

... then the situation is fairly easy. You first need to find out the commit
hash for the first commit in the repository, which you can do with:

    $ git rev-list --all | tail -1
    ec2287e5837386c54fbd082021530aa18c0dcf18

In the example above the hash is ``ec2287e5837386c54fbd082021530aa18c0dcf18``,
but this will be different for you. Now, create an empty branch containing
only that commit:

    $ git branch empty ec2287e5837386c54fbd082021530aa18c0dcf18

This will create, but not switch to, the empty branch. Next push your
``empty`` branch to GitHub:

    $ git push origin empty

Go to your repository on GitHub and click on the 'Pull Request' button at the
top right of the window:

![python versions]({filename}/images/code_review/pull_request_1.png)

Then set it up so that you are pulling the changes from ``master`` into
``empty``, as follows:

![python versions]({filename}/images/code_review/pull_request_2.png)

You can now enter a title and message for the pull request, and invite other
people to comment on the code. If you make changes to ``master``, you can
simply push the changes to GitHub as usual:

    $ git push origin master

which should cause the new commits to appear in the pull request. Once the
review is complete, you can just close the pull request (without merging), and
keep the empty branch for future reviews (or delete it).

### If the first commit is important...

... this makes things a little more complicated. The approach we'll take here
is to create two new branches - ``review``, containing the code to review, and
``empty``, containing no files - both of which contain a common and empty
first commit (which we will add). In this way, the two branches have a common
history, even though the ``empty`` branch has no files. We can set then set up
a pull request from ``review`` to ``empty``.

**Important disclaimer**: make sure that you make a backup of your repository,
and that there are no unsaved changes! If you follow these instructions, any
files that are not already in the repository *will* get deleted, as well as
any uncommitted changes! In fact, it might be safest to do this in a clean
clone of your repository, so that if anything goes wrong, you haven't affected
your usual work repository.

With that disclaimer in mind, go to the repository you want to do a review
for, and then create an empty branch that we will call ``review``

    $ git checkout --orphan review

This branch has no history, but the files should still be there and would be
added to the branch if we were to commit. However, you don't want to do this,
so remove all the files in the repository in the current branch by first
unstaging all the files:

    $ git rm -r --cached *

then removing them all:

    $ git clean -fxd

Note that any file that was not previously part of the repository will be
deleted for good, not just from this branch!

You should now have a nice and empty branch:

    $ git log
    fatal: bad default revision 'HEAD'

    $ git status
    # On branch review
    #
    # Initial commit
    #
    nothing to commit (create/copy files and use "git add" to track)

You are now ready to set up the review. You should first add a dummy commit
that contains no files:

    $ git commit --allow-empty -m "Start of the review"

Then create a new branch called ``empty`` that will contain only this commit:

    $ git branch empty

This will create a branch with the same empty commit, but will keep on the
``review`` branch. You can now merge in the changes from the branch we want to
actually review, say ``master``, into ``review``:

    $ git merge master

You will be asked to provide a merge commit message, and you can just leave
the default. Next push your ``review`` and ``empty`` branches to GitHub:

    $ git push origin review
    $ git push origin empty

Go to your repository on GitHub and click on the 'Pull Request' button at the
top right of the window:

{% img center /images/code_review/pull_request_1.png %}

Then set it up so that you are pulling the changes from ``review`` into
``empty``, as follows:

{% img center /images/code_review/pull_request_3.png %}

You can now enter a title and message for the pull request, and invite other
people to comment on the code. Make sure that you switch back to your
``master`` (or other) branch to implement the changes, and if you then want to
update the review pull request, you can switch back to ``review`` and merge
the latest changes from ``master``:

    $ git checkout review
    $ git merge master
    $ git push origin review

which should cause the new commits to appear in the pull request.

Epilogue
--------

As you can see, if the first commit in your repository is unimportant, things
are actually pretty straightforward. I'd love to hear if anyone has a better
way to deal with the case where we want to review all commits, including the
first. Finally, if any GitHub employees are reading this - please make it
easier for people to conduct full reviews! :)
