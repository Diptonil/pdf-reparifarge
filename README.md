# PDF Reparifarge

- Some fairly simple transfiguration for a PDF to alter its properties and metadata. 
- Created because I felt the need to alter the metadata of an inconsequential, yet compulsory document that I could easily copy, edit and send.
- Bring your edited PDFs here, run the program and exchange metadata you don't want for the one that you do. 
- *Reparifarge* is a transfiguration spell using in Harry Potter to undo the effects of a disastrous transformation. In some ways, that's what we are doing here too. XD


## Notes

- The primary objective of reading and swapping out metadata can be easily done with some basic manipulation and use of third-party library functions. That bit is, albeit not quite eloquently, implemented as methods to the PDF class in the `main.py` file.
- This program currently takes in file names through the code (rather than, say, the CLI). Probably will add CLI support sometime in the future if I have the time.
- The utility can be extended even further by directly copying over a metadata set stored in a JSON file to the PDF in question. Or by just having the names of the two files (the original and the 'forged' document) passed as a CLI parameter (and having the metadata of the original copied over to the new one). If you're here and wish to tune the program in such ways, feel free to change it up and make a PR.
