import numpy as np
from scipy.fft import fft,fftshift

def myFFT(x,Fs,nFFT = None):
    if not isinstance(nFFT,int):
        nFFT = pow(2,20)
    X  = fftshift(fft(x,nFFT))
    f  = np.linspace(0,Fs,len(X),endpoint=False) - Fs/2
    return dict(mag=np.abs(X), phase=np.angle(X) , f=f)

