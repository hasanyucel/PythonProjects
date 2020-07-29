from parseFromN11 import ParseProduct

p1 = ParseProduct('https://urun.n11.com/uzaktan-kumanda/samsung-tv-kumandasi-orjinal-bn59-01242a-suhd-akilli-kumanda-P238001173')

print(p1.partName,p1.partTitle,p1.partCost)
print(p1.partDetails)