# load the codmod program
import codmod as cm
reload(cm)

# setup multithreading
import mkl
mkl.set_num_threads(4)

# setup the model
m = cm.codmod('Ab10','female')
m.set_covariates(covariate_list=['year','education_yrs_pc','ln(TFR)','neonatal_deaths_per1000','ln(LDI_pc)','HIV_prevalence_pct'], age_dummies=True, age_ref=30, normalize=True)
m.set_window(age_range=[15,45], year_range=[1980,2010])
m.set_pi_samples(age_samples=[15,25,35,45], year_samples=[1980,1990,2000,2010])

# load in the data
#m.load(cache_data=True)
m.use_cache()

# build the model and use MAP to find starting values
m.initialize_model()

# use MCMC to find posterior
m.sample(iter=5000, burn=0, thin=1)


