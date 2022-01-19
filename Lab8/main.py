class dane(object):
  def __init__(self, v, p, d):
    self.odwiedzony = v
    self.poprzednik = p
    self.dystans = d

  def szukajMinimum(tab):
    min = -1
    mindist = sys.maxsize
    for i in range(0, len(macierz)):
      if ((not tab[i].odwiedzony) and tab[i].dystans < mindist):
        min = i
        mindist = tab[i].dystans
    return min

  def Dijkstra(macierz, start):
    tab = []
    for i in range(0, len(macierz)):
      tab.append(dane(False, -1, sys.maxsize))
    tab[start].dystans = 0
    u = start
    while (u != -1):
      tab[u].odwiedzony = True
      for i in range(0, len(macierz)):
        if (macierz[u][i] > 0 and tab[u].dystans + macierz[u][i] < tab[i].dystans):
          tab[i].dystans = tab[u].dystans + macierz[u][i]
          tab[i].poprzednik = u
      u = szukajMinimum(tab)
    return tab

  n = int(input('Podaj ile węzłów ma graf\n n = '))
  s = int(input('Podaj węzeł startowy\n s = '))
  print('Podaj elementy macierzy:')
  macierz = []
  for i in range(0, n):
    tab = [int(x) for x in input().split()]
    macierz.append(tab)

  tab = Dijkstra(macierz, s)
  for i in range(0, n):
    wypiszDane(i, tab[i])

  def wypiszDane(i, d):
    txt = str(i) + "\t"
    if (not d.odwiedzony):
      txt += "nieodwiedzony"
    else:
      if (d.poprzednik == -1):
        txt += "brak"
      else:
        txt += str(d.poprzednik)
      txt += "\t" + str(d.dystans)
    print(txt);