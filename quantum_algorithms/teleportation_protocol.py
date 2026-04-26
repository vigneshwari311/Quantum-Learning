from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy as np
def create_teleportation_circuit():
    qr = QuantumRegister(3, name="q")
    crz = ClassicalRegister(1, name="crz")
    crx = ClassicalRegister(1, name="crx")
    qc = QuantumCircuit(qr, crz, crx)

    qc.ry(np.pi/4, 0)
    qc.barrier()

    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    qc.measure(0, 0)
    qc.measure(1, 1)
    qc.barrier()

    # Bob's corrections using modern if_test
    with qc.if_test((crx, 1)):
        qc.x(2)
    with qc.if_test((crz, 1)):
        qc.z(2)

    return qc

teleportation_circuit = create_teleportation_circuit()
print(teleportation_circuit.draw(output='text'))