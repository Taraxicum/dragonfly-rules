from dragonfly import (Grammar, AppContext, MappingRule, Function)
from vim_context import VimContext

normal_vim = VimContext(mode='n')
insert_vim = VimContext(mode='i')
visual_vim = VimContext(mode='V')

normal_grammar = Grammar("nvim", context=normal_vim)
insert_grammar = Grammar("ivim", context=insert_vim)
visual_grammar = Grammar("vvim", context=visual_vim)

def normal():
  print "Normal Mode"

def insert():
  print "Insert Mode"

def visual():
  print "Visual Mode"

n_rules = MappingRule(
    name="normal_vim",
    mapping = { "happy": Function(normal) }
    )

i_rules = MappingRule(
    name="insert_vim",
    mapping = { "happy": Function(insert) }
    )

v_rules = MappingRule(
    name="visual_vim",
    mapping = { "happy": Function(visual) }
    )

normal_grammar.add_rule(n_rules)
normal_grammar.load()
insert_grammar.add_rule(i_rules)
insert_grammar.load()
visual_grammar.add_rule(v_rules)
visual_grammar.load()

def unload():
  global normal_grammar, insert_grammar, visual_grammar
  if normal_grammar: normal_grammar.unload()
  if insert_grammar: insert_grammar.unload()
  if visual_grammar: visual_grammar.unload()
  normal_grammar = None
  insert_grammar = None
  visual_grammar = None
  
