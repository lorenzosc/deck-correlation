# deck-correlation
Algorithm for Legends of Runeterra deck correlation using a google spreadsheet matchup table information

This requires a developer account from google with the service account data in a file. All you have to do is get yours downloaded directly from google cloud and put it in the project directory, and the same name in main.py line 6. This routine can be used for any sheet you have access to with your developer account, even if you're unable to edit it. Having permission to view is enough, since the program only gets the matchup table data. You can also use another table by changing the key to the correspondent one.

When creating the list of all objects, the current string cleaning (by replacing linebreaks with spaces) serves the sole purpose of ensuring that the hero and villain decks are written exactly the same. This is strictly related to how the sheets was written, and I advise attention to adjust for wherever the data is being gathered from.

The choice of the deck (line 24) requires the exact same characters that are in the table, so be aware of that. And lastly, the results are printed in the end of the program, feel free to change to how it suits you best. The compatibility yields the correlation coefficient formula between those 2 decks matchup tables, considering them as 2 random variables and verifying what type of correlation exists. The closer to 1, the more correlated they are. The closer to -1, the more inversely correlated they are. At 0, it means they present almost no correlation whatsoever.
