# <center>Screentools</center>

## Foreword

This is a beta version and is still under construction. The program is still fully functional on Windows and soon also compatible with Linux. Therefore, I ask for some patience and understanding.

## content

The Windows folder contains 2 working versions for Windows.
And in the Linux folder the same versions slightly modified, but not yet fully compatible for Linux.

### pygame


Is the one version that can pause and cancel the read aloud process.
But unfortunately it can not adjust the read aloud speed and fast forward/backward.

I do not recommend this version at this time because it is incomplete.

### pytttxs3

Is the one version that allows you to set the speed of the read aloud function.
But unfortunately the read aloud process can neither be fast-forwarded/fast-forwarded, paused nor canceled.

I recommend this version because it is complete.
Except for the read aloud function, which lacks the ability to pause, cancel, spool, change speed while reading aloud and change the voice.

Currently, when setting the shortcuts and the reading speed, it is still necessary to rewrite it manually in the code.
This will also be added to the GUI in the future.


## shortcuts 

|#### shortcuts |#### action|
|ALT + Q|Open Menü|
|ALT + Y|Open outputFolder|
|ALT + X|Cut Screenshot|
|ALT + C|Copy Text From Screen|
|ALT + V|reads the test aloud From Screen|
|ALT + 1-9|makes a Screenshotof 1-9 screen|


## Installation

To use the screentool you need Tesseract
-[Orgin](https://github.com/tesseract-ocr/tesseract "Officers Tesseract website")
-[orginal from Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html "Guide to the installation of Tesseract")

### Windows Installation

Downloade from the [Tesseract Version for Windows](https://github.com/UB-Mannheim/tesseract/wiki "Tesseract at UB Mannheim") and run the installer

### Linux Installation

#### Ubuntu

Installs Tesseract
```bash
apt install tesseract-ocr
```

Installs Tesseracts language packs
```bash
apt install tesseract-ocr-eng
apt install tesseract-ocr-deu
apt install tesseract-ocr-jpn
```

Give a list of Tesseracts packs
```bash
sudo apt-cache search tesseract-ocr
```

#### Arch linux

Installs Tesseract
```bash
sudo pacman -S tesseract
```

Installs Tesseracts language packs
```bash
sudo pacman -S tesseract-data-eng
sudo pacman -S tesseract-data-deu
sudo pacman -S tesseract-data-jpn
```

Give a list of Tesseracts packs
```bash
pacman -Ss tesseract
```