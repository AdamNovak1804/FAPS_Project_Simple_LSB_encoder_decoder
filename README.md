# Simple LSB program for steganography
This program primarily consists of two python files:

**encode.py**: used for hiding the data within a cover file; creates an output file

**decode.py**: used to recover hidden data from the output file

To test this program, clone the repository to your local machine and open up a command line inside the directory.
Use encode function with following syntax:

```console
python encode.py <file.txt> <img.png>
```

After successful completion no error message should be displayed and *output.png* file should be present in the directory.

To use the decoding function, write following line in to the command prompt:

```console
python decode.py <output.png>
```

If successful, output string should be printed out into the command prompt.
