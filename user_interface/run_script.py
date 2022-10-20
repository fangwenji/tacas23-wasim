import sys, getopt, re, os

def main(argv):
   script = ''
   logdir = ''
   try:
      opts, args = getopt.getopt(argv,"hs:l:i:",["script=","logdir=","inst="])
   except getopt.GetoptError:
      ('run_script.py  -s <script> -l <logpath> -i <inst_type>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('run_script.py -s <script> -l <logdir> -i <inst_type>')
         print('  -s<script>: to assign which user input script is going to be used')
         print('  -l<logdir>: to designate the directory that stores the running log files')
         print('  -i<inst_type>: to choose which type of instrcution will be verified.')
         sys.exit()
    #   elif opt in ("-i", "--inst"):
    #      inst = arg
      elif opt in ("-s", "--script"):
         script = arg
      elif opt in ("-l", "--logdir"):
         logdir = arg
      elif opt in ("-i", "--inst"):
         inst_type = arg
   print('Script name:   ', script)
   print('Log path:', logdir)
   print('Instruction type:', inst_type)
   print('\n')
   assert inst_type in ['all', 'add', 'nand', 'nop', 'set', 'none']
   if inst_type == 'all':
      inst_list = ['add', 'nand', 'set', 'nop']
   else:
      inst_list = [str(inst_type)]

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
        print('Running script:', script)
        if(len(inst_list) > 1):
           print('Current instruction:', inst)
        if(logdir == 'terminal'):
           os.system('python3 {s}'.format(s=temp_script))
        else:
           print('Log is stored in path: {l}{s1}_{i}.log'.format(s1=script, l=logdir, i=inst))
           os.system('python3 {s} > {l}{s1}_{i}.log'.format(s=temp_script, l=logdir, i=inst, s1=script))
        os.remove(temp_script)
        print('Finish!\n\n')
        
        
        
if __name__ == "__main__":
   main(sys.argv[1:])
