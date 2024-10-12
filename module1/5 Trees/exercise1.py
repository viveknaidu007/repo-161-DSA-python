class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        level = self.get_level()
        prefix = " " * 3 * level + "|__Level" if level > 0 else "|__Level"
        
        print(f"{prefix} {level} {self.data}")
        for child in self.children:
            child.print_tree()

def full_tree():
    root = TreeNode("Nilupul (CEO)")
    
    cto = TreeNode("Chinmay (CTO)")

    ih = TreeNode("Vishwa (Infrastructure Head)")

    ih.add_child(TreeNode("Dhaval (Cloud Manager)"))
    ih.add_child(TreeNode("Abhijit (App Manager)"))

    cto.add_child(ih)

    cto.add_child(TreeNode("Aamir (Application Head)"))

    hr = TreeNode("Gels (HR Head)")
    hr.add_child(TreeNode("Peter (Recruitment Manager)"))
    hr.add_child(TreeNode("Waqas (Policy Manager)"))

    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()

def name_tree():
    root = TreeNode("Nilupul")
    
    cto = TreeNode("Chinmay")

    ih = TreeNode("Vishwa")

    ih.add_child(TreeNode("Dhaval"))
    ih.add_child(TreeNode("Abhijit"))

    cto.add_child(ih)

    cto.add_child(TreeNode("Aamir"))

    hr = TreeNode("Gels")
    hr.add_child(TreeNode("Peter"))
    hr.add_child(TreeNode("Waqas"))

    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()
    
def designation_tree():
    root = TreeNode("CEO")
    
    cto = TreeNode("CTO")

    ih = TreeNode("Infrastructure Head")

    ih.add_child(TreeNode("Cloud Manager"))
    ih.add_child(TreeNode("App Manager"))

    cto.add_child(ih)

    cto.add_child(TreeNode("Application Head"))

    hr = TreeNode("HR Head")
    hr.add_child(TreeNode("Recruitment Manager"))
    hr.add_child(TreeNode("Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()

if __name__ == "__main__":
    prefix = "-" * 15
    suffix = "-" * 15

    print(f"\n{prefix} Full Tree {suffix}")
    full_tree()

    print(f"\n{prefix} Name Tree {suffix}")
    name_tree()

    print(f"\n{prefix} Designation Tree {suffix}")
    designation_tree()