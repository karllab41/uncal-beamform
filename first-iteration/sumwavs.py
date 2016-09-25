import numpy as np
import scipy.io.wavfile as wav
import scikits.audiolab


def padsig(sig, delay):
    '''
    Pad the signal at the end with a delay
    '''
    return np.append(sig[delay:], np.zeros(delay) )

def revsig(sig, delay):
    '''
    Reverse the delay given a single.
    '''
    if delay == 0:
        return sig
    return np.append(np.zeros(delay), sig[:-delay])

def buildrecv(sigs, delmatrix):
    '''
    Based on the delay matrix, specifying the signal received at each receiver. 
    For each "true" signal, we sum them at the receiver with specified offsets.
    '''
    if len(sigs) != len(delmatrix.T):
        print "ERROR: Signals not aligned with delay array"
        return -1
    recvm = []
    for delarray in delmatrix:
        recvv = []
        for j,sig in enumerate(sigs):
            recvv += [padsig( sig, delarray[j])]
        recvm += [recvv]
    return recvm

def sumrecv(sigs):
    '''
    With an list of list of true signals, this will simply add them together to
    show what the microphone would receive
    '''
    sumsigs = []
    for sig in sigs:
        sumsigs += [np.array(sig).sum(axis=0)]
    sumsigs = np.array(sumsigs)
    return (sumsigs.T / sumsigs.max(axis=1)).T

def beamform(sigs, sigindex, delmatrix):
    '''
    NOT IMPLEMENTED YET
    '''
    if len(sigs) != len(delmatrix.T):
        print "ERROR: Signals not aligned with delay array"
        return -1
    delarray = delmatrix.T[sigindex]
    recovered = np.zeros(len(sigs[0]))
    for i,sig in enumerate(sigs):
        recovered += revsig(sig, delarray[i]) 
    recovered /= recovered.max() 

    return recovered

# Read wav files
(rate,sig1) = wav.read("delay1.wav")
(rate,sig2) = wav.read("delay2.wav")
(rate,sig3) = wav.read("delay3.wav")
(rate,sig4) = wav.read("delay4.wav")

# Use only one channel
sig1 = sig1[:,0]
sig2 = sig2[:,0]
sig3 = sig3[:,0]
sig4 = sig4[:,0]

# Generate the truth signals
allsigs = [sig1,sig2,sig3,sig4]
delmatrix = np.random.randint( 0, 1e4, size=(4,4)  )
np.fill_diagonal( delmatrix, 0 )

# Build the signals as heard from the receiver
recsigs = buildrecv( allsigs, delmatrix )
sumsigs = sumrecv( recsigs )

# Beamform based on known delay matrices
beamformed = beamform( sumsigs, 2, delmatrix )

# Play the output
scikits.audiolab.play(sumsigs[2], fs=rate)
scikits.audiolab.play(beamformed, fs=rate)
# scikits.audiolab.play(recvall, fs=rate)
