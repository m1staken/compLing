import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP | NP VP VP | NP VP Con VP | VP NP Con VP
  NP -> Det Nom | PropN | Adj Nom | N
  Nom -> Adj Nom | N | AP Nom
  PP -> Det Nom | Det Adj Nom  
  AP -> Adv Adj 
  VP -> V PP | V Nom | V | V PP PP | PP V
  Det -> 'с' | 'в' | 'за' | 'на'
  N -> 'мальчик' | 'пёс' | 'мячом' | 'компьютер' | 'экран' | 'столом' | 'код' | 'Python'
  V -> 'играет' | 'смотрит' | 'программирует' 
  Adj -> 'большой' | 'маленький' | 'маленькая' | 'большим' | 'компьютерным'
  PropN -> 'Вова' | 'Маша' | 'Ралиф' | 'Дамир'
  Adv -> 'очень' | 'быстро'
  Con -> 'и'
""")

sent = ['Ралиф', 'программирует']
sent2 = ['Вова', 'играет', 'в', 'компьютер', 'за', 'компьютерным', 'столом', 'и', 'смотрит', 'в', 'большой', 'экран']
sent3 = [ 'маленький', 'мальчик', 'играет', 'за', 'очень', 'большим', 'компьютерным', 'столом']
parser = nltk.ChartParser(grammar)
trees = parser.parse(sent3)

for tree in trees:
    print(tree)
tree.draw()
plt.show() #Keeps the window open to see the tree
