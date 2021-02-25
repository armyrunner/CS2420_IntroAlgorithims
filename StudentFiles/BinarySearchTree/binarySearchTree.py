class Node:

    def __init__(self,Item):
        self.mItem = Item
        self.mLeft = None
        self.mRight = None


class binarySearchTree:


    def __init__(self):
        self.mRoot = None

    def Insert(self,Item):

        if self.Exists(Item):
            return False

        self.mRoot = self.Insert_Recursive(Item,self.mRoot)

        return True
    
    def Insert_Recursive(self,Item,current):
        if current is None:
            current = Node(Item)
        elif Item < current.mItem:
            current.mLeft = self.Insert_Recursive(Item,current.mLeft)
        else:
            current.mRight = self.Insert_Recursive(Item,current.mRight)
        return current

    def Exists(self,Item):
        if self.mRoot is None:
            return False
        return self.Exists_Recursive(Item,self.mRoot)

    def Exists_Recursive(self,Item,current):  
        if current is None:
            return False
        elif current.mItem == Item:
            return True
        elif Item > current.mItem:
            return self.Exists_Recursive(Item,current.mRight)
        else:
            return self.Exists_Recursive(Item,current.mLeft)

    def Retrieve(self,Item):
        if not self.Exists(Item):
            return None #was false
        return self.Retrieve_Recursive(Item,self.mRoot)
    
    def Retrieve_Recursive(self,Item,current):
        if current.mItem == Item:
            return current.mItem # had return true
        elif current.mItem < Item:
            return self.Retrieve_Recursive(Item,current.mRight)
        else:
            return self.Retrieve_Recursive(Item,current.mLeft)

    def Traverse(self,callback):
        current = mFirst
        self.Traverse_Recursive(current,callback)

    def Traverse_Recursive(self,Item,callback):
        if current is None:
            return current
        else:
            callback(current,mItem)
            self.Traverse_Recursive(current.mRight,callback)
            self.Traverse_Recursive(current.mLeft,callback)

    def Delete(self,Item):
        if self.Exists(Item) == False:
            return False
        self.mRoot = self.Delete_Recursive(Item,self.mRoot)

        return True


    def Delete_Recursive(self,Item,current):

        if Item < current.mItem:
            current.mLeft = self.Delete_Recursive(Item,current.mLeft)
        elif Item > current.mItem:
            current.mRight = self.Delete_Recursive(Item,current.mRight)
        else:

            if current.mRight is None and current.mLeft is None:
                current = None

            elif current.mRight is None:
                current = current.mLeft
            
            elif current.mLeft is None:
                current = current.mRight
        
            else:
                s = current.mRight
                while s.mLeft:
                    s = s.mLeft

                current.mItem = s.mItem

                current.mRight = self.Delete_Recursive(s.mItem,current.mRight)

        return current

    def Size(self):
        return self.size_recursive(self.mRoot)

    def size_recursive(self,current):
        if current is None:
            return False
        return  1 + self.size_recursive(current.mLeft) + self.size_recursive(current.mRight)