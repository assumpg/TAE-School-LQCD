Data for the anisotropic clover calculation
mpion  390 MeV
b_s ~ 0.123 fm, anisotropy factor ~ 3.5
diferent sets

detalls al fitxer "configs-details" en aquest directori and in https://arxiv.org/pdf/1109.2889

**Code files explanation:**
The files are build in a way that file 1 is included in file 2 and this is included in file 3
1. 'obtain_dataset.ipynb': explains a little the data and reads it from the desired .dat file.
2. 'applying_boot_jack.ipynb': explains the essential formulas for the bootstrap and jacknife methods and applies them to some data already obtained.
3. 'fitting.ipynb': fites only one of the data with exponential and linear fit for the time interval selected. Also computes the chi^2/dof. However it does NOT select the best fit in several time intervals.
4. 'otherfiles.ipynb': this code includes all the above but not the theoretical explanations. It process the data from the pion mass 1200. This code does the selection of the best fit and shows their systematical ans statistical errors.
