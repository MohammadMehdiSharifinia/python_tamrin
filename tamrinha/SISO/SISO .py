import numpy as np
import matplotlib.pyplot as plt

class SistemaStateSpace:
    def __init__(self, A, B, C, D, dt=0.01):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.C = np.array(C, dtype=float)
        self.D = np.array(D, dtype=float)
        self.dt = dt  # time step Δt
        self._sabet_bandi_matrises()

    def _sabet_bandi_matrises(self):
        n, m = self.A.shape
        if n != m:
            raise ValueError("Matrise A bayad square bashe (n x n).")
        if self.B.shape != (n, 1):
            raise ValueError("Matrise B bayad n x 1 bashe ke n size-e A hast.")
        if self.C.shape != (1, n):
            raise ValueError("Matrise C bayad 1 x n bashe ke n size-e A hast.")
        if self.D.shape != (1, 1):
            raise ValueError("Matrise D bayad 1 x 1 bashe.")

    def shabihsazi(self, u_func, t_end=10.0):
        n = self.A.shape[0]
        tedad_khat = int(t_end / self.dt) + 1
        zaman = np.linspace(0, t_end, tedad_khat)
        vaziat = np.zeros((n, tedad_khat))
        khoruji = np.zeros(tedad_khat)

        for k in range(tedad_khat - 1):
            u_k = u_func(zaman[k])
            vaziat_dot = self.A @ vaziat[:, k] + self.B.flatten() * u_k
            vaziat[:, k + 1] = vaziat[:, k] + self.dt * vaziat_dot
            khoruji[k] = self.C @ vaziat[:, k] + self.D.flatten() * u_k

        u_last = u_func(zaman[-1])
        khoruji[-1] = self.C @ vaziat[:, -1] + self.D.flatten() * u_last
        return zaman, khoruji

    def rasm_pasokh(self, zaman, khoruji, title=""):
        plt.figure(figsize=(8, 5))
        plt.plot(zaman, khoruji, label="y(t)")
        plt.title(title)
        plt.xlabel("zaman (s)")
        plt.ylabel("khoruji")
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    try:
        # tarif-e matrise mesal
        A = [[0, 1, 0, 0],
             [-1, -1, 0, 1],
             [0, 0, 0, 1],
             [0, -1, -1, -1]]
        B = [[0], [1], [0], [1]]
        C = [[1, 0, 0, 0]]
        D = [[0]]

        sistema = SistemaStateSpace(A, B, C, D)

        def u(t):
            return 1.0  # vorudi step

        zaman, khoruji = sistema.shabihsazi(u, t_end=10.0)
        sistema.rasm_pasokh(zaman, khoruji, title="")

    except Exception as e:
        print("Eroor:", e)