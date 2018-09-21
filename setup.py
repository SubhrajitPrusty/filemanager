from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except:
        pass

setup(name = 'filemanager',
    version = '1.0',
    description = 'Organize files in folders according to filetype',
    long_description=readme(),  
    long_description_content_type='text/markdown', 

    author='Subhrajit Prusty',  
    author_email='subhrajit1997@gmail.com',
    url = 'http://github.com/SubhrajitPrusty/filemanager',

    setup_requires=['setuptools>=40.0'],
    
    classifiers=[  
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='file manager manage order', 
    license = 'MIT',
    packages=find_packages(), 
    install_requires=['click'],
    entry_points="""
    [console_scripts]
        filemanager=filemanager:run
        """,
)