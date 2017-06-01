from pydub import AudioSegment
import pdb
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile
import wave
import nussl
from sklearn.decomposition import FastICA, PCA
myAudioFile = "s1.wav"
sound1 = AudioSegment.from_file(myAudioFile, format="wav")
# pdb.set_trace()
# new = sound1.low_pass_filter(5000)
# new.export("out2.wav", format="wav")

sound_monoL = sound1.split_to_mono()[0]
sound_monoR = sound1.split_to_mono()[1]
sound_monoR_inv = sound_monoR.invert_phase()
sound_monoL_inv = sound_monoL.invert_phase()
# sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)
# sound_CentersOut = sound_monoR.overlay(sound_monoL_inv)
# sound_CentersOut.export("outAudio.wav", format="wav")
sound_monoR_inv.export("right.wav", format="wav")
sound_monoL.export("left.wav", format="wav")
pdb.set_trace()


rate, data = scipy.io.wavfile.read('s1.wav')
# pdb.set_trace()
rate2, data2 = scipy.io.wavfile.read("left.wav")
rate2, data3 = scipy.io.wavfile.read("right.wav")
scipy.io.wavfile.write('central.wav',rate, (data2+data3))


central = AudioSegment.from_file('central.wav', format="wav")
central_inv = central.invert_phase()
central_inv.export("central_inv.wav", format="wav")
rate, background = scipy.io.wavfile.read('central_inv.wav')
scipy.io.wavfile.write('mono.wav', rate, (data[:,0]+data[:, 1])/2)
rate2, mono = scipy.io.wavfile.read("mono.wav")
scipy.io.wavfile.write('final.wav',rate, mono+background)


# ica = FastICA(n_components=2)
# S_ = ica.fit_transform(data)  # Reconstruct signals
# A_ = ica.mixing_  # Get estimated mixing matrix
# scipy.io.wavfile.write('s4.wav',rate, S_[:, 0])
# scipy.io.wavfile.write('s3.wav',rate, S_[:, 0])


# history = nussl.AudioSignal('s2.wav')
# repet = nussl.Repet(history)
# repet.run()
# background, foreground = repet.make_audio_signals()
# background.write_audio_to_file('history_background2.wav')
# foreground.write_audio_to_file('history_foreground2.wav')