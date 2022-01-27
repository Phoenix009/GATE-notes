with open('compiled.txt', 'a') as output:
    with open('topics.txt') as names:
        for name in names:
            name = name.strip()
            with open(name) as target:
                for line in target:
                    output.write(line)

