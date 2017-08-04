STSTS

#step 1:straight
#step 2:(iterate)
#step 3:right 90
#step 4:(iterate)
#step 5:straight
#step 6:(iterate)
#step 7:right 90
#step 8:(iterate)

import turtle

def steps(reps):
    for i in range(reps):
        lst=[S,T,S,T,S]
        if i%2==0:
            for k in len(lst):
                if lst[k]==T:
                    lst[k]=R
        else:
            for k in len(lst):
                if lst[k]==T:
                    lst[k]=L
        for m in len(lst):
            lst[m]=lst[m]+#append step to instructions after each existing step
#return list of instructions
#check def steps for desired output

def follow_instructions(reps,turtle)
    instructs=steps(reps)
    for i in range len(instructs):
        if instructs[i]==R:
            turtle.right(90)
        elif instructs[i]==L:
            turtle.left(90)
        elif instructs[i]==S:
            turtle.forward(200/reps)
        else:
            print('error in instructs[i]', instructs[i])
            print(instructs)
#follow_instructions(reps,turtle)