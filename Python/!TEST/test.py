favorite_laguages = {"jen": "c","sarah": "rust","edward": "python","phil": "c"}
for language in sorted(set(favorite_laguages.values())):
    print(language.title())