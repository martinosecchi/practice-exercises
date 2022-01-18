"""
Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};

Output:  Following words of dictionary are present
         GEEKS, QUIZ

Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
"""

def main():
    dictionary = {"GEEKS": 1, "FOR":1, "QUIZ":1, "GO":1}
    boggle   = [['G','I','Z'],
               ['U','E','K'],
                ['Q','S','E']]

    found = {}
    ROWS = len(boggle)
    COLS = len(boggle[0]) if ROWS > 0 else 0

    def available(i,j):
        """Computes available positions starting from position i,j
            Returns:
                an array of tuples with the coordinates
        """
        av = []
        for x in range(i-1, i+1 +1):
            for y in range(j-1, j+1 +1):
                if (i,j) != (x,y) and (0 <= x and x < ROWS) and (0 <= y and y < COLS):
                    av.append((x,y))
        # print("available from {},{}: {}".format(i,j,av))
        return av

    def copy(visited):
        c = []
        for row in range(len(visited)):
            c.append([])
            for v in visited[row]:
                c[row].append(v)
        return c

    def find(boggle, i, j, found):

        def dfs(visited, i, j, word):
            visited = copy(visited)
            visited[i][j] = True
            newword = word + boggle[i][j]
            print(newword)
            if newword in dictionary:
                # print("--- found: {} ---".format(newword))
                found[newword] = 1
            for x,y in available(i, j):
                if not visited[x][y]:
                    dfs(visited, x, y, newword)

        visited = []
        for line in range(len(boggle)):
            visited.append([])
            for w in boggle[line]:
                visited[line].append(False)

        dfs(visited, i, j, "")
    
    for i in range(len(boggle)):
        for j in range(len(boggle[i])):
            find(boggle, i, j, found)

    print(found)
    return found

if __name__ == '__main__':
    main()




