

from distutils.core import setup
setup(
  name = 'QuBuilders',         # How you named your package folder (MyLib)
  packages = ['QuBuilders'],   # Chose the same as "name"
  version = '0.0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'this is a python package help you to make n choice questions',   # Give a short description about your library
  author = 'Amirreza Zahraei',                   # Type in your name
  author_email = 'amir.reza.zahraei@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AmirrezaZahraei1387/QuBu',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AmirrezaZahraei1387/QuBu/blob/master/dist/qubuilders-0.0.6.tar.gz',    # I explain this later on
  keywords = ['Question', 'multiple choice questions', 'creating questions'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
          'hatchling',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)