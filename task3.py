def reverse_words(s):
    pass


assert reverse_words("Wikis are enabled by wiki software, otherwise known as wiki engines.") == "engines. wiki as known otherwise software, wiki by enabled are Wikis"
assert reverse_words("Hello   world") == "world Hello"
assert reverse_words("Python is the best language!") == "language! best the is Python"
assert reverse_words("") == ""