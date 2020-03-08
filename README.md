# egybest-dl

Downloads any Movie or TV Series from EgyBest.

## Description

**egybest-dl** is a command-line program to download any movies or TV series from [egy.best](http://www.egy.best) , it comes with a built-in CLI downloader; or you can copy-paste download URIs into your favorite download manager.\
It requires `Python>=2.7`, and it is not platform specific. It should work on both Linux and Windows.

```
egybest-dl [OPTIONS] [SEARCH] [SEASONS]...
```

## Requirements

- `Python >= 2.7`
- `Python >= 3.4` for the CLI downloader.
- [Google Chrome](https://www.google.com/chrome/)

## Install

### Install with pip
```
pip install egybest-dl
```

### Manual install
If you're having problems installing/running it, or would like to make changes, follow these instructions:

1. Clone the repository:
```
git clone https://github.com/yassineaddi/egybest-dl.git
```
2. Enter the directory;
```
cd egybest-dl
```
3. Finally, install:
```
pip install .
```

## Usage

`egybest-dl --help` for help

`egybest-dl <movie name>` to search for the movie and download it

`egybest-dl <series name> <season:episode,...> ...` to search for the series and download it

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

## Examples

Download a movie with a 1080p video quality:
```
egybest-dl '<movie name>' -Q 1080
```
Download the fourth season and episodes 1, 2 and 3 of the fifth season:
```
egybest-dl '<series name>' 4 5:1,2,3
```
Download all episodes of season 1 and episodes, of season 2, after the third one (you can use the less than operator too, eg: `2:<10`)
```
egybest-dl '<series name>' 1 '2:>3'
```
Set destination path for the downloaded file(s):
```
egybest-dl '<movie or series name>' -d ~/Videos
```
Save download URLs to a file:
```
egybest-dl '<movie or series name>' -o dummy.txt
```
This is useful if you'd like to use another download manager\
eg: `aria2c -i dummy.txt`\
or copy them into [Internet Download Manager](https://www.internetdownloadmanager.com/), etc.

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
then, you'll have to install the `chromedriver` and add it to your `PATH` , or specify its path using the `--executable-path` or `-x` option.\
eg: `egybest-dl --executable-path ~/Downloads/chromedriver ...`


_**PS: I, in no way support piracy. This is for educational purposes only.**_
