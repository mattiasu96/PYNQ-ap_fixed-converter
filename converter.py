from fxpmath import Fxp
import numpy as np

class Converter():

    def forward_conversion(self, input_data, signed, total_bits, fractional_bits):
        '''

        Converts input data from float/int python data types to ap_fixed with total bits and fractional_bits and returns its uint32 equivalent

        :param input_data: can be both a single int/float number or a numpy array
        :param signed: Boolean, if the input data is signed or not
        :param total_bits: numer of total bits used to represent the input data
        :param fractional_bits: number of fractional bits used to represent the input data. Integer bits = total bits - fractional bits
        :return: input data converted to uint32 format. 0.5 can be represented with 4 bits as 0.100. This is converted into 0100 (fractional point removed) and then converted to int.
                 0.5 as input is converted to 4 as uint32.

        '''
        fixed_point_representation = Fxp(input_data, signed=signed, n_word = total_bits, n_frac = fractional_bits)
        uint_coverted = np.uint32(fixed_point_representation.uraw())
        return uint_coverted



    def backward_conversion(self, input_data, total_bits, fractional_bits):
        '''
        Converts input data from uint32 format to float with total_bits and fractional_bits resolution

        :param input_data: can be both a single int/float number or a numpy array
        :param total_bits: numer of total bits used to represent the input data
        :param fractional_bits: number of fractional bits used to represent the input data. Integer bits = total bits - fractional bits
        :return: converted input data from uint32 to float
        '''

        if type(input_data) is not np.ndarray:
            input_data = np.array([input_data])

        #Function taken from here: https://discuss.pynq.io/t/how-to-use-ap-fixed-data-type-to-communicate-with-the-ip-made-by-the-vivado-hls/679/5
        condition = 1 << (total_bits - 1)
        mask = (~((1 << total_bits) - 1)) & 0xFFFFFFFF
        return np.where(input_data < condition, input_data, (input_data.view('u4') | mask).view('i4')) / (1 << fractional_bits)


if __name__ == '__main__':

    # simple main code to show how to use the code. As you might notice from the results, the number is backward converted with the available resolution in bits,
    # so 0.7 as input is converted to 5 and then back to 0.625 due to the limited number of fractional bits.
    converter = Converter()

    uint_result = converter.forward_conversion(input_data=0.7, signed=False, total_bits=4, fractional_bits=3)
    print('Forward converted input:',uint_result)

    fractional_result = converter.backward_conversion(input_data=uint_result, total_bits=4, fractional_bits=3)
    print('Backward converted input', fractional_result)
