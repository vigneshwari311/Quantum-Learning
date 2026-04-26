from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

def deutsch_jozsa_balanced():

    qc = QuantumCircuit(2, 1)
    
    qc.x(1)
    qc.h(1)
    
    qc.h(0)
    qc.barrier()
    
    qc.cx(0, 1)
    qc.barrier()
    
    qc.h(0)
    
    qc.measure(0, 0)
    
    return qc

dj_circuit = deutsch_jozsa_balanced()
print("Deutsch-Jozsa Circuit (Balanced):")
print(dj_circuit.draw(output='text'))

backend = Aer.get_backend('qasm_simulator')
t_qc = transpile(dj_circuit, backend)
result = backend.run(t_qc).result()
counts = result.get_counts()

print(f"\nMeasured result: {counts}")
if '1' in counts:
    print("Function is BALANCED.")
else:
    print("Function is CONSTANT.")