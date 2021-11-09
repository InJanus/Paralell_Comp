struct DataBlock {
    unsigned char *dev_bitmap;
    CPUAnimBitmap *bitmap;
};
   
// clean up memory allocated on the GPU
void cleanup( DataBlock *d ) {
    cudaFree( d->dev_bitmap );
}

void generate_frame( DataBlock *d, int ticks ) {
    dim3 blocks(DIM/16,DIM/16);
    dim3 threads(16,16);
    kernel<<<blocks,threads>>>( d->dev_bitmap, ticks );
    HANDLE_ERROR( cudaMemcpy( d->bitmap->get_ptr(),
    d->dev_bitmap,
    d->bitmap->image_size(),
    cudaMemcpyDeviceToHost ) );
}
   
int main( void ) {
    DataBlock data;
    CPUAnimBitmap bitmap( DIM, DIM, &data );
    data.bitmap = &bitmap;
    HANDLE_ERROR( cudaMalloc( (void**)&data.dev_bitmap,
    bitmap.image_size() ) );
    bitmap.anim_and_exit( (void (*)(void*,int))generate_frame,
    (void (*)(void*))cleanup );
}