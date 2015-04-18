#Many of these mappings are adapted from the examples of others.  In particular
#  many of them are adapted from https://github.com/AshleyF/VimSpeak/blob/master/Main.fs


from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Text, Mimic, Function, Choice, Window, FocusWindow)
vi = AppContext(title='vi')
gvim = AppContext(executable='gvim') #, title='command')
  #One thought I have is setting the title in vim based on what mode it is in, then having different grammars for different modes.  Not sure if that will be useful enough to hassle with yet, so for now just going to try treating it all as the same dragon mode.
grammar = Grammar("vim", context=(gvim | vi))

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")
noCaps = Mimic("\\no-caps")

def lower_case(text):
  print str(text).lower()
  Text(str(text).lower()).execute()

letterMap = {
    "alpha": "a",
    "bravo": "b",
    "charlie": "c",
    "delta": "d",
    "echo": "e",
    "foxtrot": "f",
    "golf": "g",
    "hotel": "h",
    "india": "i",
    "juliett": "j",
    "kilo": "k",
    "lima": "l",
    "mike": "m",
    "november": "n",
    "oscar": "o",
    "papa": "p",
    "quebec": "q",
    "romeo": "r",
    "sierra": "s",
    "tango": "t",
    "uniform": "u",
    "victor": "v",
    "whiskey": "w",
    "x-ray": "x",
    "yankee": "y",
    "zulu": "z"
    }

rules = MappingRule(
    name = "vim",
    mapping = {
      "test call <text>": Function(lower_case),
      "normal mode"  : Key("escape"),
      "insert mode"  : Key("i"),
      "letter <c>" : Key("%(c)s"),
      "append"  : Key("a"),
      "big append" : Key("A"),
      "undo" : Key("u"),
      "[<n>] delete letter" : Text("%(n)dx"),
      "yank" : Key("y"),
      "delete" : Key("d"),
      "explore"      : Text(":E\n"),
      "close buffer" : Text(":close\n"),
      "save file"    : Text(":w\n"),
      "[<n>] back"                         : Text("%(n)db"),
      "[<n>] back-word"                    : Text("%(n)db"),
      "[<n>] big-back"                     : Text("%(n)dB"),
      "[<n>] big-back-word"                : Text("%(n)dB"),
      "record macro [<c>]" : Text("q%(c)s"),
      "[<n>] run macro [<c>]" : Text("%(n)d@%(c)s"),
      "end macro": Key("q"),
      "[<n>] end"                          : Text("%(n)de"),
      "[<n>] big-end"                      : Text("%(n)dE"),
      "[<n>] back-end"                     : Text("%(n)dge"),
      "[<n>] back-big-end"                 : Text("%(n)dgE"),
      "[<n>] left"                         : Text("%(n)dh"),
      "[<n>] down"                         : Text("%(n)dj"),
      "[<n>] up"                           : Text("%(n)dk"),
      "[<n>] right"                        : Text("%(n)dl"),
      "next"                         : Text("n"),
      "next-reversed"                : Text("N"),
      "previous"                     : Text("N"),
      "column-zero"                  : Key("0"),
      "column"                       : Text("|"),
      "start-of-line"                : Text("^"),
      "end-of-line"                  : Text("$"),
      "search-under-cursor"          : Text("*"),
      "search-under-cursor-reversed" : Text("#"),
      "again"                        : Text(";"),
      "again-reversed"               : Text(","),
      "down-sentence"                : Text(")"),
      "up-sentence"                  : Text("("),
      "down-paragraph"               : Text("}"),
      "up-paragraph"                 : Text("{"),
      "start-of-next-section"        : Text("]]"),
      "start-of-previous-section"    : Text("[["),
      "end-of-next-section"          : Text("]["),
      "end-of-previous-section"      : Text("[]"),
      "matching"                     : Text("%"),
      "down-line"                    : Text("+"),
      "up-line"                      : Text("-"),
      "first-character"              : Text("_"),
      "cursor-home"                  : Text("H"),
      "cursor-middle"                : Text("M"),
      "cursor-last"                  : Text("L"),
      "start-of-document"            : Text("gg"),
      "end-of-document"              : Text("G"),
      "retrace-movements"            : Text("<C-o>"),
      "retrace-movements-forward"    : Text("<C-i>"),
      "jump-to-mark"                 : Text("'"),
      "find"                         : Text("f"),
      "find-reversed"                : Text("F"),
      "till"                         : Text("t"),
      "till-reversed"                : Text("T"),
      "search"                       : Text("/"),
      "search-reversed"              : Text(","),
      "word"                         : Text(","),
      "big-word"                     : Text(",")
      },
      extras = [
          Integer("n", 1, 1000),
          Choice("c", letterMap),
          Dictation("text"),
          Dictation("m", format=False)
      ],
      defaults = {
          "n": 1,
          "c": "",
          "m": "@"
      }
     
    )

grammar.add_rule(rules)
grammar.load()                                      # Load the grammar.

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
