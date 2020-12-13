#Class of NFA
class NFA:
    current_state = None    
    def __init__(self, states, alphabet, Transition_Table, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.Transition_Table = Transition_Table
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
    def Moving_on_next_State(self, input_value):
        if ((self.current_state, input_value) not in self.Transition_Table.keys()):
            self.current_state = None
            return
        self.current_state = self.Transition_Table[(self.current_state, input_value)]
        return
    
    def CheckingIfOnAcceptState(self):
        return self.current_state in self.accept_states
 
    def Run_NFA_On_Input(self, input_list):
        for inp in input_list:
            self.Moving_on_next_State(inp)
        if self.CheckingIfOnAcceptState():
            self.current_state = 0
            return True
        else:
            self.current_state = 0
            return False
       





#Nfa for keywords
states_Keywords = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
alphabet_Keywords = {'i','n','t','f','l','o','a','s','r','g','w','h','e'}
Transition_Table_Keywords = dict()
Transition_Table_Keywords[(0, 'i')] = 1
Transition_Table_Keywords[(1, 'n')] = 2
Transition_Table_Keywords[(2, 't')] = 22
Transition_Table_Keywords[(0, 'f')] = 3
Transition_Table_Keywords[(3, 'l')] = 4
Transition_Table_Keywords[(4, 'o')] = 5
Transition_Table_Keywords[(5, 'a')] = 2
Transition_Table_Keywords[(0, 's')] = 7
Transition_Table_Keywords[(7, 't')] = 8
Transition_Table_Keywords[(8, 'r')] = 9
Transition_Table_Keywords[(9, 'i')] = 10
Transition_Table_Keywords[(10, 'n')] = 11
Transition_Table_Keywords[(11, 'g')] = 22
Transition_Table_Keywords[(3, 'o')] = 13
Transition_Table_Keywords[(13, 'r')] = 22
Transition_Table_Keywords[(0, 'w')] = 14
Transition_Table_Keywords[(14, 'h')] = 15
Transition_Table_Keywords[(15, 'i')] = 16
Transition_Table_Keywords[(16, 'l')] = 17
Transition_Table_Keywords[(17, 'e')] = 22
Transition_Table_Keywords[(1, 'f')] = 22
Transition_Table_Keywords[(0, 'e')] = 19
Transition_Table_Keywords[(19, 'l')] = 20
Transition_Table_Keywords[(20, 's')] = 17
start_state_Keywords = 0
accept_states_Keywords = {22}
ObjectOfKeywords = NFA(states_Keywords, alphabet_Keywords, Transition_Table_Keywords, start_state_Keywords, accept_states_Keywords)




#NFA for operators
states_Operators = {0,1,2}
alphabet_Operators = {'*','/','-','+','=','<','>'}
Transition_Table_Operators = dict()
Transition_Table_Operators[(0, '*')] = 1
Transition_Table_Operators[(0, '/')] = 1
Transition_Table_Operators[(0, '-')] = 1
Transition_Table_Operators[(0, '+')] = 1
Transition_Table_Operators[(0, '=')] = 1
Transition_Table_Operators[(0, '<')] = 1
Transition_Table_Operators[(0, '>')] = 1
Transition_Table_Operators[(0, '=')] = 2
Transition_Table_Operators[(0, '<')] = 2
Transition_Table_Operators[(0, '>')] = 2
Transition_Table_Operators[(2, '=')] = 1
start_state_Operators = 0
accept_states_Operators = {1,2}
ObjectOfOperators= NFA(states_Operators, alphabet_Operators, Transition_Table_Operators, start_state_Operators, accept_states_Operators)


#NFA for Characters
states_Characters = {0,1}
alphabet_Characters = {';','(',')','{','}','.','&','!','|'}
Transition_Table_Characters = dict()
Transition_Table_Characters[(0, ';')] = 1
Transition_Table_Characters[(0, '(')] = 1
Transition_Table_Characters[(0, ')')] = 1
Transition_Table_Characters[(0, '{')] = 1
Transition_Table_Characters[(0, '}')] = 1
Transition_Table_Characters[(0, '.')] = 1   
Transition_Table_Characters[(0, '&')] = 1
Transition_Table_Characters[(0, '!')] = 1
Transition_Table_Characters[(0, '|')] = 1
start_state_Characters = 0
accept_states_Characters = {1}
ObjectOfCharacters= NFA(states_Characters, alphabet_Characters, Transition_Table_Characters, start_state_Characters, accept_states_Characters)



#NFA for alphabets
Identifiers = []
states_alphabets = {0,1}
alphabet_alphabets= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'}
Transition_Table_alphabets = dict()
Transition_Table_alphabets[(0, 'a')] = 1
Transition_Table_alphabets[(0, 'b')] = 1
Transition_Table_alphabets[(0, 'c')] = 1
Transition_Table_alphabets[(0, 'd')] = 1
Transition_Table_alphabets[(0, 'e')] = 1
Transition_Table_alphabets[(0, 'f')] = 1
Transition_Table_alphabets[(0, 'g')] = 1
Transition_Table_alphabets[(0, 'h')] = 1
Transition_Table_alphabets[(0, 'i')] = 1
Transition_Table_alphabets[(0, 'j')] = 1
Transition_Table_alphabets[(0, 'k')] = 1
Transition_Table_alphabets[(0, 'l')] = 1
Transition_Table_alphabets[(0, 'm')] = 1
Transition_Table_alphabets[(0, 'n')] = 1
Transition_Table_alphabets[(0, 'o')] = 1
Transition_Table_alphabets[(0, 'p')] = 1
Transition_Table_alphabets[(0, 'q')] = 1
Transition_Table_alphabets[(0, 'r')] = 1
Transition_Table_alphabets[(0, 's')] = 1
Transition_Table_alphabets[(0, 't')] = 1
Transition_Table_alphabets[(0, 'u')] = 1
Transition_Table_alphabets[(0, 'v')] = 1
Transition_Table_alphabets[(0, 'w')] = 1
Transition_Table_alphabets[(0, 'x')] = 1
Transition_Table_alphabets[(0, 'y')] = 1
Transition_Table_alphabets[(0, 'z')] = 1
Transition_Table_alphabets[(1, 'a')] = 1
Transition_Table_alphabets[(1, 'b')] = 1
Transition_Table_alphabets[(1, 'c')] = 1
Transition_Table_alphabets[(1, 'd')] = 1
Transition_Table_alphabets[(1, 'e')] = 1
Transition_Table_alphabets[(1, 'f')] = 1
Transition_Table_alphabets[(1, 'g')] = 1
Transition_Table_alphabets[(1, 'h')] = 1
Transition_Table_alphabets[(1, 'i')] = 1
Transition_Table_alphabets[(1, 'j')] = 1
Transition_Table_alphabets[(1, 'k')] = 1
Transition_Table_alphabets[(1, 'l')] = 1
Transition_Table_alphabets[(1, 'm')] = 1
Transition_Table_alphabets[(1, 'n')] = 1
Transition_Table_alphabets[(1, 'o')] = 1
Transition_Table_alphabets[(1, 'p')] = 1
Transition_Table_alphabets[(1, 'q')] = 1
Transition_Table_alphabets[(1, 'r')] = 1
Transition_Table_alphabets[(1, 's')] = 1
Transition_Table_alphabets[(1, 't')] = 1
Transition_Table_alphabets[(1, 'u')] = 1
Transition_Table_alphabets[(1, 'v')] = 1
Transition_Table_alphabets[(1, 'w')] = 1
Transition_Table_alphabets[(1, 'x')] = 1
Transition_Table_alphabets[(1, 'y')] = 1
Transition_Table_alphabets[(1, 'z')] = 1
Transition_Table_alphabets[(1, '1')] = 1
Transition_Table_alphabets[(1, '2')] = 1
Transition_Table_alphabets[(1, '3')] = 1
Transition_Table_alphabets[(1, '4')] = 1
Transition_Table_alphabets[(1, '5')] = 1
Transition_Table_alphabets[(1, '6')] = 1
Transition_Table_alphabets[(1, '7')] = 1
Transition_Table_alphabets[(1, '8')] = 1
Transition_Table_alphabets[(1, '9')] = 1
Transition_Table_alphabets[(1, '0')] = 1
start_state_alphabets = 0
accept_states_alphabets = {1}
ObjectOfIdentifier= NFA(states_alphabets, alphabet_alphabets, Transition_Table_alphabets, start_state_alphabets, accept_states_alphabets)


#NFA for Numbers
Numbers = []
states_Numbers = {0,1}
alphabet_Numbers = {'1','2','3','4','5','6','7','8','9','0'}
Transition_Table_Numbers = dict()
Transition_Table_Numbers[(0, '1')] = 1
Transition_Table_Numbers[(0, '2')] = 1
Transition_Table_Numbers[(0, '3')] = 1
Transition_Table_Numbers[(0, '4')] = 1
Transition_Table_Numbers[(0, '5')] = 1
Transition_Table_Numbers[(0, '6')] = 1
Transition_Table_Numbers[(0, '7')] = 1
Transition_Table_Numbers[(0, '8')] = 1
Transition_Table_Numbers[(0, '9')] = 1
Transition_Table_Numbers[(0, '0')] = 1
Transition_Table_Numbers[(1, '1')] = 1
Transition_Table_Numbers[(1, '2')] = 1
Transition_Table_Numbers[(1, '3')] = 1
Transition_Table_Numbers[(1, '4')] = 1
Transition_Table_Numbers[(1, '5')] = 1
Transition_Table_Numbers[(1, '6')] = 1
Transition_Table_Numbers[(1, '7')] = 1
Transition_Table_Numbers[(1, '8')] = 1
Transition_Table_Numbers[(1, '9')] = 1
Transition_Table_Numbers[(1, '0')] = 1
start_state_Numbers = 0
accept_states_Numbers = {1}
ObjectOfNumbers= NFA(states_Numbers, alphabet_Numbers, Transition_Table_Numbers, start_state_Numbers, accept_states_Numbers)




#Funtion to check a word on NFAS
def GettingValue(Input):
    if ObjectOfKeywords.Run_NFA_On_Input(Input):
        print("<",Input,", Keyword >")
    elif ObjectOfOperators.Run_NFA_On_Input(Input):
        print("<",Input,", Operator >")
    elif ObjectOfCharacters.Run_NFA_On_Input(Input):
        print("<",Input,", Special Characters >")
    elif ObjectOfIdentifier.Run_NFA_On_Input(Input):
        Identifiers.append(Input)
        print('< id , ',Identifiers.index(Input), '>')
    elif ObjectOfNumbers.Run_NFA_On_Input(Input):
        Numbers.append(Input)
        print('< Num , ',Numbers.index(Input),'>' )
    else:
        print("lexical error on = ", Input)


#Getting the input from the file
File = open("C:\\Users\Syed Uzair\Desktop\CC_Lexical analyzer\TestingFile.txt", "r")

Code = File.readline()
Value = Code.split()
for i in Value:
    GettingValue(i)


print('*******************************')
print('Table for identifers')
print(Identifiers) 
print('*******************************') 
print('Table for Numbers')
print(Numbers)
