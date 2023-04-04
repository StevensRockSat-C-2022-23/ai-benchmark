from ai_benchmark import AIBenchmark
import psutil, os

def main():
    p = psutil.Process(os.getpid())
    p.nice(-15) # Set this process to a higher priority. Could help us with GPU Memory issues
    
    aib = AIBenchmark(verbose_level=2)
    #results = aib.run_micro() # Inference and Micro take 2GB of RAM while Training takes 4GB
    results = aib.run_nano()

if __name__ == "__main__":
    # execute only if run as a script
    main()
