import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP | NP VP VP | NP VP Con VP | VP NP Con VP
  NP -> Det Nom | PropN | Adj Nom | N
  Nom -> Adj Nom | N
  PP -> Det Nom | Det Adj Nom
  VP -> V PP | V Nom | V | V PP PP | PP V
  Det -> 'с' | 'в' | 'за'
  N -> 'мальчик' | 'пёс' | 'мячом' | 'компьютер' | 'экран' | 'столом'
  V -> 'играет' | 'смотрит'
  Adj -> 'большой' | 'маленький' | 'маленькая' | 'большим' | 'компьютерным'
  PropN -> 'Вова' | 'Маша'
  Con -> 'и'
""")

#sent = ['маленький', 'мальчик', 'играет', 'в', 'компьютер', 'за', 'компьютерным', 'столом', 'и', 'смотрит', 'в', 'большой', 'экран']
sent = ['за', 'компьютерным', 'столом', 'играет', 'маленький', 'мальчик', 'и', 'смотрит', 'в', 'большой', 'экран']
parser = nltk.ChartParser(grammar)
trees = parser.parse(sent)

for tree in trees:
  print(tree)
tree.draw()
plt.show() #Keeps the window open to see the tree
