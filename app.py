import fire
from pkg.langchain import Wrangle

def search(name):
  # Openai_gpt2()
  # print(name)s
  return 'Hello world here will be ai {name}!'.format(name=name)

if __name__ == '__main__':
  # fire.Fire(Wrangle).Fire(search)
  fire.Fire(search)




