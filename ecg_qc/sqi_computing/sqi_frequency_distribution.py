import numpy as np


def psqi(ecg_signal: list, sampling_frequency: int) -> float:

    n = len(ecg_signal)
    t = 1 / sampling_frequency

    yf = np.fft.fft(ecg_signal)
    xf = np.linspace(0.0, 1.0/(2.0*t), n//2)

    fft_results = []

    for offset, element in enumerate(xf):
        fft_results.append([xf[offset], np.abs(yf[offset])])

    pds_num = [np.abs(yf[idx]) for idx in range(len(xf)) if xf[idx]>=5 and xf[idx]<=15]
    pds_denom = [np.abs(yf[idx]) for idx in range(len(xf)) if xf[idx]>=5 and xf[idx]<=40]
    p_sqi_score = float(round(sum(pds_num) / sum(pds_denom), 2)) 

    return p_sqi_score


def bassqi(ecg_signal, sampling_frequency):
    n = len(ecg_signal)
    t = 1 / sampling_frequency

    yf = np.fft.fft(ecg_signal)
    xf = np.linspace(0.0, 1.0/(2.0*t), n//2)

    fft_results = []

    for offset, element in enumerate(xf):
        fft_results.append([xf[offset], np.abs(yf[offset])])

    pds_num = [np.abs(yf[idx]) for idx in range(len(xf)) if xf[idx]>=0 and xf[idx]<=1]
    pds_denom = [np.abs(yf[idx]) for idx in range(len(xf)) if xf[idx]>=0 and xf[idx]<=40]

    bas_sqi_score = float(round(1 - (sum(pds_num) / sum(pds_denom)), 2))

    return bas_sqi_score
