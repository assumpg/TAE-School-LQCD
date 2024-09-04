def mean_sigma_boot(blck,nsc,nt,nboot):
    # Compute pmean using the numpy function mean for the nsc axis
    pmean=np.zeros((nboot,nt))
    pmean = np.mean(blck, axis=0)

    # Bootstrap sampling
    # Generate bootstrap indices
    pmeanboot=np.zeros((nboot,nt))
    x = np.random.uniform(size=(nsc, nboot))
    for k in range(nt):
        for j in range(nboot):
            for i in range(nsc):
                pmeanboot[j,k]+=blck[int(x[i,j]*nsc),k]
            pmeanboot[j,k]*=nsc_

    # Compute EMpoint
    kt = 1
    EMpoint=np.zeros((nboot,nt-kt))
    EMpoint = np.log(pmeanboot[:, :-kt] / pmeanboot[:, kt:]) / kt   # Shape (nboot, nt - kt)/Shape (nboot, nt - kt)

    # Compute mean and standard deviation of EMpoint
    mean = np.mean(EMpoint, axis=0)
    variance = np.mean((EMpoint - mean) ** 2, axis=0) * nsc * nsc1_
    sigma = np.sqrt(variance)

    # Compute mean and standard deviation of the correlator
    E_b=EMpoint.T

    mean_cor = np.mean(pmeanboot[:,:-1], axis=0)
    variance_cor = np.mean((pmeanboot[:,:-1] - mean_cor) ** 2, axis=0) * nsc * nsc1_
    sigma_cor = np.sqrt(variance_cor)

    return mean, sigma, mean_cor, sigma_cor, E_b
