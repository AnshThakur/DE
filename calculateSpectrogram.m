function [t,f, ps ] = calculateSpectrogram(y,fs)

%% requires voicebox toolbox. using default vales: 20 ms frame size with 10 ms overlap

[t,f,g]=spgrambw(y,fs,'pJcw',90.5/2);
ps=g;

end

