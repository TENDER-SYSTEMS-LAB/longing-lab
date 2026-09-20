"""LONGING RESEARCH — the rest of the promotion gate battery, on the generated world.

The first script ran one gate (held-out reduction of Unexplained). This one
runs the others the fourth round named, each calibrated on a planted null where
a threshold is needed:

  A. support      — the candidate loads on at least two markets and two practices
  B. bulk         — variance along the candidate clears the idiosyncratic bulk
  C. stability    — loading signs fit on one half of the window hold on the other
  D. placebo      — the declared schedule's explanatory power vanishes when the
                    arrival-date market labels are permuted
  E. monitor      — after a line is admitted, Unexplained's cross-sectional
                    covariance moves toward diagonal (a true line) or does not (a null)

numpy only, plus the harness. `python3 this.py <harness.py>`.
Nothing here selects a factor set. Every coefficient upstream is a placeholder.
"""
import importlib.util, itertools, math, random, sys
import numpy as np

HARNESS = sys.argv[1] if len(sys.argv) > 1 else "raw/documents/2026-09-20-loop-simulation-harness-v4.py"
spec = importlib.util.spec_from_file_location("sim", HARNESS)
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)
nM, nP, T = len(sim.MARKETS), len(sim.UNIVERSE), sim.WEEKS
EARLY, LATE = (60, 460), (T - 400, T - 1)


def true_loadings(seed, k):
    rng = random.Random(seed)
    return np.array([[rng.gauss(0, 1) for _ in range(k)] for _ in range(nP)])


def panel(p, seed):
    H = sim.run(p, seed)
    P = np.array([[H["P"][m][i] for i in range(nP)] for m in range(nM)])
    r = np.diff(np.log(P), axis=2).transpose(2, 0, 1)
    dU = np.diff(np.log(np.array(H["U"])))
    dsub = np.diff(np.array(H["sub"]), axis=1).T
    arr = np.array([[sim.wave_state(t, m, p)[0] for m in range(nM)] for t in range(1, T)])
    return r + dU[:, None, None], dsub, arr


def strip_schedule(r1, dsub, arr, market_map=None, block=1):
    """market_map[m] = which market's schedule to use for market m (placebo).
    block > 1 sums returns and schedule increments over blocks of that many
    weeks before regressing, so a slow drift is measured against slow noise."""
    mm = market_map or list(range(nM))
    if block > 1:
        n = (len(r1) // block) * block
        r1 = r1[:n].reshape(-1, block, nM, nP).sum(1)
        dsub = dsub[:n].reshape(-1, block, nM).sum(1); arr = arr[:n].reshape(-1, block, nM).sum(1)
    r2 = np.empty_like(r1); ss = 0.0; st = 0.0
    for m in range(nM):
        X = np.column_stack([np.ones(len(r1)), arr[:, mm[m]], dsub[:, mm[m]]])
        beta, *_ = np.linalg.lstsq(X, r1[:, m, :], rcond=None)
        fit = X @ beta; r2[:, m, :] = r1[:, m, :] - fit
        y = r1[:, m, :] - r1[:, m, :].mean(0)
        ss += ((fit - fit.mean(0)) ** 2).sum(); st += (y ** 2).sum()
    return r2, ss / st


def flat(r2, lo, hi):
    return r2[lo:hi].reshape(hi - lo, nM * nP)


# ---- A. support
def support(b, frac=0.5):
    idx = np.where(np.abs(b) > frac * np.abs(b).max())[0]
    markets = {i // nP for i in idx}; practices = {i % nP for i in idx}
    return len(markets) >= 2 and len(practices) >= 2


# ---- B. bulk clearance
def bulk_ratio(r2, b, lo, hi, k_exist):
    X = flat(r2, lo, hi); X = X - X.mean(0)
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    resid = X - (U[:, :k_exist] * s[:k_exist]) @ Vt[:k_exist]
    lam = np.linalg.eigvalsh(np.cov(resid.T))
    bulk = np.median(lam)
    q = b / np.linalg.norm(b)
    return float(np.var(resid @ q) / bulk)


# ---- C. stability
def sign_agreement(r2, b, lo, hi, k_exist):
    """Loadings on the candidate's series, fit on each half of the window AFTER
    the existing lines are removed. A candidate that only re-labels the existing
    lines has nothing left to be stable about."""
    X = flat(r2, lo, hi); X = X - X.mean(0)
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    resid = X - (U[:, :k_exist] * s[:k_exist]) @ Vt[:k_exist]
    n = len(resid) // 2; q = b / np.linalg.norm(b); out = []
    for A in (resid[:n], resid[n:]):
        A = A - A.mean(0); f = A @ q
        out.append(np.sign((A.T @ f) / (f @ f)))
    return float((out[0] == out[1]).mean())


# ---- E. monitor
def eig_ratio_k(X, kmax=15):
    X = X - X.mean(0)
    lam = np.sort(np.linalg.eigvalsh(np.cov(X.T)))[::-1][: kmax + 1]
    return int(np.argmax(lam[:-1] / np.maximum(lam[1:], 1e-12))) + 1


def count_after(r2, lo, hi, extra=None, k_exist=3):
    """Eigenvalue-ratio count of factors left in the residual after the existing
    lines, and after one more admitted line. A true line should take one away."""
    X = flat(r2, lo, hi); X = X - X.mean(0)
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    basis = Vt[:k_exist]
    if extra is not None: basis = np.vstack([basis, extra / np.linalg.norm(extra)])
    Q, _ = np.linalg.qr(basis.T)
    return eig_ratio_k(X - X @ Q @ Q.T)


def main(seeds=(11, 12, 13, 14, 15)):
    print("=" * 76)
    print("LONGING RESEARCH — the rest of the gate battery, on", HARNESS.split("/")[-1])
    print("=" * 76)
    p = sim.Params(); k_exist = 3; n_null = 40
    data = []
    for sd in seeds:
        r1, dsub, arr = panel(p, sd)
        r2, r2_sched = strip_schedule(r1, dsub, arr)
        data.append((sd, r1, dsub, arr, r2, r2_sched, true_loadings(sd, p.n_factors)))

    # A
    print("\nA. Support gate — at least two markets and two practices among entries above half the max |loading|")
    rng = np.random.default_rng(0)
    res = {"random null": [], "true column": [], "single cell": [], "single market": [], "single practice": []}
    for sd, r1, dsub, arr, r2, _, L in data:
        for _ in range(n_null): res["random null"].append(support(rng.standard_normal(nM * nP)))
        for k in range(L.shape[1]): res["true column"].append(support(np.tile(L[:, k], nM)))
        for _ in range(n_null):
            b = np.zeros(nM * nP); b[rng.integers(nM * nP)] = 1; res["single cell"].append(support(b))
            b = np.zeros(nM * nP); m = rng.integers(nM); b[m * nP:(m + 1) * nP] = rng.standard_normal(nP); res["single market"].append(support(b))
            b = np.zeros(nM * nP); pr = rng.integers(nP); b[pr::nP] = rng.standard_normal(nM); res["single practice"].append(support(b))
    for k, v in res.items(): print("   %-16s pass %.2f" % (k, np.mean(v)))
    print("   (the gate is not a size/power test; it is the floor that turns a cell effect away)")

    # B
    print("\nB. Bulk clearance — variance along the candidate / median eigenvalue of the residual after %d PCs" % k_exist)
    print("   %-8s %12s %12s %12s %8s" % ("window", "null median", "null 95%", "true median", "power"))
    for w, (lo, hi) in (("early", EARLY), ("late", LATE)):
        nul, tru = [], []
        for sd, r1, dsub, arr, r2, _, L in data:
            rng = np.random.default_rng(sd)
            for _ in range(n_null): nul.append(bulk_ratio(r2, rng.standard_normal(nM * nP), lo, hi, k_exist))
            for k in range(L.shape[1]): tru.append(bulk_ratio(r2, np.tile(L[:, k], nM), lo, hi, k_exist))
        thr = np.quantile(nul, 0.95)
        print("   %-8s %12.2f %12.2f %12.2f %8.2f" % (w, np.median(nul), thr, np.median(tru), (np.array(tru) > thr).mean()))

    # C
    print("\nC. Stability — share of the 33 loading signs that agree between the two halves, on the residual after %d PCs" % k_exist)
    print("   %-8s %12s %12s %12s %8s" % ("window", "null median", "null 95%", "true median", "power"))
    for w, (lo, hi) in (("early", EARLY), ("late", LATE)):
        nul, tru = [], []
        for sd, r1, dsub, arr, r2, _, L in data:
            rng = np.random.default_rng(sd)
            for _ in range(n_null): nul.append(sign_agreement(r2, rng.standard_normal(nM * nP), lo, hi, k_exist))
            for k in range(L.shape[1]): tru.append(sign_agreement(r2, np.tile(L[:, k], nM), lo, hi, k_exist))
        thr = np.quantile(nul, 0.95)
        print("   %-8s %12.2f %12.2f %12.2f %8.2f" % (w, np.median(nul), thr, np.median(tru), (np.array(tru) > thr).mean()))
    print("   (a random direction's loadings are noise, so its signs flip between halves; a factor's do not)")

    # D
    print("\nD. Placebo — R^2 of the declared schedule regression on 26-week block returns, true market labels vs the five permutations")
    perms = [pm for pm in itertools.permutations(range(nM)) if list(pm) != list(range(nM))]
    for w, (lo, hi) in (("early", EARLY), ("late", LATE), ("full", (1, T - 1))):
        tr, pl = [], []
        for sd, r1, dsub, arr, r2, _, L in data:
            _, s_true = strip_schedule(r1[lo:hi], dsub[lo:hi], arr[lo:hi], None, 26)
            tr.append(s_true)
            for pm in perms:
                _, s_p = strip_schedule(r1[lo:hi], dsub[lo:hi], arr[lo:hi], list(pm), 26); pl.append(s_p)
        print("   %-6s true R^2 %.3f   permuted R^2 median %.3f max %.3f   share of permutations beating the truth %.2f"
              % (w, np.mean(tr), np.median(pl), np.max(pl), np.mean([x >= np.mean(tr) for x in pl])))
    print("   (early the markets' schedules differ, so swapping labels should cost explanatory power; late they coincide)")

    # E
    print("\nE. Unexplained monitor — eigenvalue-ratio count of factors left in the residual, before and after admitting a line")
    print("   %-8s %-12s %12s" % ("window", "admitted", "count (mean)"))
    for w, (lo, hi) in (("early", EARLY), ("late", LATE)):
        base, nul, tru = [], [], []
        for sd, r1, dsub, arr, r2, _, L in data:
            rng = np.random.default_rng(sd)
            base.append(count_after(r2, lo, hi, None, k_exist))
            for _ in range(10): nul.append(count_after(r2, lo, hi, rng.standard_normal(nM * nP), k_exist))
            for k in range(L.shape[1]): tru.append(count_after(r2, lo, hi, np.tile(L[:, k], nM), k_exist))
        for name, v in (("none", base), ("null", nul), ("true", tru)):
            print("   %-8s %-12s %12.2f" % (w, name, np.mean(v)))
    print("   (the monitor triggers the promotion search while a count above zero remains; a null admitted leaves it where it was)")
    print("\nNothing above selects a factor set. Wave dates and every coefficient upstream are placeholders except where measured.")


if __name__ == "__main__":
    main()
