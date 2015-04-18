from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Playback)

chrome = AppContext(executable='chrome')

grammar = Grammar("chrome", context=chrome)


rules = MappingRule(
    name = "chrome",
    mapping = {
      "find <text>" : Key("c-f") + Text("%(text)s"),
      "find next" : Key("c-g"),
      "find previous" : Key("cs-g"),
      "refresh" : Key("f5"),
      "hard refresh" : Key("c-f5"),
      "[go] back": Key("a-left"),
      "[go] forward": Key("a-right"),
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
