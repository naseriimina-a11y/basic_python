l = {1:{"city":"shiraz",  "pop(million)":1.57, "Area(km^2)":240},
     2:{"city":"isfahan", "pop(million)":1.96, "Area(km^2)":551},
     3:{"city":"ahvaz",   "pop(million)":1.18, "Area(km^2)":185},
     4:{"city":"tabriz",  "pop(million)":1.60, "Area(km^2)":324},
     5:{"city":"mashhad", "pop(million)":3.00, "Area(km^2)":328}}

max_pop = 0
max_area = 0
min_area = 1e12

for k,v in l.items() :
    if v["pop(million)"] > max_pop :
        max_pop = v["pop(million)"]
        max_pop_city = v["city"]
    if v["Area(km^2)"] > max_area :
        max_area = v["Area(km^2)"]
        max_area_city = v["city"]

    if v["Area(km^2)"]< min_area :
        min_area = v["Area(km^2)"]
        min_area_city = v["city"]

print ('max population city: ' ,max_pop_city ,':',max_pop)
print ('max area city: ' ,max_area_city ,':',max_area)
print ('min area city: ' ,min_area_city ,':',min_area)


