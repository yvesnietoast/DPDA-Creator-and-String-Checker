import re
# Author: Yves Nieto
# Date created: 12/03/23
# DPDA CREATOR AND STRING CHECKER

#Transition Class
class Transition:
    def __init__(self,currState,inputSymbol
                 ,stackTop,nextState,stackTopRep):
        self.currState=currState
        self.inputSymbol=inputSymbol
        self.stackTop=stackTop
        self.nextState=nextState
        self.stackTopRep=stackTopRep
    def printTransition(self):
        string="["+str(self.inputSymbol).replace("-","eps")+","+str(self.stackTop).replace("-","eps")+"-> "+"".join(self.stackTopRep).replace("-","eps")+"]"
        print(string)
    def printStackTopRep(self):
        values = ''.join(str(v) for v in self.stackTopRep)
        return values
#Get states
def getStatesNum():
    return eval(input("Enter number of states:\n"))

#Get alphabet
def getAlphabet():
    Alphabet=input("Enter input alphabet as a comma separated list of symbols: (Use ` for a minus sign)\n")
    Alphabet=re.split(r'[,]+',Alphabet)
    return Alphabet

#Get Accept states
def getAcceptStates(statesNum):
    stateAccept=input("Enter accepting States as a comma-separated list of integers:\n")
    stateAccept=re.split(r'[,]+',stateAccept)
    stateAccept=[eval(i) for i in stateAccept]
    x=0
    for i in stateAccept:
        if i not in range(statesNum):
            print("invalid state %d; enter a value between 0 and %d" %(i,statesNum-1))
            x=1
    if x == 1:
        return getAcceptStates(statesNum)
    else:
        return stateAccept
#Get Transition rules
def getStateTrans(numStates):
    transRules=[]
    for state in range(numStates):
        print("Transistions for state %d\n" %(state))
        for trans in transRules:
            if(trans.currState==state):
                trans.printTransition()
        ans=input("Need a transition rule for state %d ? (y or n)" %(state))
        while(ans=="y"):
            x=addTransRule(state,transRules)
            if(x==0):
                next
            else:
                transRules.append(x)

            print("Transitions for state "+str(state)+":")
            for trans in transRules:
                if(trans.currState==state):
                    trans.printTransition()
            ans=input("Need a transition rule for state %d ? (y or n)" %(state))

    return transRules
#Add Transition Rules
def addTransRule(state,array):
    read=input("Input Symbol to read (enter - for epsilon): ")
    stack=input("Stack Symbol to match and pop (enter - for epsilon): ")
    transState=input("State to transition to: ")
    push=input("Stack symbols to push as comma separated list, first symbol to top of stack (enter - for epsilon): ")
    push=re.split(r'[,]+',push)
    newTransRule=Transition(state,read,stack,transState,push)
    for transitions in array:
        if((newTransRule.inputSymbol=="-" and newTransRule.stackTop=="-" and transitions.currState==newTransRule.currState)or(transitions.inputSymbol=="-" and transitions.stackTop=="-" and transitions.currState==newTransRule.currState)):
            print("Violation of DPDA due to epsilon input/epsilon stack transition from state "+str(state)+":")
            transitions.printTransition()
            return 0
        if((newTransRule.currState==transitions.currState) and (newTransRule.stackTop=="-")and (newTransRule.inputSymbol==transitions.inputSymbol)):
            print("Violation of DPDA due to epsilon stack transition from state "+str(state)+":")
            transitions.printTransition()
            return 0
        if((newTransRule.inputSymbol=="-") and(newTransRule.stackTop==transitions.stackTop)and(newTransRule.currState==transitions.currState)):
            print("Violation of DPDA due to epsilon input transition from state "+str(state)+":")
            transitions.printTransition()
            return 0
        if(((newTransRule.inputSymbol==transitions.inputSymbol) and (newTransRule.stackTop==transitions.stackTop)) and (newTransRule.currState==transitions.currState)):
            if(newTransRule.stackTop=="-"):
                print("Violation of DPDA due to mismatched stack transition from state "+str(state)+":")
                transitions.printTransition()
            else:
                print("Violation of DPDA due to multiple transitions for the same input and stack top from state "+ str(state) + ":")
                transitions.printTransition()
            return 0
    return newTransRule
#Prints All Transition rules
def printAllTransitions(numStates,transRules):
    print("Printing all Transitions...")
    for states in range(numStates):
        print("Transitions for state",str(states)+":")
        for transitions in transRules:
            if(transitions.currState==states):
                transitions.printTransition()

            
#Process String
    #Transition(currState,inputSymbol,stackTop,nextState,stackTopReplacement)
def processString(transRules):
    string=input("Enter a string to be processed by the PDA:")
    ogstring=string
    output=""
    currentState=0
    inputEps="-"
    stack=[]
    stuck=1
    for i in range(len(ogstring)):    
        stuck=1
        while(stuck):
            for trans in transRules:
                # #epsilon input string
                # if((trans.currState==currentState) and (inputEps==trans.inputSymbol)):
                #     #check if matches top of stack or if stacktop is epsilon
                #     print("HELP")
                #     if((trans.stackTop=="-")):
                #         print("HELLO")
                #         output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ','.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if trans.inputSymbol=='-' else trans.inputSymbol},{'eps' if trans.stackTop=='-' else trans.stackTop}->{'eps' if trans.printStackTopRep()=='-'else trans.printStackTopRep()}]-->"
                #         if(trans.printStackTopRep()=="-"):
                #             currentState=trans.nextState
                #             print(output)
                #             continue
                #         else:
                #             for i in reversed(trans.stackTopRep):
                #                 stack.append(i)
                #             currentState=trans.nextState
                #             print(output)
                #             print("AUGH")
                #             continue
                #     #epsilon Transition with Pop match Stack
                #     if(stack[-1]==trans.stackTop):
                #         print("here")
                #         output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ','.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if trans.inputSymbol=='-' else trans.inputSymbol},{'eps' if trans.stackTop=='-' else trans.stackTop}->{'eps' if trans.printStackTopRep()=='-'else trans.printStackTopRep()}]-->"
                #         stack.pop()
                #         if(trans.printStackTopRep()=="-"):
                #             currentState=trans.nextState

                #             continue
                #         else:
                #             for i in reversed(trans.stackTopRep):
                #                 stack.append(i)
                #             currentState=trans.nextState
                #             continue

                if(string!=""):
                    for transs in transRules:
                        if((transs.currState==currentState) and (string[0]==transs.inputSymbol)):
                            if(transs.stackTop=="-"):
                                rep=transs.printStackTopRep()
                                output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ','.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if transs.inputSymbol=='-' else transs.inputSymbol},{'eps' if transs.stackTop=='-' else transs.stackTop}->{'eps' if transs.printStackTopRep()=='-'else transs.printStackTopRep()}]-->"
                                if(rep=="-"):
                                    currentState=transs.nextState
                                    string=string[1:]
                                    break
                                else:
                                    for i in reversed(transs.stackTopRep):
                                        stack.append(i)
                                    string=string[1:]
                                    currentState=transs.nextState
                                    break
                            if((stack[-1]==transs.stackTop) or(transs.stackTop=="-")):
                                output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ','.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if transs.inputSymbol=='-' else transs.inputSymbol},{'eps' if transs.stackTop=='-' else transs.stackTop}->{'eps' if transs.printStackTopRep()=='-'else transs.printStackTopRep()}]-->"
                                stack.pop()
                                if(transs.printStackTopRep()=="-"):
                                    currentState=transs.nextState
                                    string=string[1:]

                                    break
                                else:
                                    for i in reversed(transs.stackTopRep):
                                        stack.append(i)
                                    string=string[1:]
                                    currentState=transs.nextState
                                    # print(output)

                                    break
                    stuck=0
                if((trans.currState==currentState) and (inputEps==trans.inputSymbol)):
                    #check if matches top of stack or if stacktop is epsilon
                    if((trans.stackTop=="-")):
                        output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ''.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if trans.inputSymbol=='-' else trans.inputSymbol},{'eps' if trans.stackTop=='-' else trans.stackTop}->{'eps' if trans.printStackTopRep()=='-'else trans.printStackTopRep()}]-->"
                        if(trans.printStackTopRep()=="-"):
                            currentState=trans.nextState
                            # print(output)
                            continue
                        else:
                            for i in reversed(trans.stackTopRep):
                                stack.append(i)
                            currentState=trans.nextState
                            # print(output)
                            continue
                    #epsilon Transition with Pop match Stack
                    if(stack[-1]==trans.stackTop):
                        output+=f"(q{currentState};{'eps' if string=='' else string};{'eps'if ''.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})--[{'eps' if trans.inputSymbol=='-' else trans.inputSymbol},{'eps' if trans.stackTop=='-' else trans.stackTop}->{'eps' if trans.printStackTopRep()=='-'else trans.printStackTopRep()}]-->"
                        stack.pop()
                        if(trans.printStackTopRep()=="-"):
                            currentState=trans.nextState

                            continue
                        else:
                            for i in reversed(trans.stackTopRep):
                                stack.append(i)
                            currentState=trans.nextState
                            continue
                if(string==""):
                    stuck=0
                
                
            #print(output)
            
            continue
            #inputString Matches Rule
    print(f"Accept string {ogstring}? ", end="")
    if((currentState in acceptState) and (string=="")):
        print("true")
    else:
        print("false")
    print(output+f"(q{currentState};{'eps' if string=='' else string};{'eps'if ''.join(str(v)for v in stack)=='' else ''.join(str(v)for v in stack)[::-1]})")
    processString(transRules)

    
if __name__ == "__main__":
    numStates=getStatesNum()
    alphabet=getAlphabet()
    acceptState=getAcceptStates(numStates)
    transRules=getStateTrans(numStates)
    #EXAMPLE1
    #transRules=[Transition(0,"-","-",1,["S","$"]),Transition(1,"a","S",2,["a","S","a"]),Transition(1,"b","S",3,["b","S","b"]),Transition(1,"c","S",4,["c"]),Transition(1,"a","a",1,["-"]),Transition(1,"-","$",5,["-"]),Transition(2,"-","a",1,["-"]),Transition(3,"-","b",1,["-"]),Transition(4,"-","c",1,['-']),Transition(1,"b","b",1,["-"])]
    
    #EXAMPLE2
    # transRules=[Transition(0,"-",'-',1,['$']),Transition(1,"0",'-',1,['0']),Transition(1,'1','0',2,['-']),Transition(2,'1','0',2,'-'),Transition(2,"-",'$',3,['-']),Transition(3,'1','-',4,['1','$']),Transition(4,'1','-',4,['1']),Transition(4,'0','1',5,['-']),Transition(5,"0",'1',5,['-']),Transition(5,'-','$',6,['-'])]
    # numStates=4
    # alphabet=["0",'1']
    # acceptState=[3]
    
    #PART 2
    # transRules=[Transition(0,"-",'-',1,['E','$']),Transition(1,'-','E',2,['T','G']),Transition(2,'-','T',3,['F','H']),Transition(3,'(',"F",4,['E',')']),Transition(3,'9','F',5,['-']),Transition(3,'8','F',5,['-']),Transition(3,'7','F',5,['-']),Transition(3,'6','F',5,['-']),Transition(3,'5','F',5,['-']),Transition(3,'4','F',5,['-']),Transition(3,'3','F',5,['-']),Transition(3,'2','F',5,['-']),Transition(3,'1','F',5,['-']),Transition(3,'0','F',5,['-']),Transition(4,'-','E',2,['T','G']),Transition(5,"*",'H',3,['F','H']),Transition(5,'/','H',3,['F','H']),Transition(5,')',')',5,['-']),Transition(5,'`','G',2,['T','G']),Transition(5,'+','G',2,['T','G']),Transition(5,'-','$',6,['-']),Transition(5,'-','H',5,['-']),Transition(5,'-','G',5,['-'])]
    # numStates=7
    # alphabet=["4","+","`",'/','*','(',')']
    # acceptState=[6]
    
    printAllTransitions(numStates,transRules)
    processString(transRules)