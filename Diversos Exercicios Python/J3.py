corvinal = "sabedoria conhecimento"
grifinoria = "coragem forca"
lufalufa = "lealdade cooperacao diversao"
sonserina = "astucia pureza arrogancia"
caracteristica = 0
c = 0
g = 0
l = 0
s = 0

while caracteristica != "fim":
	caracteristica = str(input())

	if caracteristica in corvinal:
		c += 1
	if caracteristica in grifinoria:
		g += 1
	if caracteristica in lufalufa:
		l += 1
	if caracteristica in sonserina:
		s += 1

print ('corvinal ' + str(c))
print ('grifinoria ' + str(g))
print ('lufalufa ' + str(l))
print ('sonserina ' + str(s))