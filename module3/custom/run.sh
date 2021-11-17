nvcc blur.cu -o blur
./blur "testimage.png"
nvcc sharp.cu -o sharp
./sharp "testimage.png"