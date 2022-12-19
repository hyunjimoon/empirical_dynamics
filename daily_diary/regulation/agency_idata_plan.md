output_format = dict(  
    prior_predictive=["ss_obs", "s_obs"],  
    posterior_predictive=["ss_obs_post", "s_obs_post"],  
    log_likelihood={  
        "loglik": "loglik"  
    },  
    coords={  
        "time": [n for n in range(precision['N'])],  
        "stock": setting['target_simulated_vector_names'],  
        "region": [r for r in range(precision['R'])]  
    },  
    #TODO automatic making target_simulated, observed_data, observed_data_post  
    dims={  
        'initial_outcome': ["stock"],  
        'integrated_result': ["time", "stock"],  
        "ss_obs": ["time"],  
        "s_obs": ["time"],  
        "ss_obs_post": ["time"],  
        "s_obs_post": ["time"],  
        'process_noise': ["time"],  
    }  
)

xr_lst = list()
xr.concat([xr for xr in xr_lst, groups = "prior_group"])