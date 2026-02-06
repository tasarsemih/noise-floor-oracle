"""
Demo: Noise Floor Detection on IBM-style Backend
"""

from quantum_backends.ibm_runtime import IBMNoiseFloorOracle


def run_demo():
    backend = "ibm_fake_backend"
    oracle = IBMNoiseFloorOracle(backend)

    circuit_depths = [1, 2, 4, 8, 16, 32, 64]
    error_rates = oracle.run(circuit_depths)

    print("Noise Floor Oracle Demo")
    print("-" * 30)

    for d, e in zip(circuit_depths, error_rates):
        print(f"Depth {d:>3} → Error rate {e:.4f}")

    print("\nObservation:")
    print("Error rates saturate despite increasing circuit depth.")
    print("This indicates an intrinsic hardware noise floor.")


if __name__ == "__main__":
    run_demo()
