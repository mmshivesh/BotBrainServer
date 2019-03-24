from src.store import store
class bot:
    billing=[]
    def __init__(self,pos,dir,billing):
        self.pos = pos
        self.dir = dir
        self.billing = billing
    def __encodeJson(self,paths,store):
        cmdArray=""
        tem_dir = self.dir
        for path in paths:
            print(path)
            tem_pos = path[0]
            #tem_pos = (tem_pos[1],tem_pos[0])
            #print(tem_pos)
            for i in range(1,len(path)):
                next = path[i]
                #next = (next[1],next[0])
                #print(next[0],next[1])
                if(tem_pos[1]==next[1]):
                    #print("x same")
                    if(tem_dir=='N'):
                        if(tem_pos[0]>next[0]):
                            cmdArray = cmdArray+'L'
                            tem_dir = 'W'
                        elif tem_pos[0]<next[0]:
                            cmdArray = cmdArray+'R'
                            tem_dir = 'E'
                    if(tem_dir=='S'):
                        if(tem_pos[0]>next[0]):
                            cmdArray = cmdArray+'R'
                            tem_dir = 'W'
                        elif tem_pos[0]<next[0]:
                            cmdArray = cmdArray+'L'
                            tem_dir = 'E'
                    if(tem_dir=='E'):
                        if(tem_pos[0]<next[0]):
                            if((store.matrix[tem_pos[1]+1][tem_pos[0]]==1) or ((store.matrix[tem_pos[1]-1][tem_pos[0]]==1))):
                                cmdArray = cmdArray+'S'
                    if(tem_dir=='W'):
                        if(tem_pos[0]>next[0]):
                            if((store.matrix[tem_pos[1]+1][tem_pos[0]]==1) or ((store.matrix[tem_pos[1]-1][tem_pos[0]]==1))):
                                cmdArray = cmdArray+'S'
                else:
                    if(tem_dir=='N'):
                        if(tem_pos[1]>next[1]):
                            cmdArray = cmdArray+'S'
                    if(tem_dir=='S'):
                        if(tem_pos[1]<next[1]):
                            cmdArray = cmdArray+'S'
                    if(tem_dir=='E'):
                        if(tem_pos[1]>next[1]):
                            cmdArray = cmdArray+'L'
                            tem_dir = 'N'
                        elif tem_pos[1]<next[1]:
                            cmdArray = cmdArray+'R'
                            tem_dir = 'S'
                    if(tem_dir=='W'):
                        if(tem_pos[1]>next[1]):
                            cmdArray = cmdArray+'R'
                            tem_dir = 'N'
                        elif tem_pos[1]<next[1]:
                            cmdArray = cmdArray+'L'
                            tem_dir = 'S'
                tem_pos = next
            cmdArray = cmdArray+'H'
        cmdArray = cmdArray[0:len(cmdArray)-2]+'E'
        return cmdArray              
    def update_dir_pos(self,dir,pos):
        self.dir = dir
        self.pos = pos
    def command(self,store,stop_points):
        paths=[]
        tem_pos=self.pos
        points = stop_points
        while points:
            points=sorted(points,key=lambda x:abs(x[0]+x[1]-tem_pos[0]-tem_pos[1]))
            paths.append(store.pathfinder(tem_pos,points[0]))
            tem_pos = points[0]
            points.remove(points[0])
        paths.append(store.pathfinder(tem_pos,self.billing))
        #print(paths)
        cmdArray = self.__encodeJson(paths,store)
        print(cmdArray)
        return cmdArray


# matrix_in = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# ]
# start_node = [23,16]
# end_node = [6,3]
# x = store(matrix_in)
# # x.pathfinder(start_node,end_node)
# b1 = bot(start_node,"N",,[23,18])
# b1.command(x,[[4,3],[6,3]])