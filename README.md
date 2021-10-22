# w2rgb - Convert a wavelength to an RGB Color

A small python script to quickly convert wavelengths to colors. This is basically
just a wrapper around the core function presented at http://www.noah.org/wiki/Wavelength_to_RGB_in_Python.

## Installation
```shell
pip3 install -r requirements.txt
python3 setup.py install --user
```

## Usage
```
$ w2rgb 532
#65ff00
```
### options
```
positional arguments:
  wavelength  wavelength in nm, [380 nm to 750 nm]

optional arguments:
  -h, --help  show this help message and exit
  --fmt FMT   Output format. ['hex', 'rgb', 'RGB']
```
