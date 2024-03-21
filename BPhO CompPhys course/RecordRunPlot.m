recObj = audiorecorder;
Fs=48000;
filename = sprintf('myAudioData.wav');
disp('Start speaking.')
recordblocking(recObj, 2);
disp('End of Recording.');
doubleArray = getaudiodata(recObj);
audiowrite(filename,doubleArray,Fs);
y = audioread('myAudioData.wav');
plot(y)