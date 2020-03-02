# egybest-dl

Downloads any Movie or TV Series from EgyBest.

## Description

**egybest-dl** is a command-line program to download any movies or TV series from [egy.best](www.egy.best) , it comes with a built-in CLI downloader; or you can copy-paste download URIs into your favorite download manager.\
It requires `Python>=2.7`, and it is not platform specific. It should work on both Linux and Windows.

```
egybest-dl [OPTIONS] [SEARCH] [SEASONS]...
```

## Requirements

- `Python >= 2.7`
- `Python >= 3.4` for the CLI downloader.
- [Google Chrome](https://www.google.com/chrome/)

## Install

```
pip install egybest-dl
```

## Usage

`egybest-dl --help` for help

`egybest-dl <movie name>` to search for the movie and download it\
eg: `egybest-dl 'deadpool'`

`egybest-dl <series name> <season:episode,...> ...` to search for the series and download it\
eg: `egybest-dl 'suits' 4 5:1,2,3` to download the fourth season and episodes 1, 2 and 3 of the fifth season

Since it is a command line prompt-based program, you can just do :
```
$ egybest-dl
What are you searching for : the witcher
Initializing Chrome
Searching for results...
Series : The Witcher
Requesting pages links...
What seasons and episodes ?
...
```
etc...

### Options
```
-Q, --quality [1080|720|480|360|240] Quality of output video.  [default: 720]
-o, --output-file FILENAME           Save download URIs to FILENAME.
-d, --dest TEXT                      Destination path.
--executable-path FILE               Path to chromedriver executable.
--quiet                              Activate quiet mode.
--version                            Show the version and exit.
--help                               Show this message and exit.
```

### Note

If you're facing this issue:
```
Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
then, you'll have to install the `chromedriver` and add it to your `PATH` , or specify its path using the `--executable-path` option.\
eg: `egybest-dl --executable-path ~/Downloads/chromedriver ...`


_**PS: I, in no way support piracy. This is for educational purposes only.**_
