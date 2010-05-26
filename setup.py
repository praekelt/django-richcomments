from setuptools import setup, find_packages

setup(
    name='django-richcomments',
    version='dev',
    description='Django app extending the comments framework for RIA.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-richcomments',
    packages = find_packages(),
    include_package_data=True,
)
