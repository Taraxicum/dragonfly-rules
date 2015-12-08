#Many of these mappings are adapted from the examples of others.  In particular
#  many of them are adapted from https://github.com/AshleyF/VimSpeak/blob/master/Main.fs

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Text, Function, Choice, Window, FocusWindow)


python = AppContext(title=".py", executable='gvim')

python_grammar = Grammar("python", context=python)

python_rules = MappingRule(
    name = "python",
    mapping = {
        "function <text>" : Text("def %(text)s():\n", pause=0)
      },
      extras = [
          Integer("n", 1, 1000),
          Dictation("text"),
      ],
      defaults = {
          "n": 1
      })


python_grammar.add_rule(python_rules)
python_grammar.load()                                      # Load the grammar.

def unload():
  global python_grammar
  if python_grammar: python_grammar.unload()
  python_grammar = None
