############# ARTIFACT LINK #############
github?

############# ADDITIONAL REQUIREMENTS #############
All the software dependencies are open-source and already downloaded in tacas23-wasim.zip, which could be installed automatically by the script tacas23-wasim/deps/setup.sh. 
The recommended minimum hardware requirements to run the artifact are listed as follows:
• CPU: Intel (64-bit and compatible with x86 ISA)
• Operating System: Ubuntu
• RAM: 16GB
• Storage: 128GB

############# EXPERIMENT RUNTIME #############
There are four sub-experiments in total, demonstrated in the abstract part of the artifact. The total runtime for these experiments is around 25 minutes, which is estimated on a server running Ubuntu 20.04 with a 2.9 GHz Intel Xeon(R) Platinum 8375C CPU and 128G RAM.
Runtime for each sub-experiments:
• Demo: several seconds
• Case study1: several seconds
• Case study2: 15 minutes
• Case study3: 10 minutes

############# REPRODUCIBILITY INSTRUCTIONS #############
========= Installation =========
1. Please first download the zip archive from the link we provided. (You should have completed this step)

2. Unzip the archive. Open a terminal and change directory into the folder which contains the zip archive. You can do this by first using the file explorer to navigate into the folder and right clicking in the blank space of the file explorer and select "Open in Terminal", after openning the terminal, run
    $ unzip -o -d tacas23-wasim tacas23-wasim.zip
4. Install dependencies for WASIM: in the terminal just opened in the previous step, run
    $ cd tacas23-wasim/deps
    $ chmod 755 setup.sh
    $ ./setup.sh

========= Reproduce Results of Case Studies =========
A unified script named run_script.py is used in all experiments. The usage of run_script could be inquired by the command: python3 run_script.py -h
1. Demo
    Directly run the python scripts, and the results could be seen in the terminal.
    $ cd $WASIMROOT/demo
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
            $ cd $WASIMROOT/user_interface
            $ python3 run_script.py -s simulation_simple_MAC_no_stall.py -l ../log/log_simulation/ -i 'none'
            $ cd $WASIMROOT/proof_construction
            $ python3 run_script.py -s prop_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none'
            $ python3 run_script.py -s inv_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none'
    
    2.2 Case study2: simple_pipe_stall
            $ cd $WASIMROOT/user_interface
            $ python3 run_script.py -s simulation_simple_MAC_stall.py -l ../log/log_simulation/ -i 'none'
            $ cd $WASIMROOT/proof_construction
            $ python3 run_script.py -s prop_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none'
            $ python3 run_script.py -s inv_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none'
    
    2.3 Case study3:3_stage_pipe (with four instructions)
            $ cd $WASIMROOT/user_interface
            $ python3 run_script.py -s simulation_3_stage_pipe.py -l ../log/log_simulation/ -i 'all'
            $ cd $WASIMROOT/proof_construction
            $ python3 run_script.py -s prop_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all'
            $ python3 run_script.py -s inv_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all'
            
            Note: the input parameter of run_script.py -i could be substituted by a single instruction type (e.g., 'add' or 'nand' or 'set' or 'nop') to perform single instruction simulation and verification. Note that all three parameters in the commands above should be replaced simultaneously.
            (e.g. for 'add' instruction:
            $ cd $WASIMROOT/user_interface
            $ python3 run_script.py -s simulation_3_stage_pipe.py -l ../log/log_simulation/ -i 'add'
            $ cd $WASIMROOT/proof_construction
            $ python3 run_script.py -s prop_check_3_stage_pipe.py -l ../log/log_proof/ -i 'add'
            $ python3 run_script.py -s inv_check_3_stage_pipe.py -l ../log/log_proof/ -i 'add'
            )
3. Output files and log files.
    • All of the output traces of states will be stored in ~/wasim/output in pickle format.
    • All running logs will be stored in ~/wasim/log, including log_demo, log_simulation and log_proof for demo, simulation and verification, respectively. And each log file will be named with the combination of the execution script and the instruction type.
