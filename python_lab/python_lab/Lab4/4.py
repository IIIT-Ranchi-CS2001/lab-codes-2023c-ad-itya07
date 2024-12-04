# Q4: Set operations with singers and dancers
singers = {name for name in input("Enter singers' names separated by space: ").split()}
dancers = {name for name in input("Enter dancers' names separated by space: ").split()}

artists = singers | dancers
allrounders = singers & dancers
only_dancers = dancers - singers
only_singers = singers - dancers
dancers_or_singers = only_dancers | only_singers

print("All Artists:", artists)
print("Allrounders (both singers and dancers):", allrounders)
print("Dancers but not singers:", only_dancers)
print("Singers but not dancers:", only_singers)
print("Singers or dancers but not both:", dancers_or_singers)