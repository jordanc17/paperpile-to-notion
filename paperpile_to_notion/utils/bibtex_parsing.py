from bibtexparser.customization import convert_to_unicode, author, splitname


def rebuild_name(name):
    if name.endswith(", "):
        return name[: -len(", ")]
    name = splitname(name)
    name = name["first"] + name["last"] + name["von"] + name["jr"]
    name = " ".join(name)
    return name

def rebuild_keywords(keywords):
    kw_list= keywords.split(";")
    kw_list = [kw.strip() for kw in kw_list]
    kw_list = ", ".join(kw_list)
    return kw_list


def parser_customizations(record):
    record = convert_to_unicode(record)
    record = author(record)
    if "author" in record:
        author_list = [rebuild_name(name) for name in record["author"]]
        record["author"] = ", ".join(author_list)
    if "keywords" in record:
        record["keywords"] = rebuild_keywords(record["keywords"])
    return record
