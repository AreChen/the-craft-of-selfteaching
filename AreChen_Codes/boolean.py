from IPython.core.interactiveshell import InteractiveShell as Is
Is.ast_node_interactivity = "all"
a = 1==2
b = 1!=2
print(a,b)