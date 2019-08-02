def getPlace(question):
    keywords = ['du', 'de', 'des', 'le', 'la', 'les']
    testsplit = question.split(' ')
    # print(testsplit)
    for item in testsplit:
        # print(item)
        if item in keywords or item.startswith("l'") or item.startswith("d'"):
            index = testsplit.index(item)
            if item in keywords:
                lieu = ' '.join(testsplit[index+1:])
            else:
                lieu = ' '.join(testsplit[index:])
            # print(lieu)
            return lieu
            break