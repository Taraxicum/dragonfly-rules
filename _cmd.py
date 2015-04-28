from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Playback)

command = AppContext(executable='cmd')

grammar = Grammar("command", context=command)


rules = MappingRule(
    name = "command",
    mapping = {
      "go to natlink": Text("d:\ncd \\Natlink\\Natlink\\MacroSystem\n")
      },
    extras = [
      Dictation("text", format=False)
      ],
    defaults = {
      "text" : ""
      }
    )

grammar.add_rule(rules)
grammar.load()                                      # Load the grammar.

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
