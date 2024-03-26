class Solution:
    def treeFromString(self, s : str) -> Optional['Node']:
        if not s:
            return None
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                root_val_end = i
                break
            i += 1
        if i == len(s):
            return Node(int(s))
        value = int(s[:root_val_end])
        root = Node(value)
        
        counter = 0
        for i in range(root_val_end, len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1
            if counter == 0:
                root.left = self.treeFromString(s[root_val_end+1:i])
                if i+2 < len(s):
                    root.right = self.treeFromString(s[i+2:-1])
                break
        return root