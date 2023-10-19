"use strict";

function generate_password(length=4, delimiter="-", easy_mode=false):
    if easy_mode == True:
        return generate_easy_password()
    wordfile = xp.locate_wordfile("ger-anlx")
    mywords = xp.generate_wordlist(
            wordfile=wordfile,
            min_length=3,
            max_length=16,
            valid_chars="[a-z]"
            )
    password = xp.generate_xkcdpassword(
            mywords,
            numwords=length,
            delimiter=delimiter,
            case="capitalize"
            )
    return password
