# Set the population size
N = 763

# Define initial conditions
i0 = 1
s0 = N - i0
r0 = 0
y0 = [s0, i0, r0]

# Make the data struture
stan_data = {
    "n_days": len(df.in_bed),
    "y0": y0,
    "t0": 0,
    "t": np.arange(1, len(df.in_bed)+1),
    "N": N,
    "cases": df.in_bed
}

sir_model = CmdStanModel(stan_file = 'sir_model.stan')

# Fitting
fit_sir_model = sir_model.sample(data = stan_data,
                                 iter_sampling = 2000,
                                 chains = 4,
                                 seed = 0)

# Summary
sir_summary = fit_sir_model.summary()
sir_summary.filter(items=("sigma", "beta", "recovery_time"), axis=0)

# Posterior prediction
post_pred = pd.DataFrame(sir_summary.filter(like="pred_cases", axis=0))
post_pred["t"] = range(1, 15)
post_pred["cases"] = list(df.in_bed)

post_pred = post_pred.set_index("t")
post_pred
