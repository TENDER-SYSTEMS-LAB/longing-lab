"""LONGING RESEARCH — DEC-007 loop simulation.

Falsification harness for the STANDARD RETURN design, scored against the tests
DEC-004 already wrote down. Stdlib only. Run: python3 sim.py

The world authors two numbers — an ignition and a loop gain. Everything else is
structure. If the decline needs a drift constant, or the model cannot stage a
revival against its author, the design is wrong and this says so.

Market texture is deliberately shaped to read like a real index inverted: vol
clusters, regimes persist, and forced covering cascades over months instead of
resolving in a week. That shaping is a STYLISTIC calibration to DEC-002's
terminal register. It is evidence about how the surface reads, never evidence
about the world.
"""
import math, random, statistics
from dataclasses import dataclass

WEEKS = 2000   # ~38 years. the loop needs room to cross its tipping point.

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
    ("SOL",   0.00),  # solitude — no AI substitute at all
]

# regimes. a real index is not one process; it is a few, and it stays in each
# for a long time. names describe what the LONGING terminal shows, not a mood.
#        name         vol    event rate  run prob   mean dwell (weeks)
REGIMES = [("quiet",   0.85,   0.62,     0.0015,     150),
           ("choppy",  1.15,   0.75,     0.0090,      90),
           ("stressed",2.60,   1.20,     0.0400,      35)]
TRANS = [[0.00, 0.80, 0.20],     # quiet    -> choppy mostly
         [0.55, 0.00, 0.45],     # choppy   -> either
         [0.25, 0.75, 0.00]]     # stressed -> choppy mostly


@dataclass
class Params:
    # --- the world's two authored numbers
    a0: float = 0.000125   # ignition: capability arrives on its own
    g: float = 0.55        # loop gain: how much the decline feeds itself back

    # --- numeraire
    u_max: float = 4.0     # basket saturation: 1 SR gets at most this heavy
    a50: float = 1.0
    req_k: float = 14.0    # requisition rate. DEC-007 does not specify this.

    # --- backing
    ai_anx: float = 1.2    # anxiety from trust that will not come back
    ai_pull: float = 0.55
    creation: float = 0.020
    attrition: float = 0.013

    # --- events (DEC-003: weekly prices, monthly research, something in between)
    ev_mag: float = 0.027
    ev_macro_p: float = 0.62
    ev_true_q: float = 0.40
    ev_true_share: float = 0.12   # of an event's impact, how much is true of the
                                  # practice. price vol must exceed fundamental
                                  # vol or every quote becomes news about letters.
    research_pull: float = 0.55
    n_factors: int = 9

    # --- float and positioning
    hazard0: float = 0.0006
    hazard_stress: float = 0.05
    cluster_p: float = 0.10
    cluster_ref: float = 0.004
    cluster_mult: float = 120.0
    # BEARER BOND is issuable as well as defaultable — reserve-instruments says
    # so, and the first build only implemented the defaults. without issuance a
    # practice can never be resumed, float only falls, and a melt-up can never
    # relapse. Q-002 owns who issues; this is the arithmetic placeholder.
    # DEC-004 names three rally engines. weeks come from squeezes, months from
    # the macro decelerating, and years from a genuine revival — film and vinyl
    # really did come back. this is that third engine.
    revive_p: float = 0.00010  # weekly chance ONE practice starts coming back
    # DEC-004 requires that changed conditions permit recovery. one era of
    # revival is SCHEDULED rather than drawn each week: a coin flip with a tiny
    # probability either never fires or fires twice, and the history needs
    # exactly one long uptrend to be a history rather than a slope.
    era_n: int = 1
    era_len: int = 250
    era_str: float = 0.0035
    revive_len: int = 260      # ~5 years
    revive_str: float = 0.0042 # weekly fundamental growth while it lasts
    birth: float = 0.0042    # new relationships per week, scaled by practice health
    sys_loss: float = 0.30   # a systemic week is a run, not a higher hazard
    pi_max: float = 0.80
    squeeze_k: float = 0.55
    cover_rate: float = 0.26  # <1 turns a one-week spike into a months-long melt-up
    mtm_force: float = 0.9    # rising price forces more covering, which raises it
    over_cap: float = 0.09    # a single week can only force so much covering.
                              # without a cap the cascade is unbounded and the
                              # index prints +700% in five weeks.
    rebuild: float = 0.012    # shorts re-enter slowly after being carried out
    prem_decay: float = 0.972
    noise: float = 0.002


def run(p: Params, seed=7, revival=None):
    """revival: (ticker, start_week, weeks, weekly_V_growth) or None."""
    rng = random.Random(seed)
    n = len(UNIVERSE)
    load = [[rng.gauss(0, 1) for _ in range(p.n_factors)] for _ in range(n)]
    A, B, ai_share, U = 0.02, 1.0, 0.02, 1.0
    V, N = [1.0] * n, [1000.0] * n
    # z is a LOG premium. an additive one lets a quote go negative.
    z, S, pi, last_ret = [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n
    reg, dwell = 0, 40
    rev_until = [0] * n
    eras = sorted((int(rng.uniform(0.18, 0.72) * WEEKS),
                   int(rng.uniform(0.75, 1.35) * p.era_len)) for _ in range(p.era_n))
    N0, P0, P00 = sum(N), None, None
    H = {k: [] for k in ("A", "U", "B", "ai", "L", "D", "idx", "idx0",
                         "sq", "N_tot", "ext", "loop", "reg", "sys", "era")}
    H["P"] = [[] for _ in range(n)]
    H["P0"] = [[] for _ in range(n)]
    H["SQ"] = [[] for _ in range(n)]

    for t in range(WEEKS):
        if dwell <= 0:
            r = rng.random(); acc = 0.0
            for j, q in enumerate(TRANS[reg]):
                acc += q
                if r <= acc: reg = j; break
            dwell = int(rng.expovariate(1.0 / REGIMES[reg][4])) + 8
        dwell -= 1
        _, rvol, rrate, rsys, _ = REGIMES[reg]

        M = (sum(N) / N0) * (1.0 + 0.9 * A)
        L = min(1.0, M)

        created = p.creation * (1.0 - ai_share) * B
        B_prev, B = B, max(1e-9, B + created - p.attrition * B)
        # anxiety is not the pile shrinking. it is what you gave never returning.
        D = max(0.0, (B_prev - B) / B_prev) + p.ai_anx * ai_share * p.attrition

        dext, dloop = p.a0 * L, p.g * D * L
        dA = dext + dloop
        A += dA
        ai_share += p.ai_pull * (1.0 - ai_share) * dA
        U = 1.0 + (p.u_max - 1.0) * (A / (A + p.a50))
        sub = A / (A + p.a50)

        shock, truth = [0.0] * n, [0.0] * n
        ne = 0
        while rng.random() < rrate and ne < 5:
            ne += 1
            mag = rng.gauss(0, p.ev_mag * rvol)
            true_ev = rng.random() < p.ev_true_q
            if rng.random() < p.ev_macro_p:
                k = rng.randrange(p.n_factors)
                for j in range(n):
                    hit = mag * load[j][k] * 0.5
                    shock[j] += hit
                    if true_ev: truth[j] += hit * p.ev_true_share
            else:
                j = rng.randrange(n)
                shock[j] += mag
                if true_ev: truth[j] += mag * p.ev_true_share
        era = p.era_str if any(a <= t < a + d for a, d in eras) else 0.0
        research_week = (t % 4 == 3)
        systemic = rng.random() < rsys
        stress = D * p.hazard_stress

        idx = idx0 = 0.0
        sq_week = 0
        for i, (tick, bmax) in enumerate(UNIVERSE):
            beta = bmax * sub
            drift = -beta * dA * p.req_k + era
            if rev_until[i] == 0 and rng.random() < p.revive_p:
                rev_until[i] = t + int(rng.uniform(0.5, 1.5) * p.revive_len)
            if t < rev_until[i]:
                drift += p.revive_str
            elif rev_until[i] and t >= rev_until[i]:
                rev_until[i] = 0
            if revival and tick == revival[0] and revival[1] <= t < revival[1] + revival[2]:
                drift += revival[3]
            V[i] = max(1e-6, V[i] * (1.0 + drift + truth[i] + rng.gauss(0, p.noise)))

            pressure = min(1.0, abs(drift) / p.cluster_ref)
            cluster = p.cluster_mult if rng.random() < p.cluster_p * pressure else 1.0
            h = (p.hazard0 + stress * (1.0 + 2.0 * beta)) * cluster
            if systemic:
                h = 1.0 - (1.0 - min(h, 0.5)) * (1.0 - p.sys_loss * (0.45 + 0.55 * pressure))
            health = min(1.0, V[i])          # a dying practice is resumed less often
            N[i] = max(1.0, N[i] * (1.0 - min(h, 0.92)) + p.birth * health * 1000.0)

            target = max(0.0, min(0.75, -260.0 * drift)) * N[i]
            rate = 0.06 if S[i] < target else p.rebuild
            S[i] += rate * (target - S[i])
            pi[i] = S[i] / N[i] if N[i] > 0 else 0.0

            z[i] = z[i] * p.prem_decay + (shock[i] - truth[i])
            if research_week:
                z[i] *= (1.0 - p.research_pull)

            pain = max(0.0, last_ret[i]) * pi[i] * p.mtm_force
            over = min(p.over_cap, max(0.0, pi[i] - p.pi_max) + pain)
            if over > 1e-4:
                S[i] = max(0.0, S[i] - p.cover_rate * over * N[i])
                z[i] += p.squeeze_k * p.cover_rate * over
                pi[i] = S[i] / N[i] if N[i] > 0 else 0.0
                if over > 0.02:
                    H["SQ"][i].append(t); sq_week += 1

            P = (V[i] / U) * math.exp(z[i])
            prev = H["P"][i][-1] if H["P"][i] else P
            last_ret[i] = (P - prev) / prev if prev > 0 else 0.0
            H["P"][i].append(P)
            H["P0"][i].append(V[i] * math.exp(z[i]))
            idx += P; idx0 += V[i] * math.exp(z[i])

        if P0 is None: P0, P00 = idx, idx0
        H["Vend"] = list(V)
        for k, v in (("A", A), ("U", U), ("B", B), ("ai", ai_share), ("L", L),
                     ("D", D), ("idx", 100 * idx / P0), ("idx0", 100 * idx0 / P00),
                     ("sq", sq_week), ("N_tot", sum(N)), ("ext", dext),
                     ("loop", dloop), ("reg", reg), ("sys", 1 if systemic else 0),
                     ("era", 1 if era else 0)):
            H[k].append(v)
    return H


def tests():
    """DEC-004's own tests, plus the market-texture targets the reference index
    sets. Assertions, not opinions."""
    p = Params()
    H = run(p)
    idx = H["idx"]
    r = [idx[t] / idx[t - 1] - 1 for t in range(1, WEEKS)]
    out = []
    def check(name, cond, detail): out.append((cond, name, detail))

    check("decline emerges (no drift constant)", idx[-1] < 45,
          f"index {idx[0]:.0f} -> {idx[-1]:.1f}")
    check("companion index separates yardstick from practice",
          H["idx0"][-1] > idx[-1] * 1.5,
          f"idx={idx[-1]:.1f} vs idx0={H['idx0'][-1]:.1f}")

    sol = UNIVERSE.index(("SOL", 0.00)); ltr = UNIVERSE.index(("LTR", 0.85))
    sp, lp = H["P"][sol], H["P"][ltr]
    med = statistics.median(run(p, seed=s)["Vend"][sol] for s in range(5))
    # the claim is NO SYSTEMATIC DECLINE, so the band is asymmetric on purpose:
    # a practice AI never touched drifting upward is not a failure of it.
    check("untouched practice has no systematic decline",
          0.5 < med < 3.0 and sp[-1] / sp[0] > 10 * (lp[-1] / lp[0]),
          f"SOL fundamental median x{med:.3f} over 5 seeds; quote x{sp[-1]/sp[0]:.4f} "
          f"vs LTR x{lp[-1]/lp[0]:.5f}")

    check("inverted rallies occur (float-driven squeezes)", sum(H["sq"]) > 20,
          f"{sum(H['sq'])} forced-covering events")

    Hr = run(p, revival=("FILM", 240, 200, 0.0055))
    f = UNIVERSE.index(("FILM", 0.30))
    peak = max(Hr["P"][f][240:440]); start = Hr["P"][f][240]
    check("model can disagree with its author (FILM bull market)",
          peak / start > 1.35,
          f"FILM rallies x{peak/start:.2f} over the revival window")

    late = (H["U"][-1] - H["U"][-60]) / H["U"][-60]
    check("the yardstick stops (basket saturates)", late < 0.010,
          f"SRX growth over final 60 weeks: {100*late:.4f}%")

    bpk = H["B"].index(max(H["B"]))
    check("the peak is invisible in its moment", 20 < bpk < WEEKS - 100,
          f"backing peaks at week {bpk}, falls for {WEEKS-bpk} weeks after")

    ext, loop = sum(H["ext"]), sum(H["loop"])
    check("the feedback dominates the exogenous seed", loop > 2 * ext,
          f"loop supplied {100*loop/(loop+ext):.1f}% of capability growth")

    worst = [(g, run(Params(g=g))["U"][-1], run(Params(g=g))["idx"][-1])
             for g in (0.1, 0.55, 2.0, 20.0)]
    check("saturation bounds the loop for every gain",
          all(u <= Params().u_max + 1e-6 and math.isfinite(x) for _, u, x in worst),
          "  ".join(f"g={g}: SRX={u:.2f} idx={x:.1f}" for g, u, x in worst))

    # --- market texture. the reference is a real weekly index, inverted.
    sig = statistics.pstdev(r)
    check("weekly volatility matches a real index", 0.015 < sig < 0.032,
          f"sigma {100*sig:.2f}%/week, {100*sig*52**0.5:.1f}% annualised (real ~2.2% / 16%)")

    a = [abs(x) for x in r]; mu = statistics.mean(a)
    ac = sum((a[i]-mu)*(a[i-1]-mu) for i in range(1, len(a))) / sum((x-mu)**2 for x in a)
    check("volatility clusters", ac > 0.15,
          f"|return| autocorrelation {ac:.2f} (real ~0.25)")

    best = max(range(5, WEEKS), key=lambda t: idx[t] / idx[t - 5])
    check("sharp melt-ups, the inverted crash", idx[best]/idx[best-5] - 1 > 0.25,
          f"largest 5-week move {100*(idx[best]/idx[best-5]-1):+.1f}% "
          f"(inverted 2020 crash was about +47%)")

    occ = {i: H["reg"].count(i) for i in range(3)}
    check("the market has regimes and stays in them",
          all(v > WEEKS * 0.05 for v in occ.values()),
          f"quiet {occ[0]}w, choppy {occ[1]}w, stressed {occ[2]}w")

    flat = sum(1 for t in range(100, WEEKS) if abs(idx[t]/idx[t-100] - 1) < 0.06)
    check("long sideways stretches exist", flat > 150,
          f"{flat} weeks sit inside a 100-week window that moved less than 6%")

    # a real bull phase contains corrections. measure trough-to-peak over a
    # window, not an uninterrupted run, or a 2% dip ends every "rally".
    runs, i_ = [], 0
    while i_ < len(idx) - 26:
        j = max(range(i_ + 26, min(i_ + 420, len(idx))), key=lambda k: idx[k])
        if idx[j] / idx[i_] - 1 > 0.10:
            runs.append((i_, j, idx[j] / idx[i_] - 1)); i_ = j
        else:
            i_ += 13
    longest = max((b - a for a, b, _ in runs), default=0)
    check("multi-year rallies inside the bear market", longest > 104 and len(runs) >= 3,
          f"{len(runs)} advances over +10%, longest {longest} weeks "
          f"({max((g for *_, g in runs), default=0)*100:+.0f}% at its peak)")

    print("\n" + "=" * 74)
    print("DEC-004 TESTS, AND MARKET TEXTURE")
    print("=" * 74)
    for ok, name, detail in out:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {detail}")
    failed = [n for ok, n, _ in out if not ok]
    print("\n%d/%d passed" % (len(out) - len(failed), len(out)))
    return failed


if __name__ == "__main__":
    f = tests()
    assert not f, "design tests failed: " + "; ".join(f)
