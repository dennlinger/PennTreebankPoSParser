# PennTreebankPoSParser
Transformation script that aggregates all the PoS annotations in the Penn Treebank available on Kaggle.

## Installation
Simply clone the GitHub repository with `git clone https://github.com/dennlinger/PennTreebankPoSParser.git`,
or download the content of the python script.<br/>
To run the script, you can either specify the file locations (and name/location of the output file) within the script,
or alternatively pass them by calling
``` python3 ptbPosParser.py <penn_root_folder> <output_filename> ```

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
