"""LONGING RESEARCH — identification experiment on the generated world (v2: harness path as argv[1]).

Runs the procedure every fourth-round reviewer proposed and none ran: generate
the 33 x 1565 panel from the v3 harness, strip the measured lines, and ask what
the listing can identify — early, late, and under a planted null.

It does NOT select a factor set. It reports:

  1. the two-way variance decomposition (common / market / practice /
     interaction) of residual returns, early vs late — the handover;
  2. a confusion table: true event-factor count in the generator vs the count
     an eigenvalue-ratio estimator recovers, early vs late;
  3. the promotion gate's size and power: how often a planted null direction
     passes a held-out gate, and how often a true one does, across thresholds;
  4. leave-one-market-out: how well two markets' factor loadings explain the
     third, early vs late;
  5. order sensitivity: how much attribution moves between the substitution
     line and the factor lines when their orthogonalisation order is swapped.

numpy only, plus the harness (stdlib). `python3 this.py` prints the tables.
The harness's wave dates are placeholders; so is everything downstream.
"""
import importlib.util, math, random, sys
import numpy as np

HARNESS = sys.argv[1] if len(sys.argv) > 1 else "raw/documents/2026-09-20-loop-simulation-harness-v3.py"
spec = importlib.util.spec_from_file_location("sim", HARNESS)
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)

nM, nP, T = len(sim.MARKETS), len(sim.UNIVERSE), sim.WEEKS
EARLY, LATE = (60, 460), (T - 400, T - 1)   # same windows the harness tests use
K_MAX = 15


def true_loadings(seed, k):
    """The harness draws `load` first from random.Random(seed); reproduce it."""
    rng = random.Random(seed)
    return np.array([[rng.gauss(0, 1) for _ in range(k)] for _ in range(nP)])


def panel(p, seed):
    """Weekly log returns r[t, m, p] of the QUOTE, plus the measured lines."""
    H = sim.run(p, seed)
    P = np.array([[H["P"][m][i] for i in range(nP)] for m in range(nM)])   # m,p,t
    r = np.diff(np.log(P), axis=2).transpose(2, 0, 1)                        # t,m,p
    dU = np.diff(np.log(np.array(H["U"])))                                    # numeraire line, exact
    sub = np.array(H["sub"])                                                  # m,t
    dsub = np.diff(sub, axis=1).T                                             # t,m
    arr = np.array([[sim.wave_state(t, m, p)[0] for m in range(nM)] for t in range(1, T)])
    return r, dU, dsub, arr


def strip_numeraire(r, dU):
    return r + dU[:, None, None]          # P = V e^z / U  =>  log-return + dlogU


def strip_schedule(r1, dsub, arr):
    """Regress each security on its own market's declared arrival and
    substitution increments. Returns residual and the fitted (line) part."""
    r2 = np.empty_like(r1); fit = np.empty_like(r1)
    for m in range(nM):
        X = np.column_stack([np.ones(len(r1)), arr[:, m], dsub[:, m]])
        beta, *_ = np.linalg.lstsq(X, r1[:, m, :], rcond=None)
        fit[:, m, :] = X @ beta
        r2[:, m, :] = r1[:, m, :] - fit[:, m, :]
    return r2, fit


def two_way(r2, lo, hi):
    """Variance shares of the additive blocks over a window. Each week's 3x11
    cell of returns is split into grand mean + market effect + practice effect
    + interaction, and the squared mass of each block is summed."""
    X = r2[lo:hi]                                    # t,m,p
    g = X.mean(axis=(1, 2), keepdims=True)
    me = X.mean(axis=2, keepdims=True) - g
    pe = X.mean(axis=1, keepdims=True) - g
    inter = X - g - me - pe
    tot = (X ** 2).sum()
    return {"common": (g ** 2).sum() * nM * nP / tot,
            "market": (me ** 2).sum() * nP / tot,
            "practice": (pe ** 2).sum() * nM / tot,
            "interaction": (inter ** 2).sum() / tot}


def eig_ratio_k(X, kmax=K_MAX):
    """Ahn–Horenstein eigenvalue-ratio estimator on a T x N panel."""
    X = X - X.mean(0)
    lam = np.sort(np.linalg.eigvalsh(np.cov(X.T)))[::-1]
    lam = lam[: kmax + 1]
    ratios = lam[:-1] / np.maximum(lam[1:], 1e-12)
    return int(np.argmax(ratios)) + 1


def flat(r2, lo, hi):
    return r2[lo:hi].reshape(hi - lo, nM * nP)


def practice_avg(r2, lo, hi):
    return r2[lo:hi].mean(axis=1)                    # t,p — cross-market-uniform part


def gate(r2, b, lo, hi, k_exist, thr):
    """One promotion gate: does candidate direction b lower held-out
    unexplained variance beyond k_exist principal components, by > thr?
    Loadings and PCs are fit on the first half of the window, scored on the
    second half. Returns (passed, reduction)."""
    X = flat(r2, lo, hi); n = len(X) // 2
    A, B = X[:n] - X[:n].mean(0), X[n:] - X[:n].mean(0)
    # existing lines: top-k PCs of the fit half
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    base = Vt[:k_exist]                                    # k,N
    def unexplained(basis):
        if len(basis) == 0: return (B ** 2).sum()
        Q, _ = np.linalg.qr(basis.T)                       # N,k orthonormal
        return ((B - B @ Q @ Q.T) ** 2).sum()
    u0 = unexplained(base)
    u1 = unexplained(np.vstack([base, b / np.linalg.norm(b)]))
    red = (u0 - u1) / (B ** 2).sum()
    return red > thr, red


def loo_market(r2, lo, hi, k):
    """Estimate k practice-level factor loadings from two markets, project the
    third. Returns mean held-out R^2 across the three choices."""
    out = []
    for hold in range(nM):
        keep = [m for m in range(nM) if m != hold]
        X = r2[lo:hi][:, keep, :].reshape(hi - lo, -1)     # t, 2*11
        X = X - X.mean(0)
        U, s, Vt = np.linalg.svd(X, full_matrices=False)
        F = U[:, :k] * s[:k]                               # factor series, t x k
        Y = r2[lo:hi][:, hold, :]; Y = Y - Y.mean(0)
        beta, *_ = np.linalg.lstsq(F, Y, rcond=None)
        out.append(1 - ((Y - F @ beta) ** 2).sum() / (Y ** 2).sum())
    return float(np.mean(out))


def order_sensitivity(r1, dsub, arr, lo, hi, k):
    """How much the declared schedule line's weekly attribution moves when the
    orthogonalisation order is swapped: schedule first (then PCs on the
    residual) versus PCs first (then schedule on the residual). Returns
    rms(line_A - line_B) / rms(line_A) over the window, plus the two lines'
    mean weekly drift in basis points, averaged over securities."""
    _, fitA = strip_schedule(r1, dsub, arr); fitA = fitA[lo:hi]
    X = flat(r1, lo, hi); mu = X.mean(0); Xc = X - mu
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    resid = (Xc - (U[:, :k] * s[:k]) @ Vt[:k] + mu).reshape(hi - lo, nM, nP)
    _, fitB = strip_schedule(resid, dsub[lo:hi], arr[lo:hi])
    rel = math.sqrt(((fitA - fitB) ** 2).mean()) / math.sqrt((fitA ** 2).mean())
    return rel, 1e4 * fitA.mean(), 1e4 * fitB.mean()


def main(seeds=(11, 12, 13, 14, 15), truths=(3, 6, 9, 13)):
    print("=" * 76)
    print("LONGING RESEARCH — identification experiment on", HARNESS.split("/")[-1])
    print("=" * 76)

    # ---- 1. handover, at the harness default (n_factors=9)
    p = sim.Params()
    dec = {"early": [], "late": []}
    for sd in seeds:
        r, dU, dsub, arr = panel(p, sd)
        r2, _ = strip_schedule(strip_numeraire(r, dU), dsub, arr)
        dec["early"].append(two_way(r2, *EARLY)); dec["late"].append(two_way(r2, *LATE))
    print("\n1. Two-way variance shares of residual returns after the measured lines")
    print("   (mean over %d seeds; blocks: common 1 / market 2 / practice 10 / interaction 20 dof)" % len(seeds))
    print("   %-8s %8s %8s %9s %12s" % ("window", "common", "market", "practice", "interaction"))
    for w in ("early", "late"):
        m = {k: np.mean([d[k] for d in dec[w]]) for k in dec[w][0]}
        print("   %-8s %8.3f %8.3f %9.3f %12.3f" % (w, m["common"], m["market"], m["practice"], m["interaction"]))

    # ---- 2. confusion: true k vs estimated k, three panels, early vs late
    print("\n2. Recovered factor count (eigenvalue ratio, kmax=%d) vs true event-factor count" % K_MAX)
    print("   panels: full 33; practice-average 11 (cross-market-uniform); market-demeaned 33")
    hdr = "   %-6s %-6s | %5s %5s %5s | %5s %5s %5s" % ("true", "seeds", "e:33", "e:11", "e:dm", "l:33", "l:11", "l:dm")
    print(hdr)
    conf = {}
    for kt in truths:
        p = sim.Params(n_factors=kt)
        rows = []
        for sd in seeds:
            r, dU, dsub, arr = panel(p, sd)
            r2, _ = strip_schedule(strip_numeraire(r, dU), dsub, arr)
            ests = []
            for lo, hi in (EARLY, LATE):
                X = flat(r2, lo, hi)
                Xdm = (r2[lo:hi] - r2[lo:hi].mean(axis=2, keepdims=True)).reshape(hi - lo, -1)
                ests += [eig_ratio_k(X), eig_ratio_k(practice_avg(r2, lo, hi), kmax=9), eig_ratio_k(Xdm)]
            rows.append(ests)
        conf[kt] = rows
        med = np.median(rows, axis=0)
        print("   %-6d %-6d | %5.0f %5.0f %5.0f | %5.0f %5.0f %5.0f" % (kt, len(seeds), *med))
    print("   (medians; a cell equal to `true` is recovery, a cell stuck at 1 is a dominant common direction)")

    # ---- 3. gate size and power, threshold calibrated on the null
    print("\n3. Promotion gate — held-out reduction of unexplained variance beyond k existing PCs")
    print("   A random direction always removes SOME variance, so the threshold cannot be a")
    print("   fixed number: it is the 95th percentile of planted-null reductions, per window.")
    p = sim.Params(); k_exist = 3; n_null = 40
    res = {w: {"null": [], "true": []} for w in ("early", "late")}
    for sd in seeds:
        r, dU, dsub, arr = panel(p, sd)
        r2, _ = strip_schedule(strip_numeraire(r, dU), dsub, arr)
        L = true_loadings(sd, p.n_factors)
        rng = np.random.default_rng(sd)
        for w, (lo, hi) in (("early", EARLY), ("late", LATE)):
            for _ in range(n_null):
                res[w]["null"].append(gate(r2, rng.standard_normal(nM * nP), lo, hi, k_exist, 0)[1])
            for k in range(p.n_factors):
                res[w]["true"].append(gate(r2, np.tile(L[:, k], nM), lo, hi, k_exist, 0)[1])
    print("   %-8s %12s %12s %12s %8s" % ("window", "null median", "null 95%", "true median", "power"))
    for w in ("early", "late"):
        nul, tru = np.array(res[w]["null"]), np.array(res[w]["true"])
        thr = np.quantile(nul, 0.95)
        print("   %-8s %12.4f %12.4f %12.4f %8.2f" % (w, np.median(nul), thr, np.median(tru), (tru > thr).mean()))
    print("   (null = random 33-vector, %d per seed; true = one generator loading column tiled across" % n_null)
    print("    markets; power = share of true columns clearing the null's 95th percentile)")

    # ---- 4. leave-one-market-out
    print("\n4. Leave-one-market-out: held-out R^2 of the third market from k factors fit on two")
    p = sim.Params()
    r2s = []
    for sd in seeds:
        r, dU, dsub, arr = panel(p, sd)
        r2s.append(strip_schedule(strip_numeraire(r, dU), dsub, arr)[0])
    for k in (2, 5, 9):
        e = np.mean([loo_market(r2, *EARLY, k) for r2 in r2s])
        l = np.mean([loo_market(r2, *LATE, k) for r2 in r2s])
        print("   k=%d   early %.3f   late %.3f" % (k, e, l))

    # ---- 5. order sensitivity
    print("\n5. The declared schedule line under two orthogonalisation orders (k=5 PCs removed first)")
    print("   %-6s %14s %22s %22s" % ("window", "rms shift/rms", "schedule-first bp/wk", "factors-first bp/wk"))
    for w, (lo, hi) in (("early", EARLY), ("late", LATE)):
        rows = []
        for sd in seeds:
            r, dU, dsub, arr = panel(p, sd)
            rows.append(order_sensitivity(strip_numeraire(r, dU), dsub, arr, lo, hi, 5))
        m = np.mean(rows, axis=0)
        print("   %-6s %14.3f %22.2f %22.2f" % (w, *m))
    print("   (rms shift = root-mean-square change in the line's weekly attribution when the order")
    print("    is swapped, relative to the line's own rms; bp/wk = the line's mean weekly drift)")
    print("\nNothing above selects a factor set. Wave dates and every coefficient are placeholders.")


if __name__ == "__main__":
    main()
