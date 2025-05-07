#E Creamer
#5/6/2025
#String Function Demo

#gets users input and puts it lower case
user = input("Enter a string and I will tally all of the letters: ").lower()
#declares all my counting varaibles
a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0

#a for loop that loops through each letter in the users output
for xe in range(len(user)):

    #and findsout what they are, and adds 1 to its respective counter

    if user[xe] == "a":
        a += 1
    elif user[xe] == "b":
        b += 1
    elif user[xe] == "c":
        c += 1
    elif user[xe] == "d":
        d += 1
    elif user[xe] == "e":
        e += 1
    elif user[xe] == "f":
        f += 1
    elif user[xe] == "g":
        g += 1
    elif user[xe] == "h":
        h += 1
    elif user[xe] == "i":
        i += 1
    elif user[xe] == "j":
        j += 1
    elif user[xe] == "k":
        k += 1
    elif user[xe] == "l":
        l += 1
    elif user[xe] == "m":
        m += 1
    elif user[xe] == "n":
        n += 1
    elif user[xe] == "o":
        o += 1
    elif user[xe] == "p":
        p += 1
    elif user[xe] == "q":
        q += 1
    elif user[xe] == "r":
        r += 1
    elif user[xe] == "s":
        s += 1
    elif user[xe] == "t":
        t += 1
    elif user[xe] == "u":
        u += 1
    elif user[xe] == "v":
        v += 1
    elif user[xe] == "w":
        w += 1
    elif user[xe] == "x":
        x += 1
    elif user[xe] == "y":
        y += 1
    elif user[xe] == "z":
        z += 1

#prints all counting varaibles with the corresponding letter next to it
print("\na", a,"\nb", b,"\nc", c,"\nd", d,"\ne", e,"\nf", f,"\ng", g,"\nh", h,"\ni", i,"\nj",j,"\nk", k,"\nl", l,"\nm", m,"\nn", n,"\no", o,"\np", p,"\nq", q,"\nr", r,"\ns", s,"\nt", t,"\nu", u,"\nv", v,"\nw", w,"\nx", x,"\ny", y, "\nz", z)