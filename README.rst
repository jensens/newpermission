Example showing how to add new roles and permission in Plone

It also shows/describes the problems.

- Clone this, 
- bootstrap/ run buildout, 
- start zope, 
- create a plone site with New Permission profile applied.
- add a user ``newuser``,
- go to front-page and give ``newuser`` role ``New Role``,
- go to ``[...]front-page/manage_reportUserPermissions?user=newuser``

For me it does not show the ``Newpermission: Test Permission`` for ``newuser``. 
Role
``New Role`` was applied correctly.

In ZMI ``manage_access`` it's selected on portal-root, while it does not show i
up for front-page.

But it shows it for ``admin`` user.

So whats wrong?

