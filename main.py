import argparse
from io import StringIO, BytesIO
from PIL import Image


def compressor(input_file, output_file, compression_cycles):

    # https://stackoverflow.com/questions/30771652/how-to-perform-jpeg-compression-in-python-without-writing-reading
    buffer = BytesIO()
    img = Image.open(input_file)
    img.save(fp=buffer, format="JPEG", quality=100)
    img.show()

    buffer.seek(0)
    for i in range(compression_cycles):
        imagefrombuffer = Image.open(buffer)
        buffer2 = BytesIO()
        imagefrombuffer.save(fp=buffer2, format="JPEG", quality=90)
        buffer.truncate(0)
        buffer = buffer2

    with open(output_file, "wb") as out:
        buffer.seek(0)
        out.write(buffer.read())
    imag = Image.open(output_file)
    imag.show()



    # buffer = BytesIO()
    # img.save(buffer, "JPEG")    # https://jdhao.github.io/2019/07/20/pil_jpeg_image_quality/, using 75 as default
    #
    # # buffer.seek(0)
    # with open(output_file, "wb") as handle:
    #     handle.write(buffer.getbuffer())




if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-i', '--input', help='Input file name')
    parser.add_argument('-c', '--cycles', help='Compression cycles')

    args = parser.parse_args()
    input = args.input
    output = args.output
    cycles = int(args.cycles)
    compressor(input, output, cycles)


