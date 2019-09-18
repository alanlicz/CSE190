def get_and_analyze_poem():
    verse1 = '''She likes to rhyme
And pass the time
To use the prime
or """quotes""" sublime, That's not a crime'''
    lines = verse1.split("\n")
    print(lines)
    return verse1 + "\n\n contains five " + \
        "rhyming words:" + ''.join(line.split(' ')[-1] + ', ' for line in lines)[:-2]


print(get_and_analyze_poem())