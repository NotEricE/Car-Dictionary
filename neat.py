def print_neat(dic):
    for key, value in dic.items():
        print(key, ':')
        for Models, Price in value.items():
            print(Models, ':', Price)