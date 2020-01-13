class Token(object):
    #Creates token objects with type (Integer, Mul, Add) and value (0,1,2,3,4,5,6,7,8,9, *, +,/)
    #value is a number for numbers and a string for * or +
    def __init__(self,type,value):
        self.type = type
        self.value = value
    #Prints a string of info held in token
    def __str__(self):
        return 'Token(' + str(self.type)+', ' + str(self.value) + ')'


class Reader(object):

    #Creates char-by-char reader of string text
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.curr_char = self.text[self.index]
    #Replaces self.text with string without spaces
    def remove_space(self):
        new_string = ''
        for char in self.text:
            if char != ' ':
                new_string += char
        self.text = new_string

    #Advances to next char, stopping if it reaches the end of the string
    def move_next_char(self):
        self.index += 1
        if self.index > len(self.text)-1:
            self.curr_char = None
        else:
            self.curr_char = self.text[self.index]
    #For ints that have more than 1 digit, since reader goes digit by digit
    def get_integer(self):
        ret = ''
        while self.curr_char is not None and (self.curr_char.isdigit() or self.curr_char == '-'):
            ret += self.curr_char
            self.move_next_char()
        return int(ret)
    #Returns a token of type for the char, then moves on to next char
    def tokenizer(self):
        while self.curr_char is not None:
            if self.curr_char.isdigit() or self.curr_char == '-':
                return Token("Integer", self.get_integer())

            if self.curr_char == '+':
                self.move_next_char()
                return Token("Add", '+')
            if self.curr_char == '*':
                self.move_next_char()
                return Token("Mul",'*')
            if self.curr_char == '/':
                self.move_next_char()
                return Token("Div",'/')
#For data structure

class Number(object):
    def __init__(self,token):
        self.token = token
        self.value = token.value

class Mul(object):
    def __init__(self, token):
        self.token = token
        self.operation = '*'
        self.left = None
        self.right = None

class Add(object):
    def __init__(self, token):
        self.token = token
        self.operation = '+'
        self.left = None
        self.right = None

class Div(object):
    def __init__(self,token):
        self.token = token
        self.operation = '/'
        self.left = None
        self.right = None


def parser(str):
    a = Reader(str)
    a.remove_space()
    array_of_tokens = []
    #Create list of all tokens
    while a.curr_char is not None:
        array_of_tokens.append(a.tokenizer())
    #Throws error if * or + are at beginning of sentence
    if array_of_tokens[0].type != "Integer":
        print("Invalid input!")
        return
    #create array of nodes
    array_of_nodes = []
    #converting array of tokens to array of nodes
    for i in array_of_tokens:
        if i.type == "Integer":
            temp = Number(i)
        if i.type == "Mul":
            temp = Mul(i)
        if i.type == "Add":
            temp = Add(i)
        if i.type == "Div":
            temp = Div(i)
        array_of_nodes.append(temp)
    #Check that the array of nodes is a valid arithmetic expression
    #for i in range(0,len(array_of_nodes)):
     #   if i%2==0:
      #      if type(array_of_nodes[i]) != Number:
       #         print("Invalid input!")
        #        return
        #if i%2 == 1:
         #   if type(array_of_nodes[i]) != Add or type(array_of_nodes[i]) != Mul or type(array_of_nodes[i]) != Div:
          #      print("Invalid input")
           #     return
    #Assign left and right Integer tokens to Add/Mul operator tokens, also create new array of operator nodes ONYLY
    array_of_ops = []
    i = 0
    while i < len(array_of_nodes)-1:
        array_of_nodes[i+1].left = array_of_nodes[i]
        array_of_nodes[i+1].right = array_of_nodes[i+2]
        array_of_ops.append(array_of_nodes[i+1])
        i = i+2

    root = array_of_ops[0]
    #Function for combining trio with left priority, returns node which should be root
    def combine_left_prio(node1,node2):
        node2.left = node1
        return node2
    #Function for combining trio with right priority, returns node which should be root
    def combine_right_prio(node1,node2):
        node1.right = node2
        return node1
    j = 1
    while j < len(array_of_ops):
        if root.operation == '+' and array_of_ops[j].operation == '*':
            root = combine_right_prio(root,array_of_ops[j])
        elif root.operation == '+' and array_of_ops[j].operation == '/':
            root = combine_right_prio(root,array_of_ops[j])
        else:
            root = combine_left_prio(root,array_of_ops[j])
        j+=1
    return root

def eval(root):
    #Base case
    if type(root.left) == Number and type(root.right) == Number:
        if type(root)== Add:
            return root.left.value + root.right.value
        elif type(root) == Mul:
            return root.left.value * root.right.value
        elif type(root) == Div:
            return root.left.value // root.right.value
    #Recursion: Cases where left node, right node, or both nodes are not numbers
    if type(root.left) == Number and type(root.right)!= Number:
        if type(root) == Add:
            return root.left.value + eval(root.right)
        elif type(root) == Mul:
<<<<<<< HEAD
            return root.left.value * eval(root.right)
=======
            return root.left.value + eval(root.right)
>>>>>>> e7a59291695bfa23ccc034c84c8af7c5050f3736
        elif type(root) == Div:
            return root.left.value // eval(root.right)

    if type(root.left) != Number and type(root.right) == Number:
        if type(root)== Add:
            return eval(root.left)+root.right.value
<<<<<<< HEAD
        elif type(root) == Mul:
=======
        elif type(root) == Div:
>>>>>>> e7a59291695bfa23ccc034c84c8af7c5050f3736
            return eval(root.left)*root.right.value
        elif type(root) == Div:
            return eval(root.left)//root.right.value
    if type(root.left)!= Number and type(root.right) != Number:
        if type(root)==Add:
            return eval(root.left)+eval(root.right)
        elif type(root) == Mul:
            return eval(root.left)*eval(root.right)
        elif type(root) == Div:
            return eval(root.left)//eval(root.right)
<<<<<<< HEAD



#### Added token + class for div and added logic. Need to fix tree.
###

=======


a = parser('2/5 + 6*7')
print(eval(a))


#### Added token + class for div and added logic. Need to fix tree.
###

>>>>>>> e7a59291695bfa23ccc034c84c8af7c5050f3736
#test