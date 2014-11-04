Internal Scoreboard
===================

Here lies the Django code for Hack@UCF's internal CTF team scoreboard, which is essentially a site to help the captain
eyeball point contribution and participation. The site can also be a source of 
[epeen](http://en.wiktionary.org/wiki/epeen) for its users. :)

The vocab used inside the site is as made as generic as possible so that this application can be forked for use by
any type of group that uses point-based contributions, with minimal modifications necessary.

Wish List
---------
Sampled from [https://github.com/HackUCF/research/issues/5#issuecomment-58429679](https://github.com/HackUCF/research/issues/5#issuecomment-58429679):

* Ability for users to self-report solves on public CTFs
* Ability for users to self-report assists or helps for the main solvers (some intellectual contribution)
* Scoring/sorting system - by assists, solves, category, etc
* Use OAuth for login
* Interface for creating a new CTF solve page with attributes, such as judge only (only judge can add people to solves. think CTF practice)
* Agree/disagree system: self-reported solves and assists can be agreed or disagreed with in a public forum. Certain problems can be locked to finalize the solve/assist list
* Disambigiuation of multiple solvers by a judge
* Every time a solve, assist, agree or disagreement is committed, the users must write a reason/justification
* Extra: user configuration - avatar, website
