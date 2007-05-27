from distutils.core import setup
import os

# Please run
# python setup.py install

if os.path.exists('doc/mount.wikipediafs.1.gz'):
    df = [('/usr/share/man/man1/', ['doc/mount.wikipediafs.1.gz'])]
else:
    df = []    

setup(
    name = 'wikipediafs',
    author = 'Mathieu Blondel',
    author_email = 'mblondel@users.sourceforge.net',
    url = 'http://wikipediafs.sourceforge.net',
    packages = ['wikipediafs'],
    package_dir = {'wikipediafs':'src/wikipediafs/'},
    scripts = ['src/mount.wikipediafs'],
    data_files = df,
)