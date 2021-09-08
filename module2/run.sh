pip3 install tqdm
python3 generate.py 10000000
echo "Proccess\n"
python3 benchmark_proccess.py 10
echo "Thread\n"
python3 benchmark_thread.py 10