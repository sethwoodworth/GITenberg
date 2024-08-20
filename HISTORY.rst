.. :changelog:

History
-------
0.8.7 (2024-02-13)
==================
* add all marc roles from PG
* update urllib3
* update repo lists
  * add 71848-72934
  * missing

0.8.6 (2023-10-11)
==================
* update urllib3
* update repo lists
  * add 71617-71847

0.8.5 (2023-09-27)
==================
* update cryptography and gitpython
* update repo lists
  * add 71227-71617

0.8.4 (2023-07-31)
==================
* try to stop making new when ratelimit comes in
* update repo lists
  * add 70402-71226

0.8.3 (2023-04-20)
==================
* fix opening rdf files and reading mod date
* update repo lists
  * add 69347-70401

0.8.2 (2022-12-07)
==================
* fixed long authorname issue
* update repo lists
  * add 69024-69346
* update some dependencies

0.8.1 (2022-09-26)
==================
* changed deprecated rdflib method
* download a single rdf file if not in library
* update repo lists
  * add 67825-69023
  * missing

0.8.0 (2022-04-13)
==================
* Update all dependencies to support Python 3.7 and 3.8
* fix making new config files with py3
* handle lists in pandata string fields
* rdflib-jsonld is now part of rdflib
* update repo lists
  * add 66543-67824

0.7.8 (2021-10-23)
==================
* update repo lists
  * add 66264-66542
  * missing
* allow gitberg all to have only one #, print its resulting repo names

0.7.7 (2021-09-15)
==================
* update repo lists
  * add 65660-66263
  * missing
* update requirements

0.7.6 (2021-06-11)
==================
* update repo lists
  * add 64913-65559
  * missing
* update requirements

0.7.5 (2021-03-25)
==================
* update repo lists
  * add 63880 - 64912
  * missing
* update requirements

0.7.4 (2020-11-25)
==================
* update repo lists
  * add 62775 - 63879
  * missing


0.7.3 (2020-08-01)
==================
* update repo lists
  * add 61334-62774
  * missing
* switch to using github personal access tokens

0.7.2 (2020-02-06)
==================
* updated appdirs dependency to resolve conflicts
* add __str__ method to pandata
* update repo lists
  * add 61121-61334
  * missing
  * removed
  
0.7.1 (2020-02-06)
==================
* updated requirements
  * pyepub has been factored into gitberg-autoupdate

0.7.0 (2020-01-17)
==================
* update repo lists
  * add 60078-61120
* clean up dependencies in setup.py
* fix many problems with py 3 compatibility
  * print function
  * unicode vs. str
  * read binary
  * dictionary iterators
  * function iterators
  * imports
  

0.6.3 (2019-08-12)
==================
* update repo lists
  * add 59371-60077
* update pyparsing requirement

0.6.2 (2019-05-02)
==================
* update repo lists
  * add 58592-59370
* handle missing ids in new command
* add .sib, .mus, .mxl to audiofile list
* update requirements
* fix bug setting _repo_name rebuilding a deleted repo with a previously assigned slug

0.6.1 (2019-01-01)
==================
* added -f option to "library" command, which forces an rdf library update
* "new" command includes rdf library update
* update repo lists
  * add 58309-58591
* fix an issue caused by control characters in metadata
* stop excluding mp3 in rsync


0.6.0 (2018-11-20)
==================
* add auto-updating of the rdf library - use "library" command, which now reports number of repos in the local library, not the list of repos
* add "new" command to facilitate regular addition of books from PG
* update repo lists
  * add 58152-58308
* fix a bug where the config global gets wiped before use
* delint

0.5.5 (2018-10-23)
==================
* update repo lists
  * add back ____ repos with new names
  * add 57972-58151
  * remove 3 junk repos
* fix mod_date bug when repo has no ebook file
* add list of files to remove
* addfiles action. To use this, 
  1. clone
  2. add files by hand
  3. run addfiles
* fix filepath handling of repos 1-9
* improve commit messages


0.5.4 (2018-10-19)
==================
* wikidata occasionally lies about ids- now catching the exception
* improved README template to reflect that not all books are public domain
* update repo lists, removing audio and greek (will add back greek with better names)


0.5.3 (2018-10-15)
==================
* fixed some greek repo names that were all dashes
* added "rights_note" to description
* start using missing list when iterating a range of book numbers
* suppress some debug messages


0.5.2 (2018-10-04)
==================
* added handling for an api cache to avoid running out of github calls
* save an api call by caching github repo object in book
* added modification date methods for files in git and files in rdf
* book.meta is now always a BookMetadata object
* refresh_repo action checks rdf for revised files and revises repo
* "local" keyword also turns off wikidata
* updated repo list


0.4.4 (2018-09-24)
==================
* fixed issue where gitberg refused to use the metadata from metadata.yaml, esp. repo_name
* added "local" keyword that turns off github linking in Book objects (much faster!)
* misc bugfixes
* updated requirements, esp. bs4 and html5lib

0.4.2 (2018-09-05)
==================
* fixed issue with newly fetched books and setting correct repo_name
* fixed tests which broke other tests
* parse_book_metadata moved out of command-line script into book init
* this necessitated a more uniform handling of rdf_library config

0.4.1 (2018-08-31)
==================
* no more travis. that code lives on in gitberg-build, and ebook building stuff moves to gitberg-autoupdate
* smarter commit comments

0.3.5 (2018-08-26)
==================
* packaging
* bugfixes

0.3.3 (2018-08-17)
==================
* mostly updates to add travis files
* adds code to do ebook building for releases
* adds tagging
* update to github3 API. Needed to update openssl and crypto.
* fix problematic behavior setting pubdate to today if no pubdate

0.3.1 (2017-03-29)
==================
* mostly updates to add travis files
* adds code to do ebook building for releases
* adds tagging


0.2.4 (2016-03-16)
==================
* Rewrite of config, add redf_library to config
* Adds metadata and apply actions
* includes a repo list to facilitate repo walking
* merges gitenberg.metadata package
* uses metadata package to vastly improve repo naming
* misc bugfixes
* tweak packaging to placate elastic beanstalk
* update documentation
* added example notebooks

-------
0.0.10 (2015-09-12)
==================
* Refactors and moves tests
* Adds config file crossplatform using appdirs

0.0.9 (2015-07-27)
==================
* Adds clone command

0.0.8 (2015-07-26)
==================
* Adds missing requirement

0.0.7 (2015-07-26)
==================
* Fixes `python setup.py test` when packaged

0.0.6 (2015-07-26)
==================
* Makes bugfixes and changes for packaging.
* Scaffolds out new commands via docopt

0.0.4 (2015-07-25)
==================
* Formats package for PyPi release
