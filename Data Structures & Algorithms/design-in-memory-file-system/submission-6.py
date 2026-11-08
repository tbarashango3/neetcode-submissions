class TrieNode():
    def __init__(self):
        self.children = {}
        self.content = ""
        self.name = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        #if its a file path, the return only the file name
        # if its a directory path, return list of files and directory names
        #ls only lists direct neighbors of path
        curr = self.root
        if path == "/":
            return sorted(curr.children.keys())
        
        path = path.split("/")[1:]
        #print(path)
        for c in path:
            curr = curr.children[c]
        #/
        l = []
        if curr.content != "":
            l.append(curr.name)
            return l
        for child in curr.children.keys():
            l.append(child)
        return sorted(l)


        

    def mkdir(self, path: str) -> None:
        #create directories for all directories that don't exist
        curr = self.root
        path = path.split("/")[1:]
        #print(path)
        for c in path:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.name = c
        
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        #if file path does not exist, create new file with content at path
        #otherwise, add content to original content
        curr = self.root
        filePath = filePath.split("/")[1:]
        for c in filePath:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.name = c
        if curr.content:
            curr.content += content
        else:
            curr.content = content


    def readContentFromFile(self, filePath: str) -> str:
        #return file content at filePath
        filePath = filePath.split("/")[1:]
        curr = self.root
        for c in filePath:
            curr = curr.children[c]
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
