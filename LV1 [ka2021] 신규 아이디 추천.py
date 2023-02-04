def solution(new_id):
    answer = ""
    new_id = new_id.lower()
    for i in new_id:
        if i < "a" or i > "z":
            if i < "0" or i > "9":
                if i != "-" and i != "_" and i != ".":
                    new_id = new_id.replace(i, "")
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    if len(new_id) > 1:
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if new_id == "" or new_id == ".":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id
