from time import time

def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in range(0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iwords[i] == words[i]:
                if (iwords[+i] == words[+i]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors 

def typingSpeed(iprompt, stime, etime):
    global time
    global iwords
    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

def timeElapsed(stime, etime):
    time = etime - stime

    return time

if __name__ == '__main__':
    prompt = "Imagine each paragraph as a sandwich. The real content of the sandwich—the meat or other filling—is in the middle. It includes all the evidence you need to make the point. But it gets kind of messy to eat a sandwich without any bread. Your readers don’t know what to do with all the evidence you’ve given them. So, the top slice of bread (the first sentence of the paragraph) explains the topic (or controlling idea) of the paragraph. And, the bottom slice (the last sentence of the paragraph) tells the reader how the paragraph relates to the broader argument. In the original and revised paragraphs below, notice how a topic sentence expressing the controlling idea tells the reader the point of all the evidence."
    print("Type this :- ' ", prompt, "'") # this syntax change by according to you ! 
    
    input("press ENTER when you are ready !")
    
    stime = time()
    iprompt = input()
    etime = time()

    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    print("Total Time Elapsed : ", time, "s")
    print("Your Average Typinf Speed was : ", speed, "words / minute")
    print("With a total of : ",  errors, "errors")

