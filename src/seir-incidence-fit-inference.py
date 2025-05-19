# Load in the data using pandas
import pandas as pd
df = pd.read_csv('incidence.csv')

# Set the population size
N = 763

# Define initial conditions
i0 = 1
e0 = 0
s0 = N - i0
r0 = 0
c0 = 0
y0 = [s0, e0, i0, r0, c0]

# Make the data struture
seir_data = {
    "n_days": len(df.x),
    "y0": y0,
    "t0": 0,
    "t": np.arange(1, len(df.x)+1),
    "N": N,
    "cases": df.x
}

seir_incidence_model = CmdStanModel(stan_file = 'seir-incidence.stan')

fit_seir_incidence_model = seir_incidence_model.sample(data = seir_data,
                                                       iter_sampling = 2000,
                                                       chains = 4,
                                                       seed = 0)

seir_incidence_summary = fit_seir_incidence_model.summary()
seir_incidence_summary.filter(items=("sigma", "beta", "recovery_time", "gamma", "incubation_period"), axis=0)

#inference
post_pred = pd.DataFrame(seir_incidence_summary.filter(like="pred_incidence", axis=0))
post_pred["t"] = range(1, 14)
post_pred["incidence"] = list(df.x)

post_pred = post_pred.set_index("t")
