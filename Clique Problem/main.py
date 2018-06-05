import random
secure_random = random.SystemRandom()


def clique(U, size):                    #Recursive algorithm that increases the size of the subgraph clique per iteration
    global max
    if len(U)==0:
        if size>max:
            max = size
            cliques.append(max)
            print("Maximum size clique: %s" % max)
        return
    while len(U)>0:
        if (size + len(U)) <= max:
            return
        Vi = random.choice(U)
        clique(intersect(U, neighbours(Vi)), size+1)        #Select random vertex and find neighbours of that vertex then call
        U.remove(Vi)                                        #Clique for refined set of neighbours
    return

def findHigher(index):                                      #function to find Si = list of vertices with higher index than index
    list = []
    for i in range(len(vertices)):
        if i > index:
            list.append(vertices[i])
    return list

def neighbours(i):                      #find the neighbours / adjacent vertices of vertice i
    n = []
    for edge in edges:
        if edge[0] == i:
            n.append(edge[1])
        if edge[1] == i:
            n.append(edge[0])
    return n

def intersect(U, Nv):               #return list of intersecting lists U, Nv
    inter = list(set(U) & set(Nv))
    return inter

edges = []
vertices = []
cliques = []

while(True):
    filename = input("\n Please input filename: ")
    fname = 'files/' + filename
    try:
        with open(fname) as f:
            content = f.readlines()
            print(f.readline())
        content = [x.strip() for x in content]
    except FileNotFoundError:
        print("Wrong file name, try again")
    else:
        break

for item in content:
    line = item.split(" ", 2)
    if(line[0]=='e'):
        entry=[line[1], line[2]]
        edges.append(entry)

for edge in edges:                  #find
    if(edge[0] not in vertices):
        vertices.append(edge[0])
    if(edge[1] not in vertices):
        vertices.append(edge[1])

found = False
max = 0
vertices = sorted(vertices, key=int)        #Sort the vertices list numerically asc
clique(vertices, 0)