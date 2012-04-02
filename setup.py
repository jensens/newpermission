from setuptools import setup, find_packages
import sys, os

version = '0.1'
shortdesc = 'Test newpermission'

setup(name='newpermission',
      version=version,
      description=shortdesc,
      long_description="",
      author='Jens Klein    ',
      author_email='jens@bluedynamics.com',
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
