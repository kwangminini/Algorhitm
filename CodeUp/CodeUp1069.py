n=input()

def f(ch):
    return{
        'A':"best!!!",
        'B':"good!!",
        'C':"run!",
        'D':"slowly~"
        }.get(ch, "what?")

print(f(n))