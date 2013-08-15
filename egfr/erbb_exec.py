"""
Model M1a: Extrinsic apoptosis model with "embedded together" model of MOMP.
"""


from pysb import *
import pickle

#from egfr import shared
Model()
from egfr import chen_modules

# Declare monomers
chen_modules.rec_monomers()
chen_modules.mapk_monomers()
chen_modules.akt_monomers()
chen_modules.crosstalk_monomers()

# Generate the upstream and downstream sections
chen_modules.rec_events()
chen_modules.mapk_events()
chen_modules.akt_events()
chen_modules.crosstalk_events()

# Initial protein concentrations
chen_modules.rec_initial_lig_hEGF()
chen_modules.rec_initial()
chen_modules.mapk_initial()
chen_modules.akt_initial()
chen_modules.crosstalk_initial()

#Declare observables
Observable('obsAKTPP', AKT(bpip3=None, both=None, S='PP'))
Observable('obsErbB1_ErbB_P_CE', erbb(bd=1, ty='1', st='P') % erbb(bd=1))
Observable('obsERKPP', ERK(st='PP'))

Observable('obsErbB1_lig', erbb(bd=None, ty='1', st='U', bl=ANY))
Observable('obsErbB1_ErbB', erbb(bd=1, ty='1', st='U') % erbb(bd=1, st='U'))
Observable('obsErbB1_ErbB1', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='1', st='U'))
Observable('obsErbB1_ErbB2', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='2', st='U'))
Observable('obsErbB1_ErbB3', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='3', st='U'))
Observable('obsErbB1_ErbB4', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='4', st='U'))
Observable('obsErbB1_ErbB_ATP', erbb(bd=1, ty='1', st='U', b=2) % erbb(bd=1, st='U') % ATP(b=2))

Observable('obsErbB_GAP_GRB2', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
Observable('obsErbB_GAP_GRB2_GAB1U', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='U'))
Observable('obsErbB_GAP_GRB2_GAB1P', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='P'))
Observable('obsErbB_GAP_GRB2_GAB1P_PI3K', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='P', bpi3k=4) % PI3K(bgab1=4))
Observable('obsPIP3', PIP(S='PIP3'))
Observable('obsAKT_PIP3', AKT(bpip3=1, S='U') % PIP(S='PIP3', bakt=1))
Observable('obsAKTP', AKT(S='P'))

# with open('model_species', 'rb') as handle:
#     model_species = pickle.loads(handle.read())
# n = 1
# for i in model_species:
#     Observable('m'+str(n), i)
#     n = n + 1

