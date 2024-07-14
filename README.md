### The Art of Math

#### Mathematics can be a complicated subject, but from that complexity can come beauty. This project is all about exploring different theorems and simple functions and the different ways to represent their beauty.

#### The parameters for the outputs are provided using json configuration files for each of the theorems or visuals. Example config files are provided within the directories. In order to produce the images yourself, first you must clone the repository, install all necessary libraries, and then run the desired config in the command line.

#### The following example will produce the twin primes graph below, assuming you are in the outer art_of_math directory:

    python art_of_math.py primes/twin_config.json


![Twin prime example](/output/primes/twin/20x20/black_twilight.png)

#### For a more detailed description of the theorems themselves and the specific run parameters required, see the README files in each directory:

- [Adding Waves](/adding_waves/README.md)
- [Amazing Graphs](/amazing_graphs/README.md)
- [Contours](/contours/README.md)
- [Double Pendulum](/double_pendulum/README.md)
- [Equation Graphs](/equation_graphs/README.md)
- [Primes](/primes/README.md)
