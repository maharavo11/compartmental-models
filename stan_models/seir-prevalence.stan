functions {
  vector seir(real t,
             vector y, 
             real beta, 
             real sigma,
             real gamma,
             real N) {

      vector[4] dydt;

      real S = y[1];
      real E = y[2];
      real I = y[3];
      real R = y[4];
      
      dydt[1] = -beta * I * S / N;
      dydt[2] = beta * I * S / N - gamma * E;
      dydt[3] =  gamma * E - sigma * I;
      dydt[4] =  sigma * I;
      
      return dydt;
  }
}
data {
  int<lower=1> n_days;
  vector[4] y0;
  real t0;
  array[n_days] real t;
  int N;
  array[n_days] int<lower=0> cases;
}

parameters {
  real<lower=0> sigma;
  real<lower=0> beta;
  real<lower=0> gamma;
  real<lower=0> phi_inv;
}
transformed parameters{
  array[n_days] vector[4] y;
  real<lower=0> phi = 1. / phi_inv;
  
  y = ode_rk45(seir, y0, t0, t, beta, sigma, gamma, N);
}
model {
    //priors
    beta ~ normal(4, 2); //truncated at 0
    sigma ~ normal(0.8, 0.3); //truncated at 0
    gamma ~ normal(1.0, 0.25);
    phi_inv ~ exponential(5);
    
    //sampling distribution
    cases ~ neg_binomial_2(y[:, 3], phi);
}
generated quantities {
  real R0 = beta / sigma;
  real recovery_time = 1 / sigma;
  real incubation_period = 1 / gamma;

  array[n_days] real pred_cases;
  pred_cases = neg_binomial_2_rng(y[:,3], phi);
}
