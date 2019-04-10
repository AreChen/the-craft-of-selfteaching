import matplotlib.pyplot as ht
labels = ['Major Match','']
sizes = [273,727]
colors = ['#E2E2E2', '#6392BF']
explode = (0,0.08)
ht.figure(figsize=(7,7))
ht.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct='%1.1f%%',
    colors=colors,
    startangle=270,
    shadow=True
    )
ht.savefig('UniStudent_Major_Match.png',transparent=True)
ht.show()
