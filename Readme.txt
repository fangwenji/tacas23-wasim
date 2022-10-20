ARTIFACT LINK:
github?

ADDITIONAL REQUIREMENTS:
All the software dependencies are open-source, and already downloaded in tacas23-wasim.zip, which could be installed automatically by the script tacas23-wasim/deps/setup.sh. 
The recommoned minimum hardware requirements to run the artifact are listed as follows:
• CPU: Intel (64-bit and compatible with x86 ISA)
• Operating System: Ubuntu
• RAM: 16GB
• Storage: 128GB

EXPERIMENT RUNTIME:
There are four sub-experiments in total, demonstrated in abstract part of the artifact. The total runtime for these experiments is around 20 minutes, which is estimated on a server running Ubuntu 20.04 with a 2.9 GHz Intel Xeon(R) Platinum 8375C CPU and 128G RAM.

REPRODUCIBILITY INSTRUCTIONS:
1. Downloed the atifact data file tacas23-wasim.zip and copy it to the tacas23 virtual machine.
2. Unzip the tacas23-wasim.zip file in new directory.
    $ unzip -o -d /home/tacas23 tacas23-wasim.zip
3. Setup dependencies for WASIM. (After running the following commands, the source code of WASIM will be copied into /home/tacas23/wasim)
    $ cd /home/tacas23/tacas23-wasim/deps
    $ chmod 755 setup.sh
    $ ./setup.sh
    $ cd /home/tacas23/
    $ chmod -R 755 wasim
4. Run the experiments.
    4.1 Demo
        Directly run the python scripts and the results could be seen in the terminal.
        $ cd /home/tacas23/wasim/demo
        $ python3 api.py
        $ python3 abs.py
        $ python3 fpv.py
        $ python3 inv.py
    4.2 Case Studies
        The execution processes are similar for the following three case studies, including 
            • simulation in user_interface/ to obtain the traces of abstract states stored in output/ with pickle format
            • formal property check in proof_construction/
            • invariant check  in proof_construction/
        And the log files with running details, results and runtime are stored in log/log_simulation and log/log_proof 
        A unified script named run_script.py is used in all three case studies. The usage of run_script could be inquired by:
        $ python3 run_script.py -h
        After running the run_script.py, the log storage directory will be shown in the terminal.
        4.2.1 Case study1: simple_pipe_no_stall
              $ cd /home/tacas23/wasim/user_interface
              $ python3 run_script.py -s simulation_simple_MAC_no_stall.py -l ../log/log_simulation/ -i 'none'
              $ cd /home/tacas23/wasim/proof_construction
              $ python3 run_script.py -s prop_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none'
              $ python3 run_script.py -s inv_check_simple_MAC_no_stall.py -l ../log/log_proof/ -i 'none'
        4.2.2 Case study2: simple_pipe_stall
              $ cd /home/tacas23/wasim/user_interface
              $ python3 run_script.py -s simulation_simple_MAC_stall.py -l ../log/log_simulation/ -i 'none'
              $ cd /home/tacas23/wasim/proof_construction
              $ python3 run_script.py -s prop_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none'
              $ python3 run_script.py -s inv_check_simple_MAC_stall.py -l ../log/log_proof/ -i 'none'
        4.2.3 Case study3: 3_stage_pipe (with four instructions)
              $ cd /home/tacas23/wasim/user_interface
              $ python3 run_script.py -s simulation_3_stage_pipe.py -l ../log/log_simulation/ -i 'all'
              $ cd /home/tacas23/wasim/proof_construction
              $ python3 run_script.py -s prop_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all'
              $ python3 run_script.py -s inv_check_3_stage_pipe.py -l ../log/log_proof/ -i 'all'
              
              Note: the input parameter of run_script.py -i could be subsituted by single instrcution type (e.g. 'add' or 'nand' or 'set' or 'nop') to perform single instruction simulation and verification. Note that all three parameters in the commands above should be replaced simutanously.
 
