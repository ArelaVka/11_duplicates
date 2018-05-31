# Anti-Duplicator

Script can help find duplicate files in current directory (recursively). Files with the same name and size are considered to be duplicate.

# How to use

To use script you need specify path of directory to find duplicates.
```bash
python duplicates.py <directory>
```

Example (Windows):
```cmd
C:\>python C:\11_duplicates\duplicates.py C:\testdir

Duplicate files:
+ C:\testdir\123.docx
+ C:\testdir\123123\123.docx
+ C:\testdir\in\123.docx

Duplicate files:
+ C:\testdir\README-copy - копия.md
+ C:\testdir\in\README-copy - копия.md

Duplicate files:
+ C:\testdir\README-copy.md
+ C:\testdir\in\README-copy.md
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
