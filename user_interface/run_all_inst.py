import sys, getopt, re, os

def main(argv):
   script = ''
   logdir = ''
   try:
      opts, args = getopt.getopt(argv,"hs:l:",["script=","logdir="])
   except getopt.GetoptError:
      ('run_all_inst.py  -s <script> -l <logpath>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('run_all_inst.py -s <script> -l <logdir>')
         sys.exit()
    #   elif opt in ("-i", "--inst"):
    #      inst = arg
      elif opt in ("-s", "--script"):
         script = arg
      elif opt in ("-l", "--logdir"):
         logdir = arg
#    print('input file: ', inst)
   print('script name:   ', script)
   print('log file:', logdir)

   inst_list = ['add', 'nand', 'set', 'nop']
   temp_script = 'temp_'+str(script)
   for inst in inst_list:
        ## regular expression to replace the script
        f_t = open(str(script), 'r')
        f = open(str(temp_script), 'w')
        lines = f_t.readlines()
        for line in lines:
                if('_inst.' in str(line)):
                    line_new = re.sub(r'_inst.', '_'+str(inst)+'.', line)
                else:
                    line_new = line
                f.writelines(line_new)
        f_t.close()
        f.close()

        os.system('python {s} > {l}_{i}.txt'.format(s=temp_script, l=logdir, i=inst))
        os.remove(temp_script)
        
if __name__ == "__main__":
   main(sys.argv[1:])
