# Lokaverkefni í Inngang að máltækni

Eftir Ármann Schelander

This is a final project I did for a course on language technology, I realize it's methodology is not quite perfect looking back.

## GloVe Analyzer

The GloVe Analyzer is a simple terminal program that reads in two GloVe models from txt files. It can then be used to compare vectors found in each model by comparing it's respective n closest vectors then comparing the two sets.

To use it you will need two GloVe model txt files, you can load them by entering `load <modela> <modelb>` or if you wish to load them separately, `loada <modela>`, `loadb <modelb>`.

For a list of commands enter `help`, for elaboration on any given commands enter `help <command>`