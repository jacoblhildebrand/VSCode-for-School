import numpy as np

scores = np.array([89,72,48,77,92,100])

print()
print(f'The scores are {scores} ')
print(f'The sum of the scores is {scores.sum()}')
print(f'The average of the socres is {scores.mean()}')
print(f'The standard deviation of the scores is {scores.std():.1f}')
print(f'The maximum of the scores is {scores.max()}')
print(f'The minimum of the scores is {scores.min()}')
adj_ave = (scores.sum()-scores.min())/(len(scores)-1)
print(f'The adjusted average of the scores is {adj_ave}')
print()