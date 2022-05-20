star2movies = {}
for i in range(int(input())):
    title, star1, star2 = input().split(",")
    title = title.strip(); star1 = star1.strip(); star2 = star2.strip()
    if star1 not in star2movies:
        star2movies[star1] = [title]
    else:
        star2movies[star1].append(title)
    if star2 not in star2movies:
        star2movies[star2] = [title]
    else:
        star2movies[star2].append(title)
print(star2movies)
star = input().split(',')
for i in star:
    if i.strip() in star2movies:
        print('%s -> %s' %(i.strip(),', '.join(star2movies[i.strip()])))
    else:
        print('%s -> Not found' %(i.strip()))