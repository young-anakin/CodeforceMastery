def findDuplicate(paths):
    content = {}
    paths = []
    str = "ab"
    for a in range(0, len(paths)):
        init = paths[a].index('(')
        end = paths[a].index(')')
        content[paths[a][init:end+1]] = 

