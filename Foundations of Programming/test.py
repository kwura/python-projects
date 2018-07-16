def main():

  new = {}
  old = {}
  old["hi"] = 1
  old["sup"] = 1
  old["ok"] = 2
  old["nope"] = 3
  old["yes"] = 4
  old["huh"] = 4
  print(old)
  for key in old:
    new_key = old[key]
    if (new_key in new):
      new[new_key].append(key)
    else: 
      new_list = []
      new_list.append(key)
      new[new_key] = new_list

  print(new)
main()
  