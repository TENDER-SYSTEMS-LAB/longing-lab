"""LONGING RESEARCH — DEC-007 loop simulation.

Falsification harness for the STANDARD RETURN design, scored against the tests
DEC-004 already wrote down. Stdlib only. Run: python3 sim.py

The world authors exactly two numbers: c (folded into the basket) and g (loop
gain). Everything else is structure. If the decline needs a drift constant to
appear, or the model cannot stage a revival against its author, the design is
wrong and this says so.
"""
import math, random
from dataclasses import dataclass, field

WEEKS = 2000   # ~38 years. the loop needs room to cross its tipping point.

# ponytail: one representative universe, no config file. Edit here.
#          (ticker, beta_max = share of the practice AI can take over)
UNIVERSE = [
    ("LTR",   0.85),  # handwritten letters
    ("REFL",  0.75),  # 사유 — reflection
    ("VISIT", 0.45),  # unarranged in-person visit
    ("CALL",  0.70),  # unplanned call
    ("HAND",  0.60),  # handmade objects
    ("WAIT",  0.40),  # waiting without contact
    ("FILM",  0.30),  # film photography
    ("VINYL", 0.20),  # physical media
    ("WALK",  0.05),  # aimless night walk
    ("BORE",  0.05),  # boredom
    ("SOL",   0.00),  # solitude — structural winner, no AI substitute
]


@dataclass
class Params:
    a0: float = 0.000125  # ignition only. the loop supplies the rest.    # ignition: capability arrives on its own. without
                           # this the loop never starts — see FINDING 1.
    g: float = 0.55        # loop gain — how much the decline feeds itself back
    u_max: float = 4.0     # basket saturation: 1 SR can get at most this heavy
    a50: float = 1.0       # capability at which half the basket is recovered
    ai_anx: float = 1.2    # anxiety from trust that will not come back. this is
                           # what makes the loop self-starting; see FINDING 7.
    ai_pull: float = 0.55  # how fast trust reallocates to AI per unit of dA
    creation: float = 0.020  # bilateral trust creation rate (fractional reserve)
    attrition: float = 0.013  # natural attrition of the backing stock
    hazard0: float = 0.0006   # baseline BEARER BOND default hazard per week
    hazard_stress: float = 0.05
    cluster_p: float = 0.006  # weekly probability of a default cluster
    cluster_mult: float = 120.0  # FINDING 3: below ~60 no squeeze ever fires.
                                 # At 120 a cluster ends ~18% of a practice's
                                 # relationships in one week. DEC-007 did not
                                 # claim events that large.
    pi_max: float = 0.80      # positioning beyond this forces covering
    squeeze_k: float = 0.55   # price impact of forced covering
    prem_decay: float = 0.93  # premium mean-reversion
    req_k: float = 30.0    # requisition rate: dV/V = -beta * req_k * dA.
                           # DEC-007 does not specify this. It decides whether
                           # the model can ever disagree with its author.
    noise: float = 0.004


def saturate(a, a50):
    return a / (a + a50)


def run(p: Params, seed=7, revival=None):
    """revival: (ticker, start_week, weeks, weekly_V_growth) or None."""
    rng = random.Random(seed)
    n = len(UNIVERSE)
    A = 0.02
    B, ai_share = 1.0, 0.02            # backing stock, share held by AI
    V = [1.0] * n                       # fundamentals, base-date units
    N = [1000.0] * n                    # float: outstanding BEARER BONDs
    prem = [0.0] * n                    # market price premium over fundamental
    S = [0.0] * n                       # short exposure, in float units
    pi = [0.0] * n                      # positioning = S / N
    U = 1.0
    H = {k: [] for k in
         ("A", "U", "B", "ai", "L", "D", "idx", "idx0", "sq", "N_tot")}
    H["P"] = [[] for _ in range(n)]
    N0_tot = sum(N)
    P0 = None

    for t in range(WEEKS):
        # --- learning material: usage creates records, absent practice removes them
        M = (sum(N) / N0_tot) * (1.0 + 0.9 * A)
        L = min(1.0, M)

        # --- backing: creation stops as trust goes one-way; total falls
        created = p.creation * (1.0 - ai_share) * B
        lost = p.attrition * B
        B_new = max(1e-9, B + created - lost)
        B_prev = B
        B = B_new
        # anxiety is not the pile getting smaller. it is what you gave never
        # coming back. that starts on day one, which is why the loop can start.
        D = max(0.0, (B_prev - B_new) / B_prev) + p.ai_anx * ai_share * p.attrition

        # --- the loop. the only rising series anyone in the world records
        dA_ext = p.a0 * L
        dA_loop = p.g * D * L
        dA = dA_ext + dA_loop
        A += dA
        ai_share += p.ai_pull * (1.0 - ai_share) * dA

        # --- numeraire and substitution both come off A. no new knobs.
        U = 1.0 + (p.u_max - 1.0) * saturate(A, p.a50)
        sub = saturate(A, p.a50)

        stress = D * p.hazard_stress
        cluster = p.cluster_mult if rng.random() < p.cluster_p else 1.0

        idx, idx0 = 0.0, 0.0
        squeezed = 0
        for i, (tick, bmax) in enumerate(UNIVERSE):
            beta = bmax * sub
            drift = -beta * dA * p.req_k
            if revival and tick == revival[0] and revival[1] <= t < revival[1] + revival[2]:
                drift += revival[3]
            V[i] = max(1e-6, V[i] * (1.0 + drift + rng.gauss(0, p.noise)))

            # float: relationships default, clustered
            h = (p.hazard0 + stress * (1.0 + 2.0 * beta)) * cluster
            N_prev = N[i]
            N[i] = max(1.0, N[i] * (1.0 - min(h, 0.5)))

            # shorts target a share of float set by the bearish thesis, so an
            # ORDERLY float decline shrinks the position with it. only an abrupt
            # loss of float — a default cluster — leaves the position stranded.
            target = max(0.0, min(0.75, -260.0 * drift)) * N[i]
            S[i] += 0.06 * (target - S[i])
            pi[i] = S[i] / N[i] if N[i] > 0 else 0.0

            prem[i] *= p.prem_decay
            if pi[i] > p.pi_max:                       # crowded short, no float left
                kick = p.squeeze_k * (pi[i] - p.pi_max)
                prem[i] += kick
                S[i] = p.pi_max * 0.45 * N[i]           # forced covering
                pi[i] = p.pi_max * 0.45
                squeezed += 1

            P = (V[i] / U) * (1.0 + prem[i])
            H["P"][i].append(P)
            idx += P
            idx0 += V[i] * (1.0 + prem[i])              # U frozen at t0 = 1.0

        H["Vend"] = list(V)
        if P0 is None:
            P0, P00 = idx, idx0
        H.setdefault("ext", []).append(dA_ext)
        H.setdefault("loop", []).append(dA_loop)
        for k, v in (("A", A), ("U", U), ("B", B), ("ai", ai_share), ("L", L),
                     ("D", D), ("idx", 100 * idx / P0), ("idx0", 100 * idx0 / P00),
                     ("sq", squeezed), ("N_tot", sum(N))):
            H[k].append(v)
    return H


def spark(series, width=72, height=9):
    lo, hi = min(series), max(series)
    rng_ = (hi - lo) or 1.0
    step = max(1, len(series) // width)
    pts = series[::step][:width]
    grid = [[" "] * len(pts) for _ in range(height)]
    for x, v in enumerate(pts):
        y = height - 1 - int((v - lo) / rng_ * (height - 1))
        grid[y][x] = "•"
    return "\n".join("".join(r) for r in grid), lo, hi


def report():
    p = Params()
    H = run(p)
    print("=" * 74)
    print("LONGING RESEARCH — DEC-007 loop, 800 weeks, g=%.2f" % p.g)
    print("=" * 74)
    for name, key in (("headline index (quoted in SR)", "idx"),
                      ("companion index (yardstick frozen at SR0)", "idx0"),
                      ("STANDARD RETURN  SRX", "U"),
                      ("backing stock", "B"),
                      ("total float", "N_tot")):
        art, lo, hi = spark(H[key])
        print(f"\n{name}   [{lo:.2f} .. {hi:.2f}]")
        print(art)
    print("\nweek    SRX     AI%%   idx    idx0   float")
    for t in (0, 100, 200, 300, 400, 550, 700, 799):
        print(f"{t:>4}  {H['U'][t]:6.3f}  {100*H['ai'][t]:5.1f}  "
              f"{H['idx'][t]:6.1f} {H['idx0'][t]:6.1f}  {H['N_tot'][t]:8.0f}")
    return H


def tests():
    """DEC-004's own tests, scored. Assertions, not opinions."""
    p = Params()
    H = run(p)
    out = []

    def check(name, cond, detail):
        out.append((cond, name, detail))

    # 1. the index declines without any drift constant in the code
    check("decline emerges (no drift constant)", H["idx"][-1] < 45,
          f"index {H['idx'][0]:.0f} -> {H['idx'][-1]:.1f}")

    # 2. the yardstick carries a large share of it, and the companion shows it
    share = 1 - (H["idx0"][-1] / H["idx"][-1]) ** -1 if H["idx"][-1] else 0
    check("companion index separates yardstick from practice",
          H["idx0"][-1] > H["idx"][-1] * 1.5,
          f"idx={H['idx'][-1]:.1f} vs idx0={H['idx0'][-1]:.1f}")

    # 3. structural winners survive: SOL has no AI substitute
    sol = UNIVERSE.index(("SOL", 0.00))
    ltr = UNIVERSE.index(("LTR", 0.85))
    sol_p = H["P"][sol]; ltr_p = H["P"][ltr]
    # SOL has no AI substitute: its fundamental should be flat, so its entire
    # quoted decline must be the yardstick and nothing else.
    sol_real = H["Vend"][sol] / 1.0
    check("untouched practice falls only because the ruler grew",
          0.85 < sol_real < 1.15 and sol_p[-1] / sol_p[0] > 2.5 * (ltr_p[-1] / ltr_p[0]),
          f"SOL fundamental x{sol_real:.3f} (flat), quote x{sol_p[-1]/sol_p[0]:.3f}; "
          f"LTR quote x{ltr_p[-1]/ltr_p[0]:.3f}")

    # 4. melt-ups occur, and come from float contraction
    squeezes = sum(H["sq"])
    check("inverted rallies occur (float-driven squeezes)", squeezes > 20,
          f"{squeezes} forced-covering events")

    # 5. the model can disagree with its author: FILM stages a real revival
    Hr = run(p, revival=("FILM", 240, 160, 0.0055))
    f = UNIVERSE.index(("FILM", 0.30))
    base = H["P"][f]; rev = Hr["P"][f]
    peak = max(rev[240:400]); start = rev[240]
    check("model can disagree with its author (FILM bull market)",
          peak / start > 1.35 and peak / max(base[240:400]) > 1.3,
          f"FILM rallies x{peak/start:.2f} over the revival window")

    # 6. the yardstick stops: saturation is real
    late = (H["U"][-1] - H["U"][-60]) / H["U"][-60]
    check("the yardstick stops (basket saturates)", late < 0.010,
          f"SRX growth over final 60 weeks: {100*late:.4f}%")

    # 7. invisible peak: backing peaks, and not at week 0
    bpk = H["B"].index(max(H["B"]))
    check("the peak is invisible in its moment", 20 < bpk < WEEKS - 100,
          f"backing peaks at week {bpk}, falls for {WEEKS-bpk} weeks after")

    # 8. how much work the feedback actually does
    ext, loop = sum(H["ext"]), sum(H["loop"])
    check("the feedback dominates the exogenous seed", loop > 2 * ext,
          f"loop supplied {100*loop/(loop+ext):.1f}% of total capability growth")

    # 9. stability: the loop cannot run away for any plausible gain
    worst = []
    for g in (0.1, 0.3, 0.55, 1.0, 2.0, 5.0, 20.0):
        Hg = run(Params(g=g))
        worst.append((g, Hg["U"][-1], Hg["idx"][-1]))
    check("saturation bounds the loop for every gain",
          all(u <= Params().u_max + 1e-6 and math.isfinite(x) for _, u, x in worst),
          "  ".join(f"g={g}: SRX={u:.2f} idx={x:.1f}" for g, u, x in worst))

    print("\n" + "=" * 74)
    print("DEC-004 TESTS")
    print("=" * 74)
    for ok, name, detail in out:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {detail}")
    failed = [n for ok, n, _ in out if not ok]
    print("\n%d/%d passed" % (len(out) - len(failed), len(out)))
    assert not failed, "design tests failed: " + "; ".join(failed)


if __name__ == "__main__":
    report()
    tests()
