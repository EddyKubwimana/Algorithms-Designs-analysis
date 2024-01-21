

class Tree:

    def __init__(self, value):

        self.data = value
        self.left = None
        self.right = None
    

    def addNode(self,value):

        if self.data>value :
                if self.left == None:
                    self.left = Tree(value)
                    return 

                else:

                    self.left.addNode(value)


        if self.data< value :
            if self.right == None:
                    self.right = Tree(value)
                    return
            else:
                self.right.addNode(value)


    def levelTraversal(self):
         
        
         
         queueLevel = [self]

         counter = 1

         while queueLevel:

            curr_level = queueLevel.pop(0)
            
            if curr_level.left:

                queueLevel.append(curr_level.left)

            if curr_level.right :
                    queueLevel.append(curr_level.right)

            print(curr_level.data)
            



        
                   
                
                   

              
            

              
         
         
         

         
         




        


       


        



#testing :
                

tree = Tree(50)
tree.addNode(10)
tree.addNode(5)
tree.addNode(1)
tree.addNode(60)
tree.addNode(90)
tree.addNode(75)
tree.levelTraversal()





