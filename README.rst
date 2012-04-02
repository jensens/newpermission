Example showing how to add new roles and permsiiosn in Plone

It also shows/describes the problems.

- Clone this, 
- bootstrap/ run buildout, 
- start zope, 
- create a plone site with New Permission profile applied.
- add a user ``newuser``,
- go to front-page and give ``newuser`` role ``New Role``,
- go to ``[...]front-page/manage_reportUserPermissions?user=newuser``

For me it does not show the ``Newpermission: Test Permission`` for ``newuser``.
But it shows it for ``admin`` user.
And in ZMI it's selected on portal-root, while it does not show up for front-page.

So whats wrong?

