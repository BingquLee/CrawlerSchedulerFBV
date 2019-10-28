<<<<<<< HEAD
def get_tag(text):
    text = text + ' '
    tag_list = []
    flag = False
    start = 0
    end = 0
    for i in range(len(text)):
        if text[i] == '#':
            start = i
            flag = True
        elif text[i] == ' ' and flag:
            end = i
            flag = False
        if end > start:
            item = {"start": start, "end": end, "type": 1, "hashtag_name": text[start + 1: end]}
            if item not in tag_list:
                tag_list.append(item)
    return tag_list
=======
def get_tag(text):
    text = text + ' '
    tag_list = []
    flag = False
    start = 0
    end = 0
    for i in range(len(text)):
        if text[i] == '#':
            start = i
            flag = True
        elif text[i] == ' ' and flag:
            end = i
            flag = False
        if end > start:
            item = {"start": start, "end": end, "type": 1, "hashtag_name": text[start + 1: end]}
            if item not in tag_list:
                tag_list.append(item)
    return tag_list
>>>>>>> c7c3fae9169c3514cca359cf767c0ddb4fe4061d
