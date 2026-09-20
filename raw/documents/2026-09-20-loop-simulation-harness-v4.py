"""LONGING RESEARCH — DEC-008 / DEC-009 simulation.

Thirty years of weekly strikes, 1996-2026, across three markets, built on the
decisions as they now stand:

  DEC-008  a BEARER BOND is perpetual; its principal is attention; the one who
           leans issues it; the decline is made of CALLS, not defaults; and
           write-downs answer the counterparty, with a severity distribution
           whose tail supplies the melt-ups.
  DEC-009  Japan, Korea and the United States list the same practices apart and
           converge as events stop being local. One numeraire for all three.
  technology-waves
           arrival raises what substitution later takes. Every wave is a rise
           followed by a decline, and each has its own invisible peak.
  DEC-007  prices are quoted against STANDARD RETURN, which the basket makes
           heavier as the tools improve.

Stdlib only. `python3 sim.py` runs it and scores the tests.

v4 — TWO WAVES ARE MEASURED, FIVE ARE STILL PLACEHOLDERS.

The mobile and broadband arrival weeks and widths come from the WDI spine
retrieved 2026-09-20 (vintage 2026-07-13): a three-parameter logistic fit to
each country's annual series, the midpoint as the arrival week and the fitted
scale as the width. Mobile subscriptions are fit only up to the first year at or
above 100 per 100, because growth past that is lines per person, not people.
Weeks count from 1996-01 with each annual value at its year end. Internet use was
fitted as a check series and is not wired in: it is not a dial-up series.
Dial-up, the social web, smartphones, messaging and AI keep their placeholder
dates, since the sourcing round found no measured three-country series for
them. The measured boundary is week 1461, the end of 2023, the last year every
spine series is complete. Everything else is unchanged from v3 and uncalibrated.
"""
import math, random, statistics
from dataclasses import dataclass, field

WEEKS = 1565          # 1996-01 .. 2026-01, thirty years
MARKETS = ["KR", "JP", "US"]

#            ticker   alpha  beta   what alpha/beta mean:
#                                   alpha = how much a NEW way to connect creates
#                                           this practice
#                                   beta  = how much of it can later be done alone
UNIVERSE = [("LTR",   0.30, 0.85),   # handwritten letters
            ("CALL",  0.85, 0.70),   # unplanned calls — telephony CREATED these
            ("VISIT", 0.20, 0.45),   # unarranged in-person visits
            ("REFL",  0.05, 0.75),   # 사유 — reflection
            ("HAND",  0.15, 0.60),   # handmade objects
            ("WAIT",  0.10, 0.40),   # waiting without contact
            ("FILM",  0.25, 0.30),   # film photography
            ("VINYL", 0.15, 0.20),   # physical media
            ("WALK",  0.05, 0.05),   # aimless night walks
            ("BORE",  0.05, 0.05),   # boredom
            ("SOL",   0.00, 0.00)]   # solitude — the control: neither created
                                     # by a new device nor delegable to one

# Technology waves. Arrival week per market, then a lag before substitution.
# Week 0 = 1996. Ordered as the three countries actually met them; the early
# waves land far apart and the late ones land together, which is convergence
# arriving as history rather than as a parameter.
# The spread between the three columns IS the convergence. Early waves land
# years apart; late ones land in the same season. Nothing enforces that — it is
# what happened, and it is why the markets stop having their own weather.
# `creates` is how much of a wave's arrival makes new ways to reach a person
# rather than new ways to manage without one. It is the user's correction made
# into a number: the alumni boom and the telephone brought people together
# before anything was taken, and AI barely connects anyone at all.
# `width` is the fitted logistic scale in weeks where a wave is measured, and
# None where it is not, in which case Params.spread applies as before.
#        name          KR    JP    US   lag  strength creates  width  basis
WAVES = [("dialup",     10,  -40,  -80, 260, 0.9,   1.00,  None),  # placeholder
         ("mobile",    250,  255,  376, 300, 1.2,   1.30,   153),  # WDI IT.CEL.SETS.P2
         ("broadband", 458,  548,  564, 280, 1.0,   0.85,   159),  # WDI IT.NET.BBND.P2
         ("socialweb", 195,  450,  430, 300, 1.1,   1.40,  None),  # placeholder
         ("smartphone",690,  700,  675, 240, 1.6,   0.55,  None),  # placeholder
         ("messaging", 745,  760,  750, 260, 1.3,   0.90,  None),  # placeholder
         ("ai",       1355, 1358, 1352, 130, 2.2,   0.12,  None)]  # placeholder

MEASURED_UNTIL = 1461   # end of 2023: the last year every spine series is
                        # complete. The boundary is really one per series; this
                        # single number is the earliest of them.


@dataclass
class Params:
    # --- waves
    spread: float = 100.0      # adoption width, weeks
    u_max: float = 4.0        # basket saturation
    a50: float = 0.35

    # --- BEARER BOND, per DEC-008
    issue_k: float = 9.0      # arrival creates reliance
    issue_base: float = 0.0030  # people keep forming relationships with no new
                                # device at all. without this a practice can
                                # never be resumed and float only falls.    # arrival creates reliance
    call_k: float = 5.2       # substitution redeems it     # substitution redeems it
    default_h: float = 0.00035
    wd_base: float = 0.0160   # baseline withdrawal intensity
    wd_excite: float = 0.55   # a withdrawal raises the next one's odds
    wd_decay: float = 0.90
    sev_mild: float = 0.020   # most people lower it a little
    sev_tail: float = 0.15    # this share cut everything at once
    sev_full: float = 0.45

    # --- fundamentals
    gain_a: float = 2.80     # arrival raises the practice
    gain_s: float = 5.4     # substitution lowers it
    noise: float = 0.0016

    # --- events (DEC-003) and convergence (DEC-009)
    ev_rate: float = 0.85
    ev_mag: float = 0.055
    ev_true_share: float = 0.12
    research_pull: float = 0.5
    n_factors: int = 9
    arch: float = 3.0

    # --- positioning
    trend_w: float = 0.05      # ~20-week memory; a position follows a trend,
                               # not one week's move
    pos_k: float = 260.0       # how strongly a fundamental's drift attracts
                               # positions. NEGATIVE drift attracts shorts;
                               # positive drift — an arrival phase — attracts
                               # longs, and a crowded long unwinds into a drop.
    long_cap: float = 0.70     # how crowded the long side may get
    pi_long: float = 0.62      # below this a long is not crowded
    unwind_k: float = 1.00     # price impact of forced liquidation. smaller than
                               # squeeze_k on purpose: in this market the violent
                               # direction is up, which is the inversion DEC-004
                               # asks for.
    unwind_rate: float = 0.22
    pi_crowd: float = 0.76     # below this a short is not crowded
    pi_max: float = 0.80
    sq_record: float = 0.035   # what counts as a forced-covering event
    squeeze_k: float = 1.70
    cover_rate: float = 0.26
    mtm_force: float = 2.6
    over_cap: float = 0.60
    rebuild: float = 0.012
    prem_decay: float = 0.970


def logistic(x, w):
    return 1.0 / (1.0 + math.exp(-x / w)) if -60 < x / w < 60 else (0.0 if x < 0 else 1.0)


TOTAL_STRENGTH = sum(w[5] for w in WAVES)
TOTAL_CREATES = sum(w[5] * w[6] for w in WAVES)


def wave_state(t, m_i, p):
    """Arrival burst and substitution level, both normalised.

    Substitution runs 0..1 over the whole history, so its weekly increments sum
    to 1 and a coefficient is an elasticity rather than a magic number. Arrival
    increments sum to 1 the same way.
    """
    arrive = subst = 0.0
    for name, kr, jp, us, lag, strength, creates, width in WAVES:
        t0 = (kr, jp, us)[m_i]
        w = width if width is not None else p.spread
        a = logistic(t - t0, w)
        arrive += strength * creates * (a - logistic(t - 1 - t0, w))
        subst += strength * logistic(t - t0 - lag, w * 1.6)
    return arrive / TOTAL_CREATES, subst / TOTAL_STRENGTH


def run(p: Params, seed=11):
    rng = random.Random(seed)
    nM, nP = len(MARKETS), len(UNIVERSE)
    load = [[rng.gauss(0, 1) for _ in range(p.n_factors)] for _ in range(nP)]

    L = [[1000.0] * nP for _ in range(nM)]     # float: outstanding attention
    V = [[1.0] * nP for _ in range(nM)]
    z = [[0.0] * nP for _ in range(nM)]
    S = [[0.0] * nP for _ in range(nM)]
    last_ret = [[0.0] * nP for _ in range(nM)]
    trend = [[0.0] * nP for _ in range(nM)]   # positions are taken on trends
    excite = [0.0] * nM
    sub_prev = [0.0] * nM
    vol = 1.0

    H = {k: [] for k in ("U", "A", "idx", "idx0", "disp", "sq", "un",
                         "float", "calls", "defaults", "issued", "arrive")}
    H["mkt"] = [[] for _ in range(nM)]
    H["mkt0"] = [[] for _ in range(nM)]
    H["sub"] = [[] for _ in range(nM)]
    H["P"] = [[[] for _ in range(nP)] for _ in range(nM)]
    H["V"] = [[[] for _ in range(nP)] for _ in range(nM)]
    base = None

    for t in range(WEEKS):
        arr = [0.0] * nM
        sub = [0.0] * nM
        for mi in range(nM):
            arr[mi], sub[mi] = wave_state(t, mi, p)
        A = sum(sub) / nM                       # one global capability level
        U = 1.0 + (p.u_max - 1.0) * (A / (A + p.a50))
        psi = A / (A + p.a50)                   # global share of events

        # --- events: local early, common late
        shock = [[0.0] * nP for _ in range(nM)]
        truth = [[0.0] * nP for _ in range(nM)]
        ne = 0
        while rng.random() < p.ev_rate and ne < 5:
            ne += 1
            mag = rng.gauss(0, p.ev_mag * vol)
            k = rng.randrange(p.n_factors)
            common = rng.random() < psi
            hit_markets = range(nM) if common else [rng.randrange(nM)]
            for mi in hit_markets:
                for pi_ in range(nP):
                    h = mag * load[pi_][k] * 0.5
                    shock[mi][pi_] += h
                    truth[mi][pi_] += h * p.ev_true_share
        research_week = (t % 4 == 3)

        idx_sum = idx0_sum = 0.0
        mkt_ret = []
        sq_week = un_week = calls_w = def_w = iss_w = 0.0
        for mi in range(nM):
            d_sub = max(0.0, sub[mi] - sub_prev[mi])

            # --- contagion: self-exciting withdrawal (DEC-008)
            excite[mi] *= p.wd_decay
            fired = rng.random() < (p.wd_base + p.wd_excite * excite[mi]) * (1 + 220 * d_sub)
            if fired:
                excite[mi] += 1.0
                severity = p.sev_full if rng.random() < p.sev_tail else p.sev_mild
            else:
                severity = 0.0

            m_idx = m_idx0 = 0.0
            for pi_, (tick, alpha, beta) in enumerate(UNIVERSE):
                issue = (p.issue_k * alpha * arr[mi] + p.issue_base) * 1000.0
                call = p.call_k * beta * d_sub * L[mi][pi_]
                wd = severity * (0.35 + beta) * L[mi][pi_]
                dflt = p.default_h * L[mi][pi_]
                L[mi][pi_] = max(1.0, L[mi][pi_] + issue - call - wd - dflt)
                calls_w += call; def_w += dflt; iss_w += issue

                drift = p.gain_a * alpha * arr[mi] - p.gain_s * beta * d_sub
                V[mi][pi_] = max(1e-6, V[mi][pi_] *
                                 (1.0 + drift + truth[mi][pi_] + rng.gauss(0, p.noise)))

                # signed positioning. shorts are not the only thing that moves a
                # price: an arrival phase attracts real buyers.
                trend[mi][pi_] = (1 - p.trend_w) * trend[mi][pi_] + p.trend_w * drift
                raw = -p.pos_k * trend[mi][pi_]
                target = max(-p.long_cap, min(0.75, raw)) * L[mi][pi_]
                rate = 0.06 if abs(S[mi][pi_]) < abs(target) else p.rebuild
                S[mi][pi_] += rate * (target - S[mi][pi_])
                pi_ratio = S[mi][pi_] / L[mi][pi_] if L[mi][pi_] > 0 else 0.0

                z[mi][pi_] = z[mi][pi_] * p.prem_decay + (shock[mi][pi_] - truth[mi][pi_])
                if research_week:
                    z[mi][pi_] *= (1.0 - p.research_pull)

                # only a crowded short is hurt by a rising price. without the
                # gate, ordinary weekly volatility "squeezes" every position.
                pain = (max(0.0, last_ret[mi][pi_]) * max(0.0, pi_ratio - p.pi_crowd)
                        * p.mtm_force)
                over = min(p.over_cap, max(0.0, pi_ratio - p.pi_max) + pain)
                if over > 1e-4:
                    S[mi][pi_] = max(0.0, S[mi][pi_] - p.cover_rate * over * L[mi][pi_])
                    z[mi][pi_] += p.squeeze_k * p.cover_rate * over
                    if over > p.sq_record: sq_week += 1

                # the long side. a crowded long that stops being paid liquidates,
                # and the revival gives back what it lent.
                lpain = (max(0.0, -last_ret[mi][pi_]) * max(0.0, -pi_ratio - p.pi_long)
                         * p.mtm_force)
                lover = min(p.over_cap, max(0.0, -pi_ratio - p.long_cap) + lpain)
                if lover > 1e-4:
                    S[mi][pi_] = min(0.0, S[mi][pi_] + p.unwind_rate * lover * L[mi][pi_])
                    z[mi][pi_] -= p.unwind_k * p.unwind_rate * lover
                    if lover > p.sq_record: un_week += 1

                P = (V[mi][pi_] / U) * math.exp(z[mi][pi_])
                prev = H["P"][mi][pi_][-1] if H["P"][mi][pi_] else P
                last_ret[mi][pi_] = (P - prev) / prev if prev > 0 else 0.0
                H["P"][mi][pi_].append(P)
                H["V"][mi][pi_].append(V[mi][pi_])
                m_idx += P
                m_idx0 += V[mi][pi_] * math.exp(z[mi][pi_])

            H["mkt"][mi].append(m_idx)
            H["mkt0"][mi].append(m_idx0)
            H["sub"][mi].append(sub[mi])
            if len(H["mkt"][mi]) > 1:
                mkt_ret.append(m_idx / H["mkt"][mi][-2] - 1)
            idx_sum += m_idx; idx0_sum += m_idx0
            sub_prev[mi] = sub[mi]

        if base is None: base, base0 = idx_sum, idx0_sum
        avg = sum(abs(last_ret[mi][pi_]) for mi in range(nM) for pi_ in range(nP)) / (nM * nP)
        vol = 0.86 * vol + 0.14 * (1.0 + p.arch * avg)

        for k, v in (("U", U), ("A", A), ("idx", 100 * idx_sum / base),
                     ("idx0", 100 * idx0_sum / base0),
                     ("disp", statistics.pstdev(mkt_ret) if len(mkt_ret) > 1 else 0.0),
                     ("sq", sq_week), ("un", un_week), ("float", sum(map(sum, L))),
                     ("calls", calls_w), ("defaults", def_w), ("issued", iss_w),
                     ("arrive", sum(arr) / nM)):
            H[k].append(v)
    return H


# ----------------------------------------------------------------- tests

def _corr(a, b):
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den if den else 0.0


def market_corr(H, lo, hi):
    R = [[H["mkt"][i][t] / H["mkt"][i][t - 1] - 1 for t in range(lo + 1, hi)]
         for i in range(len(MARKETS))]
    return (_corr(R[0], R[1]) + _corr(R[0], R[2]) + _corr(R[1], R[2])) / 3


def advances(idx, thr=0.10):
    """Trough-to-peak advances over a window. A real bull phase contains
    corrections, so this must not break on a 2% dip."""
    out, i = [], 0
    while i < len(idx) - 26:
        j = max(range(i + 26, min(i + 420, len(idx))), key=lambda k: idx[k])
        if idx[j] / idx[i] - 1 > thr:
            out.append((i, j, idx[j] / idx[i] - 1)); i = j
        else:
            i += 13
    return out


def tests():
    p = Params()
    H = run(p)
    idx = H["idx"]
    r = [idx[t] / idx[t - 1] - 1 for t in range(1, WEEKS)]
    out = []
    def check(name, cond, detail): out.append((bool(cond), name, detail))

    # --- the shape DEC-004 asks for
    check("decline emerges, no drift constant", idx[-1] < 40,
          f"index {idx[0]:.0f} -> {idx[-1]:.1f} over thirty years")
    check("companion index separates yardstick from practice",
          H["idx0"][-1] > idx[-1] * 1.5,
          f"idx={idx[-1]:.1f} vs idx0={H['idx0'][-1]:.1f}; SRX {H['U'][0]:.2f} -> {H['U'][-1]:.2f}")

    sol = [t for t, a, b in UNIVERSE].index("SOL")
    ltr = [t for t, a, b in UNIVERSE].index("LTR")
    sp, lp = H["P"][0][sol], H["P"][0][ltr]
    check("the untouched practice falls only because the ruler grew",
          sp[-1] / sp[0] > 6 * (lp[-1] / lp[0]),
          f"SOL quote x{sp[-1]/sp[0]:.3f} vs LTR x{lp[-1]/lp[0]:.4f}")

    # --- DEC-008: the decline is redemption, not breach
    calls, defaults = sum(H["calls"]), sum(H["defaults"])
    check("the decline is made of calls, not defaults", calls > 2.5 * defaults,
          f"calls {calls:,.0f} against defaults {defaults:,.0f} "
          f"({100*calls/(calls+defaults):.0f}% redemption)")

    # --- DEC-008: a practice can be resumed
    rises = sum(1 for t in range(1, WEEKS) if H["float"][t] > H["float"][t - 1])
    check("float can rise — a practice can be resumed", rises > WEEKS * 0.2,
          f"total outstanding attention rose in {rises} of {WEEKS} weeks")

    # --- technology-waves: arrival leads substitution
    # measured on the FUNDAMENTAL, not the quote. An earlier version of this test
    # read the quote, which carries the event premium, and passed while the
    # arrival phase did not exist at all.
    call_i = [t for t, a, b in UNIVERSE].index("CALL")
    cv = H["V"][0][call_i]
    peak_w = max(range(WEEKS), key=lambda t: cv[t])
    check("arrival raises before substitution takes",
          cv[peak_w] > cv[0] * 1.10 and 40 < peak_w < WEEKS - 200,
          f"CALL's fundamental peaks at week {peak_w} at x{cv[peak_w]/cv[0]:.2f}, "
          f"then falls to x{cv[-1]/cv[0]:.3f}")

    check("rallies are not only short covering",
          sum(H["un"]) > 5,
          f"{int(sum(H['un']))} forced long liquidations against "
          f"{int(sum(H['sq']))} forced coverings — buyers exist, and they can be "
          f"carried out too")

    arrive, sub = H["arrive"], H["sub"][0]
    d_sub = [sub[t] - sub[t - 1] for t in range(1, WEEKS)]
    cross = [t for t in range(60, WEEKS - 60) if arrive[t] < d_sub[t - 1] <= arrive[t - 1]]
    check("substitution overtakes arrival inside the history", len(cross) >= 1,
          f"{len(cross)} crossings — each is an invisible peak nobody can see at the time")

    adv = advances(idx)
    longest = max((b - a for a, b, _ in adv), default=0)
    check("multi-year advances inside the decline", longest > 104 and len(adv) >= 3,
          f"{len(adv)} advances over +10%, longest {longest} weeks")

    # --- DEC-009: three markets, converging
    early, late = market_corr(H, 60, 400), market_corr(H, WEEKS - 400, WEEKS)
    check("the three markets converge", late > early + 0.25 and late > 0.7,
          f"mean pairwise return correlation {early:+.2f} early -> {late:+.2f} late")
    check("the three markets had their own weather first", early < 0.65,
          f"early correlation {early:+.2f}; the same practice died at different speeds")

    # --- market texture, against a real weekly index
    sig = statistics.pstdev(r)
    check("weekly volatility matches a real index", 0.015 < sig < 0.032,
          f"sigma {100*sig:.2f}%/week, {100*sig*52**0.5:.1f}% annualised (real ~2.2% / 16%)")
    a = [abs(x) for x in r]; mu = statistics.mean(a)
    ac = sum((a[i] - mu) * (a[i - 1] - mu) for i in range(1, len(a))) / sum((x - mu) ** 2 for x in a)
    check("volatility clusters", ac > 0.10, f"|return| autocorrelation {ac:.2f} (real ~0.25)")
    best = max(range(5, WEEKS), key=lambda t: idx[t] / idx[t - 5])
    check("sharp melt-ups, the inverted crash", idx[best] / idx[best - 5] - 1 > 0.20,
          f"largest five-week move {100*(idx[best]/idx[best-5]-1):+.1f}% at week {best} "
          f"(a real 2020 crash was -32%)")
    flat = sum(1 for t in range(100, WEEKS) if abs(idx[t] / idx[t - 100] - 1) < 0.06)
    check("long sideways stretches exist", flat > 120,
          f"{flat} weeks sit inside a 100-week window that moved less than 6%")

    # --- the published boundary
    check("the measured window ends inside the history", 0 < MEASURED_UNTIL < WEEKS,
          f"measured to week {MEASURED_UNTIL} of {WEEKS}; the institute publishes the rule")

    print("\n" + "=" * 76)
    print("LONGING RESEARCH — DEC-008 / DEC-009 / technology-waves — v4, two waves measured")
    print("=" * 76)
    for ok, name, detail in out:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {detail}")
    failed = [n for ok, n, _ in out if not ok]
    print("\n%d/%d passed" % (len(out) - len(failed), len(out)))
    return failed


if __name__ == "__main__":
    f = tests()
    assert not f, "design tests failed: " + "; ".join(f)
