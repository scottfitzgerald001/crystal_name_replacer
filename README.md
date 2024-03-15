
### Crystal name replacer

Takes a list of names and replaces the trainer names in the ROM generated by the pret team's pokecrystal disassembly.

### Requirements
Python3 - download the newest version from python's website, any version of py3 _should_ work (anything 3.7+ is prefered)

rgbds - for building the crystal rom
https://rgbds.gbdev.io/install/

### How to use

You will see two json files:

*  `trainer_names.json`
	* Contains a Chat-GPT generated list of all non-essential trainer classes (no gym leaders or rival)
	* You can remove a class from this file and the mapper will not override the trainer class's name (you could reduce this down to a specific list of trainer's who's name can be replaced)
* `input_names.json`
	* Json list of all names to add into the ROM

This is a quick python script that goes into the rom and maps new name onto the trainer classes. 

To set up you will need to clone the pret repo into the same directory as the main file:

`git clone https://github.com/pret/pokecrystal.git`

Then you simply update the input files accordingly and run the program with:

`python3 ./main.py`

After that runs, you need to build the crystal rom:

`cd pokecrystal`

`make` 

^ Note that you may need to do some additional setup for downloading tools that  enables compiling Crystal's rom

### How do I reset the trainer file?

If you want to rerun this mapper, checkout the trainer.asm file again before running a new mapping:

`cd pokecrystal`

`git checkout data/trainers/parties.asm`
