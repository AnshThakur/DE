%% read audio file
[x fs]=audioread('test_h.wav');
[t,f,ps]=calculateSpectrogram(x,fs);
%% add context
[data] = getps_temporal(ps,5);

%% load mean directions
load('mean_directions.mat');

DE=means*data;

DE=softmax(DE);


[H]=MI(DE);

H=normalize(1-H,0,1);
%[H time_taken] = getWeights(smooth(H,5),1);
H=smooth(H,10);





