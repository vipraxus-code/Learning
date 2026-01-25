def abbrev_name(name):
    return f"{name[0]}.{name[name.index(" ")]}"

print(abbrev_name("Sam Harris"))