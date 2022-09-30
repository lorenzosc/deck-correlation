from deck import Deck, compatibility
import gspread

#%% importing data from sheets
sa = gspread.service_account(filename = "service_account.json")

key = "1Xlh2kg7gLzvqugqGPpI4PidAdM5snggbJ44aRLuik5E" #key from the document
sheet_name = "Winrate" #name of desired sheet

sh = sa.open_by_key(key)
wks = sh.worksheet(sheet_name)
all_decks = wks.get_all_records()

#%% creating a list of all the deck objects
all_decks_list = []
for row in all_decks:
    clean_row = { k.replace('\n', ' '): v for k, v in row.items() }
    clean_row[clean_row[' ']] = 50
    aux = Deck(clean_row.pop(' ', None), clean_row)
    all_decks_list.append(aux)

#%% choosing deck and main routine
"""
    print all the deck names and associate with their list index and ask for the
    user to input the index of the deck they want to compare with the rest of the
    pool
"""
for i, option in enumerate(all_decks_list):
    print(f"{i}: {option.name}")

main_deck = int(input())

#running compatibility of chosen deck with the rest of the pool
compatibilities = []
for option in all_decks_list:
    aux = compatibility(option, all_decks_list[main_deck])
    compatibilities.append((option.name, aux))

#sorting and printing compatibilities
compatibilities = sorted(compatibilities, key=lambda tup: tup[1], reverse = True)
for i in compatibilities:
    print(i)