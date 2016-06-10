# Data extraction, cleaning, and formatting

Now that we've spent some time experimenting with tools designed for an interpretive, hand-crafted mode of GIS work, let's move to the other end of the spectrum and work with some larger data sets. As a test project, we're going to be extracting "toponyms" - place references - from novels. It would take weeks or months to do this by hand - we'd have to read the entire novel, highlight each of the place references by hand, and then manually everything into some kind of database at the end. Instead, we're going to write a simple Python script to do "named entity recognition" (NER), a process that automatically extracts words or phrases in a text that are proper names, locations, etc. This process is far from perfect, but it's much faster than doing things by hand, and it allows us to get a high-level snapshot of the spatial "fingerprint" of a text.

## Set up a Python development environment

First, we'll install the latest release of Python 3.

**MAC**

1. On Mac, the easiest way to do this is with a program called Homebrew, a package manager that automatically installs software on OSX. Go to http://brew.sh, and copy-and-paste the command on the front page into your terminal.

1. Install Python 3 with: `brew install python3`

1. Change into the `Projects` directory that we created when georeferencing Minard's map: `cd ~/Projects`

1. Create a new directory called `geotext`, which is what we'll call our program: `mkdir geotext`

1. Change down into the new directory with `cd geotext`.

1. Now, we'll create a "virtual environment," a set of files that wraps up a copy of Python and a set of dependencies that will be specific to this individual project. Run: `pyvenv env` This will create a directory called `env` under `geotext`.

1. Activate the environment with: `. env/bin/activate`

1. Create a `requirements.txt` file, which will define our dependencies: `touch requirements.txt`

1. Open up `requirements.txt` in Atom and enter these dependencies:

  ```
  ipython
  click
  numpy
  polyglot
  nltk
  python-dotenv
  geojson

  -e git+https://github.com/geopy/geopy.git#egg=geopy
  ```

1. Back in the terminal, run `pip install -r requirements.txt` **NOTE**: If you're on Mac, and this gives an error, run this command:

  `CFLAGS=-I/usr/local/opt/icu4c/include LDFLAGS=-L/usr/local/opt/icu4c/lib pip install pyicu`

  And then run `pip install -r requirements.txt` again.

1. Now, if you type `ipython`, you should get dropped into an interactive Python shell.

**WINDOWS**

TODO

## Create a simple command-line program

Next, we'll scaffold out the files needed to create a command-line utility called `geotext`, which we'll use as a point entry for a set of scripts to extract place names, geocode them, and wrangle the data into different formats.

1. In the `geotext` directory, add a file called `setup.py`: `touch setup.py`

1. Open the file in Atom, and enter in some basic metadata about the project:

  ```
  from setuptools import setup, find_packages

  setup(

      name='geotext',
      version='0.1.0',
      description='Extract toponyms from plain text.',
      license='MIT',
      author='David McClure',
      author_email='dclure@stanford.edu',
      packages=find_packages(),
      scripts=['bin/geotext'],

  )
  ```

  The important part here is the last two lines - `packages` and `scripts` - which tell Python where to find our code.

1. Back on the command line, create a new directory called `bin` - `mkdir bin`

1. Create a new file in that directory called `geotext` - `touch bin/geotext`

1. Set the permissions on the file to make it executable - `chmod 755 bin/geotext`

1. Open the new `geotext` file in Atom, and enter a basic hello world program as a test:

  ```
  print('Hello world!')
  ```

1. Back on the command line, install the program with: `python setup.py develop`

1. Now, if you just run the command `geotext`, you should see - `Hello world!`

## Toponym extraction

Now, we're ready to sketch in the logic for the entity extraction and geocoding. We'll walk through this together, but here's the complete code for reference:

https://github.com/davidmcclure/hilt-2016/blob/master/geotext/bin/geotext
