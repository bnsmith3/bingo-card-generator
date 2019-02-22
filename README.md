# bingo-card-generator

A simple command line tool to generate bingo cards

---

## Quick Start
Using bingo-card-generator is fairly straightforward. To see the command line arguments, issue the following command from the directory that contains `bingo.py`:
`python bingo.py --help`

When running `bingo.py`, the script takes 5 arguments, 2 of which are required:
* `-e` or `--entries_file` (required): The name of the file that holds the items to use to populate the generated cards
* `-f` or `--card_file` (required): The name of the html file to which the generated cards will be written
* `-c` or `--num_cards`: The number of cards to create; 5 is the default
* `-r` or `--num_rows`: The number of rows each card should have; 5 is the default
* `-t` or `--title`: The title to display at the top of the cards; "Bingo Card" is the default