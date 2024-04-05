pgs_SD = 6.17208 #from UKBB fluid int test, item 20016
pgs_mean = 2.14121 #from UKBB fluid int test, item 20016
pgs_beta = 0.149 #from pgscatalog.org/score/PGS003724/ validation stats

def pgs_to_iq(pgs_raw, pgs_mean, pgs_SD, pgs_beta, iq_SD=15,iq_mean=100):
    pgs_z = (pgs_raw-pgs_mean) / pgs_SD
    iq_z = pgs_z * pgs_beta
    return iq_z * iq_SD + iq_mean

print(pgs_to_iq(13, pgs_mean, pgs_SD, pgs_beta))
