
def read_text_files(text_file):
    '''读取文本文件'''
    lines = []
    with open(text_file, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def replaceNamedEntity(namedEntitySets, sentenceWords):
    '''替换被分割的命名实体
    :param namedEntitySets, 命名实体构成的列表
    :param sentenceWords, 一句话构成的列表, 每个元素为一个词
    '''
    replaceNeSenWords = []
    sw_len = len(sentenceWords)

    i = 0
    while i < sw_len:
        word = sentenceWords[i]
        step = 1
        j = i + 1
        while j < sw_len:
            saveWord = word
            word += sentenceWords[j]
            if inNamedEntitySets(namedEntitySets, word):
                step += 1
                # 最后一个分词直接加入
                if j == (sw_len - 1):
                    replaceNeSenWords.append(word)
            else:
                replaceNeSenWords.append(saveWord)
                break
            j += 1


        if i == (sw_len - 1):
            replaceNeSenWords.append(sentenceWords[i])

        i += step
    return replaceNeSenWords



def inNamedEntitySets(namedEntitySets, word):
    for namedEntity in namedEntitySets:
        if word == namedEntity:
            return True



if __name__ == '__main__':
    namedEntitySets = read_text_files('frequency_deal_3.txt')
    line = "平安 集团 的 理财 产品 怎么样".split(' ')
    print(line)
    print(replaceNamedEntity(namedEntitySets, line))
