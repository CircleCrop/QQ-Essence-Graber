import essence
order = 1
group_id = 1234567
cookie = ''
while(order<=1000):
    out = str(essence.get(order,group_id,cookie)) + ','
    print(out)
    order += 1
