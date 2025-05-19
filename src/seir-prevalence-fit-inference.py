import pandas as pd
df = pd.read_csv('flu_data.csv')

# Convert the dates to datetime format
df.Date = pd.to_datetime(df.date)

# Use date as index
df = df.set_index("date")

# Set the population size
N = 763

# Define initial conditions
i0 = 1
e0 = 0
s0 = N - i0
r0 = 0
y0 = [s0, e0, i0, r0]

# Make the data struture
seir_data = {
    "n_days": len(df.in_bed),
    "y0": y0,
    "t0": 0,
    "t": np.arange(1, len(df.in_bed)+1),
    "N": N,
    "cases": df.in_bed
}

seir_model = CmdStanModel(stan_file = 'seir_prevalence.stan')

fit_seir_model = seir_model.sample(data = seir_data,
                                   iter_sampling = 2000,
                                   chains = 4,
                                   seed = 0)

seir_summary = fit_seir_model.summary()
seir_summary.filter(items=("sigma", "beta", "recovery_time", "gamma", "incubation_period"), axis=0)

#inference
post_pred = pd.DataFrame(seir_summary.filter(like="pred_cases", axis=0))
post_pred["t"] = range(1, 15)
post_pred["cases"] = list(df.in_bed)

post_pred = post_pred.set_index("t")
