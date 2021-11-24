RelationDB
==========

RelationDB is an attempt at a modular database of objects that are taggable and support relations.

Development notes
-----------------

Dependencies
^^^^^^^^^^^^

- ``peewee``

Dependency handling + virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- currently using ``virtualenv venv``
- consider using poetry

Goal
----

There are technically several goals that I'm trying to achieve with this project, however, I want to put a lot of effort into making the project as modular and customisable as possible, so that it can have a wide variety of use cases.

My first and main goal is to be able to use this as a search engine for files in a similiar way to how boorus work. The idea is that a user will be able to add tags to files on their file system and then they'll be able to search for these files using the assigned tags. This should solve the problem with folder structure, where a file fits into several different folders, but due to how conventional file systems work, you can only put the file into one of them. You could of course create symlinks, but those can get quite messy rather quickly.

My secondary goal is to be able to use this as a database for people - a contact book. I could add one of my friend and create a relationship between them and me (two separate objects) to "friends". Then I could add their dad maybe if I know want to. In general, the end result could end up being a lot more powerful than what conventional contact books (such as Google Contacts) allow for. It should be noted, that some relationships can be one-sided. Reader can be a fan of author, but that doesn't me that the author is a fan of the reader. This would require directional relationships to be implemented.

I'm not expecting to be able to realise everything I've set out to do, however, my intention is to get as close as possible.

Checklist
^^^^^^^^^

- [ ] a modular front-end
	- [ ] shell
	- [ ] web GUI
	- [ ] REST API
	- [ ] filesystem integration
- [ ] a modular back-end
	- [ ] JSON
	- [ ] folder structure
	- [ ] SQLite
	- [ ] other SQL databases
- [ ] plugins
	- [ ] automatic tagging (creation date, id)
	- [ ] dynamic tags (current content, size)
- [ ] everything should be easily configurable through a centralised configuration system
- [ ] running under Docker