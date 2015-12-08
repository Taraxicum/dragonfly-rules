#Many of these mappings are adapted from the examples of others.  In particular
#  many of them are adapted from https://github.com/AshleyF/VimSpeak/blob/master/Main.fs

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Text, Function, Choice, Window, FocusWindow)
from vim_context import VimContext


insert = VimContext(mode='i')
normal = VimContext(mode='n')
visual = VimContext(mode='V')

insert_grammar = Grammar("vim", context=insert)
normal_grammar = Grammar("vim", context=normal)

surrounders = {
    "(paren | parenthesis)" : ")",
    "brace" : "}",
    "angle" : ">",
    "bracket" : "]",
    "quote" : "\"",
    "single quote" : "'"
    }

char_motions = {
    "til" : "t",
    "back-til" : "T",
    "find" : "f",
    "back-find" : "F"
    }

text_motions = {
    "search" : "/"
    }

bare_motions = {
    "left" : "h",
    "right" : "l",
    "up" : "k",
    "down" : "j",
    "word" : "w",
    "big-word" : "W",
    "back" : "b",
    "big-back" : "B",
    "end" : "e",
    "big-end" : "E",
    "start-of-line" : "^",
    "end-of-line" : "$",
    "zero" : "0", 
    "column" : "|",
    "match bracket" : "%",
    "next" : "n",
    "previous" : "N",
    "top screen line" : "M",
    "middle screen line" : "M",
    "bottom screen line" : "L",
    "(doc | document) line" : "G",
    "start [of] sentence" : "(",
    "end [of] sentence" : ")",
    "start [of] paragraph" : "{",
    "end [of] paragraph" : "}",
    "end [of] (document | file)" : "G",
    "start [of] (document | file)" : "gg"
    }

text_objects = {
    "quote" : '"',
    "single-quote" : "'",
    "(paren | parenthesis)" : "(",
    "angle [bracket]" : "<",
    "bracket" : "[",
    "brace" : "{",
    "paragraph" : "p",
    "sentence" : "s",
    "tag block" : "t",
    "word" : "w",
    "letter" : "l"
    }
text_operators = {
    "dell" : "d",
    "(yank | copy)" : "y",
    "change" : "c",
    }

bare_operators = {
    "paste" : "p",
    "back-paste" : "P",
    "join" : "J",
    "change case" : "~"
    }

modifiers = {
    "inner" : "i",
    "outer" : "a"
    }
numberMap = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "zero" : 0
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
    "zulu"     : "z",
    "equal"    : "="
    }

charMap = {}
charMap.update(letterMap)
charMap.update(numberMap)

insert_rules = MappingRule(
    name = "vim-insert",
    mapping = {
      "letter <c>"       : Key("%(c)s"),
      "text <text>"      : Text("%(text)s", pause=0),
      "upper letter <c>" : Key("s-%(c)s"),
      "normal [mode]"    : Key("escape"),
      "complete"         : Key("c-n")
    }, 
    extras = [
        Choice("c", charMap),
        Dictation("text")
        ]
    )

normal_rules = MappingRule(
    name = "vim-normal",
    mapping = {
      "letter <c>"                                              : Key("%(c)s"),
      "upper letter <c>"                                        : Key("s-%(c)s"),
      "normal [mode]"                                           : Key("escape"),
      "insert [mode]"                                           : Key("i"),
      "insert text <text>"                                      : Text("i%(text)s", pause=0)+Key("escape"),
      "visual [mode]"                                           : Key("v"),
      "visual line"                                             : Key("V"),
      "visual block"                                            : Key("c-Q"),
      "dell line"                                               : Text("dd"),
      "(after | append)"                                                  : Key("a"),
      "big (after | append)"                                              : Key("A"),
      "[<n>] undo"                                              : Key("%(n)d,u"),
      "[<n>] redo"                                              : Key("%(n)d,c-r"),
      "<bare_motion>" : Text("%(bare_motion)s"),
      "<n> <bare_motion>" : Text("%(n)d%(bare_motion)s"),
      "[<n>] <char_motion> <char>" : Text("%(n)d%(char_motion)s%(char)s"),
      "[<n>] <text_motion> <text>" : Text("%(n)d%(text_motion)s%(text)s", pause=0),
      "[<n>] <bare_operator>" : Text("%(n)d%(bare_operator)s"),
      "[<n>] <text_operator>[<n2>] [<modifier>]<text_object>" :
          Text("%(n)d%(text_operator)s%(n2)d%(modifier)s%(text_object)s"),
      "[<n>] <text_operator>[<n2>] <bare_motion>" :
          Text("%(n)d%(text_operator)s%(n2)d%(modifier)s%(bare_motion)s"),
      "[<n>] <text_operator> [<n>] <char_motion> <char>" :
          Text("%(n)d%(text_operator)s%(char_motion)s%(char)s"),
      "[<n>] <text_operator> [<n>] <text_motion> <text>" : 
          Text("%(n)d%(bare_operator)s%(char_motion)s%(text)s", pause=0),
      "surround [<n>] [<modifier>] [<text_object>] [<surrounder>]" :
          Text("ys%(n)d%(modifier)s%(text_object)s%(surrounder)s"),
      "surround [<n>] [<modifier>] [<bare_motion>] [<surrounder>]" :
          Text("ys%(n)d%(modifier)s%(bare_motion)s%(surrounder)s"),
      "explore"                                                 : Text(":E\n"),
      "close buffer"                                            : Text(":close\n"),
      "save file"                                               : Text(":w\n"),
      "record macro [<c>]"                                      : Text("q%(c)s"),
      "[<n>] run macro [<c>]"                                   : Text("%(n)d@%(c)s"),
      "end macro"                                               : Key("q"),
      "search-under-cursor"                                     : Text("*"),
      "search-under-cursor-reversed"                            : Text("#"),
      "again"                                                   : Text(";"),
      "again-reversed"                                          : Text(","),
      "start-of-next-section"                                   : Text("]]"),
      "start-of-previous-section"                               : Text("[["),
      "end-of-next-section"                                     : Text("]["),
      "end-of-previous-section"                                 : Text("[]"),
      "matching"                                                : Text("%"),
      "cursor-home"                                             : Text("H"),
      "cursor-middle"                                           : Text("M"),
      "cursor-last"                                             : Text("L"),
      "retrace-movements"                                       : Text("<C-o>"),
      "retrace-movements-forward"                               : Text("<C-i>"),
      "jump-to <c>"                                             : Text("`%(c)s"),
      "mark [letter] <c>"                                       : Text("m%(c)s"),
      "search-reversed"                                         : Text(","),
      },
      extras = [
          Integer("n", 1, 1000),
          Integer("n2", 1, 1000),
          Choice("c", letterMap),
          Choice("char", charMap), #TODO should not just be lettermap but all char options
          Choice("bare_operator", bare_operators),
          Choice("text_operator", text_operators),
          Choice("bare_motion", bare_motions),
          Choice("char_motion", char_motions),
          Choice("text_motion", text_motions),
          Choice("text_object", text_objects),
          Choice("modifier", modifiers),
          Choice("surrounder", surrounders),
          Dictation("text"),
          Dictation("m", format=False)
      ],
      defaults = {
          "n": 1,
          "n2": 1,
          "designator": "",
          "c": "",
          "char": "",
          "text_object": "",
          "modifier": "",
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
