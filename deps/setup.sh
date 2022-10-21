#!/bin/bash
# TODO:chmod 755 setup.sh


echo "Install Dependencies"
#1. install pysmt (pip3)
pip3 install PySMT-0.9.5.tar.gz

#2. install z3 (pip3)
pip3 install z3_solver-4.8.15.0-py2.py3-none-manylinux1_x86_64.whl

#3. install boolector (pip3)
pip3 install PyBoolector-3.2.2.20221010.1-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl

#4. install cvc5 (copy)
cp cvc5-Linux /home/tacas23/

echo "All Dependencies Are Installed Successfully!"

#5. copy source code
echo "Copy wasim to New Path"
cp -rf /home/tacas23/tacas23-wasim/wasim /home/tacas23/

cd /home/tacas23/wasim/

mkdir output
mkdir log
cd log
mkdir log_demo
mkdir log_simulation
mkdir log_proof



