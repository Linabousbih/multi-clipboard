# Clipboard Manager

This Python command-line app allows you to easily copy and retrieve multiple pieces of data from your clipboard using custom titles. 

## Installation

Before using the app, make sure you have Python installed on your system.

1. Clone or download this repository.

2. Open your terminal and navigate to the project directory.

## Usage

The Clipboard Manager supports the following commands:

### Save

Use the `save` command to store the current contents of your clipboard with a custom title.

```bash
python main.py save [title]
```

### Copy

Use the `copy` command to retrieve data from the clipboard using its assigned title.

```bash
python main.py copy [title]
```

### List

Use the `list` command to display a list of all stored data titles and their corresponding values.

```bash
python main.py list
```
