movies = ["The Holy Grail", 1975, "Terry jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliams", "Eric Idle", "Terry Jones"]]]
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)