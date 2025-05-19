# Set the population size
N = 763

# Define initial conditions
i0 = 1
s0 = N - i0
r0 = 0
y0 = [s0, i0, r0]

# Make the data struture, Where df is the data
stan_data = {
    "n_days": len(df.in_bed),
    "y0": y0,
    "t0": 0,
    "t": np.arange(1, len(df.in_bed)+1),
    "N": N,
    "cases": df.in_bed
}

# Fitting
sir_model_prior = CmdStanModel(stan_file = 'sir_model_prior.stan')
prior_check = sir_model_prior.sample(data = stan_data,
                                     iter_sampling = 2000,
                                     chains = 4,
                                     seed = 0)
