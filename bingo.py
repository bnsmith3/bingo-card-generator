# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:39:13 2019
@author: bnsmith3
"""

from random import sample
import argparse

def get_combinations(num_combs, num_entries, entries=[]):
    """Return a list of unique combinations of entries.

    Parameters
    ----------
    num_combs: Number of combinations of entries to return
    num_entries: Number of items that should be in each combination
    entries: List of items to use to make the combinations
    """
    choices = []
    while len(choices) < num_combs:
        new_choice = sample(entries, num_entries)
        if new_choice not in choices:
            choices.append(new_choice)

    return choices

def get_cards(num_cards, num_rows=5, title='Bingo Card', entries=[], entries_file=None, card_file=None, in_order=False):
    """Generate an html file that displays num_cards number of bingo cards.

    If entries_file is provided, the contents of that file are used in lieu of
    the entries list.

    If card_file is provided, the html file is saved to that file in addition
    to being returned.

    Parameters
    ----------
    num_cards: The number of cards to create
    num_rows: The number of rows and columns each card should have
    title: The title to display at the top of the cards
    entries: List of items to use to make the cards
    entries_file: Name of the file that holds one item per line
    card_file: Name of the file to which to save the html file
    in_order: boolean that is True if the entries should be added to the cards in order;
        it is False if the entries should be added in a random order
    """
    if entries_file:
        with open(entries_file, 'r') as f:
            entries = f.readlines()

    free_space = False if (num_rows % 2) == 0 else True
    midpoint = -1
    if free_space:
        if in_order:
            combinations = [entries[:(num_rows**2)-1]] * num_cards
        else:
            combinations = get_combinations(num_cards, (num_rows**2)-1, entries)
        midpoint = ((num_rows**2)-1)/2
    else:
        if in_order:
            combinations = [entries[:(num_rows**2)]] * num_cards
        else:
            combinations = get_combinations(num_cards, num_rows**2, entries)

    html = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
            "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
    	<title>Bingo Card</title>
    	<style>
    		html {
    			font-family: Helvetica, Arial, sans-serif;
    		}

    		table {
    			page-break-after: always;
    			border-collapse: collapse;
                table-layout: fixed;
                width: 500px;
                border: 2px solid darkgrey;
    		}

    		td {
    			border: 2px solid darkgrey;
    			text-align: center;
    			padding: 5px 5px;
                height: 100px;
    		}

    		th {
    			text-align: center;
    			padding: 5px 0;
                background-color: #BF3B3B;
                color: white;
    		}
    	</style>
    </head>
    <body>
    """

    for card in combinations:
        html += """
        <table>
        <thead>
        <tr><th colspan="{}">{}</th></tr>
        </thead>
        <tbody>
        """.format(num_rows, title)
        item_count = 0
        for entry in card:
            if (item_count % num_rows) == 0:
                html += "<tr>"

            if midpoint == item_count:
                html += "<td>FREE<br>SPACE</td>".format(entry)
                item_count += 1

            html += "<td>{}</td>".format(entry)

            if (item_count % num_rows) == (num_rows-1):
                html += "</tr>"

            item_count += 1

        html += "</tbody></table>"

    html += "</body></html>"

    if card_file:
        with open(card_file, 'w') as w:
            w.write(html)

    return html

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Auto-generate bingo cards'))
    parser.add_argument('--num_cards', '-c', action='store', type=int,
                        default=5,
                        help='The number of cards to create; 5 is the default.')
    parser.add_argument('--num_rows', '-r', action='store', type=int,
                        default=5,
                        help='The number of rows each card should have; 5 is the'
                            ' default.')
    parser.add_argument('--title', '-t', action='store', default='Bingo Card',
                        help='The title to display at the top of the cards. '
                            ' \"Bingo Card\" is the default.')
    parser.add_argument('--entries_file', '-e', action='store', required=True,
                        help='The file that holds the items to use to populate'
                            ' the generated cards.')
    parser.add_argument('--card_file', '-f', action='store', required=True,
                        help='The file to which we will write the generated cards.')
    parser.add_argument('--in_order', '-i', action='store_true',
                        help='Add this flag if the entries should be added to '
                            'cards in order.')

    args = parser.parse_args()
    a = get_cards(args.num_cards, args.num_rows, args.title, \
                  entries_file=args.entries_file, card_file=args.card_file, \
                  in_order=args.in_order)
