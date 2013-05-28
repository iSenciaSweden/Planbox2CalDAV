from distutils.core import setup

setup(
    name='Planbox2CalDAV',
    version='0.0.1',
    author='Christian Klemetsson',
    author_email='christian.klemetsson@isencia.com',
    packages=[
        'planbox2caldav',
    ],
    url='http://www.isencia.se/',
    license='LICENSE.txt',
    description='Synchronize Planbox tasks with CalDAV calendar.',
    long_description=open('README.txt').read(),
    install_requires=[
        "simplejson >= 2.0.9",
        "MySQLdb >= 1.2.3",
    ],
    entry_points={
        'console_scripts':[
            'planboxdav = planbox2caldav.planboxdav:main',
        ],
    },
)
