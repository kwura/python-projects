# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo"). 
  
  # create a set of unique sites 
  unique_sites = set(site_list)

  # create dictionary w/ sites as keys and values as empty set to store users who visited the site
  site_dict = {}
  
  for i in unique_sites:
    site_dict[i] = set()

  # go through site list and and add users to the dictionary w/ sites
  for i in range(len(site_list)):
    site_dict[site_list[i]].add(user_list[i])

  # track highest affinity and the pair of websites
  highest_affinity_counter = 0
  highest_affinity_pair = None

  # go through all pairs of websites and start counting!
  unique_sites_list = list(unique_sites)

  for i in range(len(unique_sites_list) - 1):
    for j in (unique_sites_list[ i + 1 :]):
      # Get a pair of websites
      current_pair = unique_sites_list[i], j 
      
      # find the set of common users that they share. Think intersection
      common_set_of_users = site_dict[unique_sites_list[i]] & site_dict[j]

      # count the number of common users
      affinity_counter = len(common_set_of_users)

      # check if this affinity is larger than the current highest infinity count
      if(affinity_counter >= highest_affinity_counter):
        highest_affinity_counter = affinity_counter

        highest_affinity_pair = current_pair
  
  # At this point all pairs of websites have been checked
  
  # sort real quick cause the test cases are strict on order
  fix_order = list(highest_affinity_pair)
  
  fix_order.sort()
  
  highest_affinity_pair = tuple(fix_order)

  return highest_affinity_pair