#Text-Chunker-From-Folder


## Overview

Text-Chunker is a program to take a folder full of text files and split each file into a user-determined number of equal sized chunks and placed into their own sub-folders. This repo comes with the source code that can be run from the command line as well as an executable version of the program.

##Usage
This program can be run with any Python3 installation.

2 inputs are required to run the program. One is a relative path to the file to be split up. The second is the number of files to break up each individual text file into.

A sample run command is given below

```python3 main.py [1] [2]```

[1]: The relative path to the directory containing the text files to chunk
[2]: Number of chunks to gbreak up a file into

The TextChunker will give output in a folder called "output" in the same relative directory as the script and text files. For each text file parsed, a folder inside of the "output" folder will be generated and the chunked files will be found in there.

For example, given the following folder structure

```
D:.
|   main.py
|   
+---speakers
|   |   Aaron.txt
|   |   Abinadi.txt
|   |   Abinadom.txt
\

```
and run command:

```python3 main.py "speakers\" ```

The expected output would result as follows:

```
D:.
|   main.py
|           
+---speakers
|   |   Aaron.txt
|   |   Abinadi.txt
|   |   Abinadom.txt
|   |   
|   \---output
|       +---Aaron
|       |       Aaron_1.txt
|       |       Aaron_2.txt
|       |       Aaron_3.txt
|       |       
|       +---Abinadi
|       |       Abinadi_1.txt
|       |       Abinadi_2.txt
|       |       Abinadi_3.txt
|       |       
|       +---Abinadom
|       |       Abinadom_1.txt
|       |       Abinadom_2.txt
|       |       Abinadom_3.txt
|       \       
\
```
