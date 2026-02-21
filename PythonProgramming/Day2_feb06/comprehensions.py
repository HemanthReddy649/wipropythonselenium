# comprehensions -create lits using line of code instead of loops

#syntax

#[expression for item in iterable if condition]

#square of number
sqs=[x*x for x in range(1,6)]
print(sqs)

#with condition

sqs=[x for x in range(10) if x%2==0]
print(sqs)

#dic comprehension---INCREASE BY 10%

salary={
    "A":50000,"B":60000,"C":70000
}
update={k:v+0.1*v for k,v in salary.items()}
print(update)


#condition

#filtering of dict
employees={
    'harsha':"active",
    "amit":"inactive",
    "ravi":"active"
}
upd={k:v for k,v in employees.items() if v=="active"}
print(upd)


#set comprehensions

sqs={x**2 for x in range(1,6)}
print(sqs)

#condition

sqs={x for x in range(10) if x%2==0}
print(sqs)