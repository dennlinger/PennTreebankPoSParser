# PennTreebankPoSParser
Transformation script that aggregates all the PoS annotations in the Penn Treebank available on Kaggle into a single CSV file.
The main problem here is that the files are extremely difficult to parse "on the fly", as they contain multiple different formats (see section "Disclaimers below").

## Installation/Execution
Simply clone the GitHub repository with `git clone https://github.com/dennlinger/PennTreebankPoSParser.git`,
or download the content of the python script.<br/>
It further assumes that you do have some form of the downloaded Penn Treebank on your system, and know its root folder location, in which there is another subfolder `tagged/`, that contains the respective PoS tag information.<br/>
To run the script, you can either specify the file locations (and name/location of the output file) within the script,
or alternatively pass them by calling
``` python3 ptbPosParser.py <penn_root_folder> <output_filename> ```
The result will be an aggregated 

## Options
The parser allows you two major options:

* The delimiter for the resulting file can be set as a function argument to `appendLine`, and defaults to a whitespace.
* If enabled, every quotation mark that either follows " or \`\`, will be removed. This can be set as a major argument when calling `parseSingleFile`, and will be handed down to `appendLine` in a similar fashion, as it can make up both a full line, or appear in compounds.

## Disclaimers
I don't guarantee 100% correctness. There are some flaws within the dataset that make it particularly difficult to parse.
This includes (but might not be limited to):

* The splitting character for word-tag is the slash ("/"), which also sometimes appears as a character in text (although escaped with the backslash ("\/").
* Some lines are separated by multiple "=" characters.
* The stripping of " ", "\[", and "\]" for some form of composite phrases (?)
* Randomly appearing (and not consistently denoted) quotation marks (" vs \`\`), that sometimes appear in between sentences,and sometimes within the sentence itself.

## Output Format
The output format is per default a space-delimited pair of the form
``` <word> <PoS_token>```
Sentences are generally split after a dot; special treatment is given if there are quotation marks after a dot, but this can lead to theoretical inconsistencies.
