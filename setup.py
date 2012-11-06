from setuptools import find_packages
from setuptools import setup


setup(
    name='slt.content',
    version='0.1',
    description="Provides content types for SLT shopping site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.sll.fi/kauppa',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['slt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.cart.shopping',
        'hexagonit.testing',
        'plone.browserlayer',
        'setuptools',
        'z3c.autoinclude',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
