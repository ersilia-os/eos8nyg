"""Pin numpy's OpenBLAS kernel, so every machine returns the same hits.

OpenBLAS picks a kernel to suit each CPU, and kernels round in a different order.
The differences are tiny, but neighbours in the library are often closer than that,
so on another CPU near-tied hits swap places and the output changes. Haswell (AVX2
and FMA) is fast and present on nearly every x86-64 CPU, so it is pinned wherever
the CPU has it. Elsewhere OpenBLAS keeps its own choice, rather than crash.

Import this before anything that imports numpy: OpenBLAS reads the setting once,
when it loads.
"""

import os
import platform


def _has_avx2_and_fma():
    if platform.machine() not in ("x86_64", "AMD64"):
        return False
    try:
        with open("/proc/cpuinfo") as fh:
            for line in fh:
                if line.startswith("flags"):
                    return {"avx2", "fma"} <= set(line.split(":", 1)[1].split())
    except OSError:
        pass
    return False


if _has_avx2_and_fma():
    os.environ.setdefault("OPENBLAS_CORETYPE", "Haswell")
