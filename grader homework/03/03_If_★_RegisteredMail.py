G = int(input())
if G <= 100:
  print('18')
elif G > 100 and G <= 250:
  print('22')
elif G > 250 and G <= 500:
  print('28')
elif G > 500 and G <= 1000:
  print('38')
elif G > 1000 and G <= 2000:
  print('58')
else:
  print('Reject')