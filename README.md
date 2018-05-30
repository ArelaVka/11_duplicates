# Anti-Duplicator

Script can help find duplicate files in current directory (recursively). Files with the same name and size are considered to be duplicate.

# How to use

To use script you need specify path of directory to find duplicates.
```bash
python duplicates.py <directory>
```

Example (Windows):
```cmd
C:\>python C:\11_duplicates\duplicates.py C:\11_duplicates\testdir

File "C:\11_duplicates\testdir\README-copy - копия.md" is copy of "C:\11_duplicates\testdir\in\README-copy - копия.md"

File "C:\11_duplicates\testdir\README-copy.md" is copy of "C:\11_duplicates\testdir\in\README-copy.md"
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
