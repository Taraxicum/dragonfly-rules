#Many of these mappings are adapted from the examples of others.  In particular
#  many of them are adapted from https://github.com/AshleyF/VimSpeak/blob/master/Main.fs

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Text, Function, Choice, Window, FocusWindow)
from vim_context import VimContext


insert = VimContext(mode='i')
normal = VimContext(mode='n')
visual = VimContext(mode='V')

insert_grammar = Grammar("vim", context=insert)
normal_grammar = Grammar("vim", context=normal)

surroundTypeMap = {
    "(paren | parenthesis)" : ")",
    "brace"                 : "}",
    "bracket"               : "]",
    "angle"                 : ">",
    "quote"                 : "\"",
    "single quote"          : "'"
    }

targetMap = {
    "(word | words)"       : "w",
    "letter"               : "l",
    "(paren | parenthesis)" : ")",
    "brace"                 : "}",
    "bracket"               : "]",
    "angle"                 : ">",
    "quote"                 : "\"",
    "single quote"          : "'",
    "line"                  : "s"
    }
designatorMap = {
    "inner" : "i",
    "outer" : "a"
    }

letterMap = {
    "alpha"    : "a",
    "bravo"    : "b",
    "charlie"  : "c",
    "delta"    : "d",
    "echo"     : "e",
    "foxtrot"  : "f",
    "golf"     : "g",
    "hotel"    : "h",
    "india"    : "i",
    "juliett"  : "j",
    "kilo"     : "k",
    "lima"     : "l",
    "mike"     : "m",
    "november" : "n",
    "oscar"    : "o",
    "papa"     : "p",
    "quebec"   : "q",
    "romeo"    : "r",
    "sierra"   : "s",
    "tango"    : "t",
    "uniform"  : "u",
    "victor"   : "v",
    "whiskey"  : "w",
    "x-ray"    : "x",
    "yankee"   : "y",
    "zulu"     : "z"
    }


insert_rules = MappingRule(
    name = "vim-insert",
    mapping = {
      "letter <c>"       : Key("%(c)s"),
      "upper letter <c>" : Key("s-%(c)s"),
      "normal [mode]"    : Key("escape"),
      "complete"         : Key("c-n")
    }, 
    extras = [
        Choice("c", letterMap)
        ]
    )

normal_rules = MappingRule(
    name = "vim-normal",
    mapping = {
      "letter <c>"                                              : Key("%(c)s"),
      "upper letter <c>"                                        : Key("s-%(c)s"),
      "normal [mode]"                                           : Key("escape"),
      "insert [mode]"                                           : Key("i"),
      "visual [mode]"                                           : Key("v"),
      "visual line"                                             : Key("V"),
      "visual block"                                            : Key("V"),
      "append"                                                  : Key("a"),
      "big append"                                              : Key("A"),
      "undo"                                                    : Key("u"),
      "[<n>] delete letter"                                     : Text("%(n)dx"),
      "yank [<n>] [<designator>] [<target>]"                    : Text("y%(n)d%(designator)s%(target)s"),
      "change [<n>] [<designator>] [<target>]"                  : Text("c%(n)d%(designator)s%(target)s"),
      "delete [<n>] [<designator>] [<target>]"                  : Text("d%(n)d%(designator)s%(target)s"),
      "explore"                                                 : Text(":E\n"),
      "close buffer"                                            : Text(":close\n"),
      "save file"                                               : Text(":w\n"),
      "surround [<n>] [<designator>] [<target>] [<surrounder>]" : Text("ys%(n)d%(designator)s%(target)s%(surrounder)s"),
      "[<n>] back"                                              : Text("%(n)db"),
      "[<n>] back-word"                                         : Text("%(n)db"),
      "[<n>] big-back"                                          : Text("%(n)dB"),
      "[<n>] big-back-word"                                     : Text("%(n)dB"),
      "record macro [<c>]"                                      : Text("q%(c)s"),
      "[<n>] run macro [<c>]"                                   : Text("%(n)d@%(c)s"),
      "end macro"                                               : Key("q"),
      "[<n>] end"                                               : Text("%(n)de"),
      "[<n>] big-end"                                           : Text("%(n)dE"),
      "[<n>] back-end"                                          : Text("%(n)dge"),
      "[<n>] back-big-end"                                      : Text("%(n)dgE"),
      "[<n>] left"                                              : Text("%(n)dh"),
      "[<n>] down"                                              : Text("%(n)dj"),
      "[<n>] up"                                                : Text("%(n)dk"),
      "[<n>] right"                                             : Text("%(n)dl"),
      "next"                                                    : Text("n"),
      "next-reversed"                                           : Text("N"),
      "previous"                                                : Text("N"),
      "column-zero"                                             : Key("0"),
      "column"                                                  : Text("|"),
      "start-of-line"                                           : Text("^"),
      "end-of-line"                                             : Text("$"),
      "search-under-cursor"                                     : Text("*"),
      "search-under-cursor-reversed"                            : Text("#"),
      "again"                                                   : Text(";"),
      "again-reversed"                                          : Text(","),
      "down-sentence"                                           : Text(")"),
      "up-sentence"                                             : Text("("),
      "down-paragraph"                                          : Text("}"),
      "up-paragraph"                                            : Text("{"),
      "start-of-next-section"                                   : Text("]]"),
      "start-of-previous-section"                               : Text("[["),
      "end-of-next-section"                                     : Text("]["),
      "end-of-previous-section"                                 : Text("[]"),
      "matching"                                                : Text("%"),
      "down-line"                                               : Text("+"),
      "up-line"                                                 : Text("-"),
      "first-character"                                         : Text("_"),
      "cursor-home"                                             : Text("H"),
      "cursor-middle"                                           : Text("M"),
      "cursor-last"                                             : Text("L"),
      "start-of-document"                                       : Text("gg"),
      "end-of-document"                                         : Text("G"),
      "retrace-movements"                                       : Text("<C-o>"),
      "retrace-movements-forward"                               : Text("<C-i>"),
      "jump-to-mark"                                            : Text("'"),
      "mark [letter] <c>"                                       : Text("%(m)s%(c)s"),
      "find"                                                    : Text("f"),
      "find-reversed"                                           : Text("F"),
      "till"                                                    : Text("t"),
      "till-reversed"                                           : Text("T"),
      "search [<text>]"                                         : Text("/%(text)s"),
      "search-reversed"                                         : Text(","),
      "word"                                                    : Text(","),
      "big-word"                                                : Text(",")
      },
      extras = [
          Integer("n", 1, 1000),
          Choice("c", letterMap),
          Choice("target", targetMap),
          Choice("designator", designatorMap),
          Choice("surrounder", surroundTypeMap),
          Dictation("text"),
          Dictation("m", format=False)
      ],
      defaults = {
          "n": 1,
          "designator": "",
          "c": "",
          "m": "@"
      })


insert_grammar.add_rule(insert_rules)
normal_grammar.add_rule(normal_rules)
insert_grammar.load()                                      # Load the grammar.
normal_grammar.load()                                      # Load the grammar.

def unload():
  global insert_grammar, normal_grammar
  if insert_grammar: insert_grammar.unload()
  if normal_grammar: normal_grammar.unload()
  normal_grammar = None
  insert_grammar = None
