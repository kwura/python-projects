def permute (a,lo):
  hi = len(a)
  if (lo == hi):
    if(check_ab(a) and check_cd(a)):
      print(a)
  else:
  	for i in range(lo, hi):
  	  a[lo], a[i] = a[i], a[lo]
  	  permute(a, lo + 1)
  	  a[lo], a[i] = a[i], a[lo]

def check_ab(a):
  return (a.index('A') == a.index('B') + 1) or (a.index('A') == a.index('B') - 1)

def check_cd(a):
  return (a.index('C') != a.index('D') + 1) and (a.index('C') != a.index('D') - 1)

def main():
  a = ['A', 'B', 'C', 'D', 'E']
  permute(a, 0)
main()