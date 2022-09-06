import numpy as np
import mne
edf = mne.io.read_raw_edf(eeg.edf)
header = ','.join(edf.ch_names)
np.savetxt(eeg.csv, edf.get_data().T, delimiter=',', header=header)