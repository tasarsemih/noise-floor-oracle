"""
Demo: Noise Floor Visualization for IBM-style Backend
"""

from quantum_backends.ibm_runtime import IBMNoiseFloorOracle
import matplotlib.pyplot as plt


def run_demo():
    backend = "ibm_fake_backend"
    oracle = IBMNoiseFloorOracle(backend)

    circuit_depths = [1, 2, 4, 8, 16, 32, 64, 128]
    error_rates = oracle.run(circuit_depths)

    # Plot
    plt.figure()
    plt.plot(circuit_depths, error_rates, marker='o')
    plt.xscale("log", base=2)
    plt.xlabel("Circuit Depth (log2 scale)")
    plt.ylabel("Error Rate")
    plt.title("Noise Floor Saturation on Quantum Backend")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    run_demo()
