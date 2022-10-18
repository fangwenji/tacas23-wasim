import sys
sys.path.append('/data/wenjifang/WASIM')
sys.path.append('/data/wenjifang/WASIM/symsim_framework')

from pathlib import Path
from symsim_framework.symtraverse import *

btor_parser = BTOR2Parser()
sts, _ = btor_parser.parse_file(Path("/data/wenjifang/WASIM/design/testcase1_2-simple_MAC_no_stall/test.btor2"))
executor = SymbolicExecutor(sts)

executor.init(
  executor.convert({
    'wen_stage1':'v1',
    'wen_stage2':'v2',
    'wen_stage3':'v3',
    'stage1':'a',
    'stage2':'b',
    'stage3':'c'
  }))

executor.print_current_step() 
executor.print_current_step_assumptions()

executor.set_input(
    executor.convert({'rst':0}), [])
executor.sim_one_step()

state = executor.get_curr_state()
state.print()
state = executor.set_curr_state()

