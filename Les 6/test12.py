mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "Registratienummer" : "AA18891" }
mijn_dictionary["Achternaam"] = "Potter"
mijn_dictionary.pop("Geboortedatum")
del mijn_dictionary["Geboortejaar"]
print()
for k, v in mijn_dictionary.items():
    print (k,v)