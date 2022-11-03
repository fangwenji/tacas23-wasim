############# ARTIFACT LINK #############
Zenodo link: 
Please download the zip archive through this link.

############# ADDITIONAL REQUIREMENTS #############
All the software dependencies are open-source and already downloaded in tacas23-wasim.zip, which could be installed automatically by the script tacas23-wasim/deps/setup.sh. 
The recommended minimum hardware requirements to run the artifact are listed as follows:
• CPU: Intel (64-bit x86 ISA, frequncy >= 2.40GHz) 
• Operating System: Ubuntu
• RAM: 16GB
• Storage: 128GB

############# EXPERIMENT RUNTIME #############
There are five sub-experiments in total, demonstrated in the abstract part of the artifact. The total runtime for these experiments is around 25 minutes, which is estimated on a server running Ubuntu 20.04 with a 2.9 GHz Intel Xeon(R) Platinum 8375C CPU and 128G RAM.
Runtime for each sub-experiments:
• Demo: several seconds
• Case study1: several seconds
• Case study2: 15 minutes
• Case study3: 10 minutes
• Berkeley-abc experiments: please terminate the process manually
Note: 

############# REPRODUCIBILITY INSTRUCTIONS #############
========= Installation =========
1. Please first download the zip archive from the link we provided. (You should have completed this step)
2. Unzip the archive. Open a terminal and change directory into the folder which contains the zip archive. You can do this by first using the file explorer to navigate into the folder and right clicking in the blank space of the file explorer and select "Open in Terminal", after openning the terminal, run
    $ unzip -o -d tacas23-wasim tacas23-wasim.zip
3. Install dependencies for WASIM: in the terminal just opened in the previous step, run
    $ cd tacas23-wasim/deps
    $ chmod 755 setup.sh
    $ ./setup.sh

========= Reproduce Results of Case Studies =========
A unified script named run_script.py is used in all experiments. The usage of run_script could be inquired by the command: python3 run_script.py -h
After running the commonds of part 2 (case studies), the results Table 1 will be fully reproduces, which might be slightly different due to distinct experimental environments.
1. Demo
    Directly run the python scripts, and the results could be seen in the terminal.
    These will reproduce all the screenshots in Appendix. 
    $ cd ~/wasim/demo
    $ python3 run_script.py -s api.py -l ../log/log_demo/ -i 'none'
    $ python3 run_script.py -s abs.py -l ../log/log_demo/ -i 'none'
    $ python3 run_script.py -s fpv.py -l ../log/log_demo/ -i 'none'
    $ python3 run_script.py -s inv.py -l ../log/log_demo/ -i 'none'
2. Case Studies
    The execution processes are similar for the following three case studies, including 
        • simulation in user_interface/ to obtain the traces of abstract states stored in output/ with pickle format
        • formal property check in proof_construction/
        • invariant check  in proof_construction/
    
    2.1 Case study1: simple_pipe_no_stall
            $ cd ~/wasim/user_interface
            $ python3 run_script.py -s simulation_simple_MAC_no_stall.py -l ../log/log_simulation/ -i 'none'
            $ cd ~/wasim/proof_construction
            $ python3 run_script.py -s prop_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none' -v fpv
            $ python3 run_script.py -s inv_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none' -v inv
    
    2.2 Case study2: simple_pipe_stall
            $ cd ~/wasim/user_interface
            $ python3 run_script.py -s simulation_simple_MAC_stall.py -l ../log/log_simulation/ -i 'none'
            $ cd ~/wasim/proof_construction
            $ python3 run_script.py -s prop_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none' -v fpv
            $ python3 run_script.py -s inv_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none' -v inv
    
    2.3 Case study3:3_stage_pipe (with four instructions)
            $ cd ~/wasim/user_interface
            $ python3 run_script.py -s simulation_3_stage_pipe.py -l ../log/log_simulation/ -i 'all'
            $ cd ~/wasim/proof_construction
            $ python3 run_script.py -s prop_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all' -v fpv
            $ python3 run_script.py -s inv_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all' -v inv
    2.4 Experimental results statistics
            $ cd ~/wasim
            $ python3 statistc.py
        After this step, all the experimental results will be written into the ~/wasim/statistics.log, corresponding to the Table 1 in the paper.
    
3. Output files and log files.
    • All of the output traces of states will be stored in ~/wasim/output in pickle format.
    • All running logs will be stored in ~/wasim/log, including log_demo, log_simulation and log_proof for demo, simulation and verification, respectively. And each log file will be named with the combination of the execution script and the instruction type.

4. Helper functions for the useful APIs of WASIM are avaliable. You can check the manual through the command help(object) in Python.
    Here is an example of the helper function:
    $ cd ~/wasim/symsim_framework
    $ python3 
    $ import symsim
    $ help(symsim)
    Then the usage of symbolic simulator will be demonstrated on the terminal, including classes with attributes and functions with arguments. 
    If you want to exit the helper function, you can press the key 'q', and input the quit() command in Python.

5. Reproduce Berkeley-abc experiments
    Please note here, Berkeley-abc is not our tool. We include experiments using Berkeley-abc in this artifact just as a comparison to our tool. This is to show our tool is advantageous on certain problems that are typically hard for a hardware model checker.
    $ cd ~/abc/script
    $ ~/oss-cad-suite/bin/yosys-abc
    $ source abc-script.ys
    Note: all the experiments are integrated in the one script 'abc-script.ys', the Berkeley-abc execution will not terminate for at least 72 hours, so please terminate the process by Ctrl+C manually if you want to exit.

    
