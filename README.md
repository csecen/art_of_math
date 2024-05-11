### The Art of Math

##### Mathematics can be a complicated subject, but from that complexity can come beauty. This project is all about exploring different theorems and simple functions and the different ways to represent this beauty.

##### The parameters for the outputs are provided using json configuration files for each of the theorems or visuals. Example config files are provided with the directories. In order to produce the images yourself, first you must clone the repository, install all necessary libraries, and then run the desired config in the command line.

##### The following example will produce the twin primes graph below, assuming you are in the outer art_of_math directory:

    python art_of_math.py primes/twin_config.json


![Twin prime example](/output/primes/twin/20x20/black_twilight.png)

##### For a more detailed description of the theorems themselves and the specific run parameter required, see the ReadMe files in each directory.

- [Primes](/primes/README.md)