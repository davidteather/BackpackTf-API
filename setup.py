from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'BackpackTF',         
  packages = ['BackpackTF'],   
  version = '0.0.1',      
  license='MIT',        
  description = 'The Unoffical Backpack.tf API Wrapper in Python 3.',   
  author = 'David Teather',                   
  author_email = 'contact.davidteather@gmail.com',     
  url = 'https://github.com/davidteather/BackpackTF-Python',
  long_description=long_description,
  long_description_content_type="text/markdown",  
  download_url = 'https://github.com/davidteather/BackpackTf-Python/tarball/master', 
  keywords = ['backpacktf', 'python3', 'tf2', 'unofficial', 'backpack.tf', 'trading-bot', 'api'], 
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.7'
  ],
)