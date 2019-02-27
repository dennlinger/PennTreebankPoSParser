#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:54:26 2019
The P^3 (PennTreeBank PoS Parser)

This script parses the POS-tagged WSJ corpus from
https://www.kaggle.com/nltkdata/penn-tree-bank/version/5#treebank.zip
to be contained in a single file.

@author: Dennis Aumiller
"""

import sys
import os
import csv
import io


def parseSingleFile(filename, removeQuotationMarks=False):
    print(filename)
    resultingObjects = []
    
    with open(filename) as openFile:
        lines = openFile.readlines()
        
    for i, line in enumerate(lines):
        # skip empty lines, separators "======", and any trailing/leading quotation marks
        strippedLine = line.rstrip("\n").strip(" []")
        if removeQuotationMarks and (strippedLine == "``/``" or strippedLine == "''/''"):
            continue
        if not strippedLine or set(strippedLine) == set("="):
            continue
        else:
            # two spaces in between appear, and crash csv reader. Check those cases, and replace
            if "  " in strippedLine:
                strippedLine = strippedLine.replace("  ", " ")
            appendLine(resultingObjects, strippedLine, removeQuotationMarks=removeQuotationMarks)
                
    return resultingObjects
            
 
def appendLine(resultingObjects, strippedLine, delimiter=" ", removeQuotationMarks=False):
    tokens = strippedLine.split(" ")
    for token in tokens:
        if removeQuotationMarks and (token == "``/``" or strippedLine == "''/''"):
            continue
        # more complicated way to replace "/" with " ", as "/" also sometimes appears in text.
        # http://www.sieswerda.net/2010/10/08/splitting-strings-while-not-ignoring-escape-characters/s
        newFormat = delimiter.join(next(csv.reader(io.StringIO(token), delimiter="/", escapechar="\\")))
        resultingObjects.append(newFormat)
    return resultingObjects           
        

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        ptbRoot = sys.argv[1]
    else:
        ptbRoot = "./treebank/"
        
    if len(sys.argv) > 2:
        outputFilename = sys.argv[2]
    else:
        outputFilename = "./PTB_PoS_pairs.csv"
        
    ptbPos = os.path.join(ptbRoot, "tagged")
    print(ptbPos)
    
    allSentences = []
    
    # skip the README, which is sometimes also in the same folder, also iterate over sorted files.
    # https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
    for filename in sorted(os.listdir(ptbPos)):
        if filename.endswith(".pos"):
            allSentences.extend(parseSingleFile(os.path.join(ptbPos, filename), removeQuotationMarks=True))
    
    # write output
    with open(outputFilename, "w") as openFile:
        for i, instance in enumerate(allSentences):
            openFile.write(instance+"\n")
            # separate sentences
            if instance == ". .":
                openFile.write("\n")
    
    
