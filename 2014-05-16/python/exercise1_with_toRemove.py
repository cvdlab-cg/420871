# Exercise 1

""" progressive refinement of a block diagram """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/home/biagio/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])


def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

master = assemblyDiagramInit([15,13,2])([[0.3,2,0.3,1,0.3,2,0.3,1,0.3,1,0.3,2,0.3,0.5,0.3], [0.3,2,0.3,1.5,0.3,0.5,0.3,1,0.3,1.7,0.3,1.3,0.3], [0.1,3]])
V,CV = master

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),YELLOW,1)
#VIEW(hpc)


# walls removing
toRemove =[0,1,2,3,4,5,6,7,8,9,10,11,12,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,43,45,48,49,50,51,67,69,71,74,75,76,77,81,83,85,87,89,93, 95,97,100,101,102,103,107,109,111,113,115,126,127,128,129,133,135,137,139,141,144,145,146,147,148,149,150,151,152,153,154,155,
174,175,176,177,178,179,180,181,185,200,201,202,203,204,205,206,207,338,339,340,341,342,343,344,345,346,347,348,349,350,351,
352,353,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,
263,237,211,289,293,267,241,297,299,301,
189,191,193,195,197,
305,307,309,
331,333,335,
357,359,361,
279,281,283,
245,247,249,251,253,255,257,
]


master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

# main door creation
toMerge = 35
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([3,1,2])([[0.1,0.8,0.1],[.3],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

toRemove = [226]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /main door creation

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

# kitchen door
toMerge = 41
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([3,1,2])([[0.1,0.8,0.1],[.3],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [230]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /kitchen door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)


# room 1 door
toMerge = 94
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([3,1,2])([[0.1,0.8,0.1],[.3],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

toRemove = [234]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /room 1 door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)


# day-night door
toMerge = 79
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([1,3,2])([[0.3],[0.3,0.9,0.3],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [238]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /day-night door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

# bathroom door
toMerge = 106
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([1,3,2])([[0.3],[0.3,0.9,0.3],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1.5)
#VIEW(hpc)

toRemove = [242]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /bathroom door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# room-bath door
toMerge = 154
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([1,3,2])([[0.3],[0.1,0.8,0.1],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [246]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /room-bath door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# room2 door
toMerge = 113
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

door = assemblyDiagramInit([1,3,2])([[0.3],[0.1,0.8,0.1],[2.2,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [250]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /room2 door

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# kitchen window
toMerge = 14
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([3,1,3])([[0.2,1.6,0.2],[.3],[1,1.4,.3]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [256]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /kitchen window

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# garden window
toMerge = 70
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([3,1,2])([[0.2,1.6,0.2],[.3],[2.2,.5]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [261]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /garden window

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# bath-room window
toMerge = 175
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([3,1,3])([[0.2,0.9,0.2],[.3],[1,1.4,.3]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [267]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /bath-room window

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# room window
toMerge = 178
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([1,3,3])([[0.3],[0.1,1.1,0.1],[1,1.4,.3]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [274]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /room window

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# bath window
toMerge = 181
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([1,3,3])([[0.3],[0.2,0.9,0.2],[1.8,0.6,.3]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [281]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /bath window

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

# bath-room window
toMerge = 188
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

window = assemblyDiagramInit([1,3,3])([[0.3],[0.1,0.8,0.1],[1.8,0.6,.3]])
master = diagram2cell(window,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [288]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
# /bath-room window








### ESPORTAZIONE

solidCV = [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW((master[0],solidCV))

exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in toRemove]
exteriorCV += exteriorCells(master)
CV = solidCV + exteriorCV
V = master[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))

BF = boundaryCells(solidCV,FV)
boundaryFaces = [FV[face] for face in BF]
B_Rep = V,boundaryFaces
#VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS(B_Rep)))
#VIEW(STRUCT(MKPOLS(B_Rep)))


verts, triangles = quads2tria(B_Rep)
B_Rep = V,boundaryFaces
#VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS((verts, triangles))))
#VIEW(STRUCT(MKPOLS((verts, triangles))))

# ESPORTO
objExporter((verts, triangles), 'exercise1.obj')
