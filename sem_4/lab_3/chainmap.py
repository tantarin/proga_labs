from collections import ChainMap


baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
ch = ChainMap(adjustments, baseline)
c = ChainMap()
d = c.new_child()
e = c.new_child()
print(e.maps[0])
print(e.maps[-1])
print(e.parents)

d['x'] = 1
print(d['x'])
del d['x']
list(d)
len(d)
d.items()
dict(d)
