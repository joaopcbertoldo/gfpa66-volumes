# Glass fiber-reinforced polyamide 66 3D X-ray computed tomography dataset for deep learning segmentation

# todos
 
 - updated zip files links
 - updated h5/xdmf files links
 - updated pymicro tutorial link
 - make the `read_h5` work
 - update description in zenodo
 - include link to this 
 - todo show how to do it with fiji --> add it to zenodo as well

If you use this volume, please cite us: 

```
bibtex entry TO BE UPDATED
```

We show how to open data in two ways:

 - from a pair of `.h5`-`.xdmf` files using [`pymicro`](https://github.com/heprom/pymicro)'s class `SampleData`
 
 - `.raw` files


## `.raw` files

**There is no special dependency to use it this way (apart from basic stuff: numpy and matplotlib if you want to plot). **

**You only need the `.zip`s and the module `read_raw.py` in this directory.**

Download and extract the contents of the `crack.zip`, `pa66.zip`, and `pa66_test.zip` files to this directory.

TODO add links

 - [crack.zip]()
 - [pa66.zip]()
 - [pa66_test.zip]()

The `.info` files contain the shape (`x`, `y`, and `z` sizes) of the corresponding files with the same name so that you don't need to type them.

The module `read_raw.py` has a function that will be used to load the files' contents into `numpy.ndarray`s - credits to [`pymicro`](https://github.com/heprom/pymicro).

See the notebook `read_raw.ipynb` for a brief demo of how to open the `.raw`s as numpy arrays - put the contents of the `.zip` files in a folder `raws` before. 

## `SampleData` (`.h5` + `.xdmf`)

Download the files below and put them in this directory.

- [pa66_volumes.h5]()
- [pa66_volumes.xdmf]()

Install [`pymicro`](https://github.com/heprom/pymicro) and follow the tutorial in `read_h5.ipynb`.

To see how the `.h5`/`.xdmf` files were generated, see the file `write_h5.ipynb` or check [this tutorial in `pymicro`'s repository']().



<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Glass fiber-reinforced polyamide 66 3D X-ray computed tomography dataset for deep learning segmentation</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName"><a rel="author" href="https://orcid.org/0000-0002-9512-772X">Joao P C Bertoldo</a>, <a rel="author" href="https://orcid.org/0000-0002-1349-8042">Etienne Decencière</a>, <a rel="author" href="https://orcid.org/0000-0003-3268-4892">David Ryckelynck</a>, and <a rel="author" href="https://orcid.org/0000-0002-4075-5577">Henry Proudhon</a></span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
